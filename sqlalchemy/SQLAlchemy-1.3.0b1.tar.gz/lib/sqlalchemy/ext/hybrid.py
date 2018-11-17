# ext/hybrid.py
# Copyright (C) 2005-2018 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

r"""Define attributes on ORM-mapped classes that have "hybrid" behavior.

"hybrid" means the attribute has distinct behaviors defined at the
class level and at the instance level.

The :mod:`~sqlalchemy.ext.hybrid` extension provides a special form of
method decorator, is around 50 lines of code and has almost no
dependencies on the rest of SQLAlchemy.  It can, in theory, work with
any descriptor-based expression system.

Consider a mapping ``Interval``, representing integer ``start`` and ``end``
values. We can define higher level functions on mapped classes that produce
SQL expressions at the class level, and Python expression evaluation at the
instance level.  Below, each function decorated with :class:`.hybrid_method` or
:class:`.hybrid_property` may receive ``self`` as an instance of the class, or
as the class itself::

    from sqlalchemy import Column, Integer
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import Session, aliased
    from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

    Base = declarative_base()

    class Interval(Base):
        __tablename__ = 'interval'

        id = Column(Integer, primary_key=True)
        start = Column(Integer, nullable=False)
        end = Column(Integer, nullable=False)

        def __init__(self, start, end):
            self.start = start
            self.end = end

        @hybrid_property
        def length(self):
            return self.end - self.start

        @hybrid_method
        def contains(self, point):
            return (self.start <= point) & (point <= self.end)

        @hybrid_method
        def intersects(self, other):
            return self.contains(other.start) | self.contains(other.end)

Above, the ``length`` property returns the difference between the
``end`` and ``start`` attributes.  With an instance of ``Interval``,
this subtraction occurs in Python, using normal Python descriptor
mechanics::

    >>> i1 = Interval(5, 10)
    >>> i1.length
    5

When dealing with the ``Interval`` class itself, the :class:`.hybrid_property`
descriptor evaluates the function body given the ``Interval`` class as
the argument, which when evaluated with SQLAlchemy expression mechanics
returns a new SQL expression::

    >>> print Interval.length
    interval."end" - interval.start

    >>> print Session().query(Interval).filter(Interval.length > 10)
    SELECT interval.id AS interval_id, interval.start AS interval_start,
    interval."end" AS interval_end
    FROM interval
    WHERE interval."end" - interval.start > :param_1

ORM methods such as :meth:`~.Query.filter_by` generally use ``getattr()`` to
locate attributes, so can also be used with hybrid attributes::

    >>> print Session().query(Interval).filter_by(length=5)
    SELECT interval.id AS interval_id, interval.start AS interval_start,
    interval."end" AS interval_end
    FROM interval
    WHERE interval."end" - interval.start = :param_1

The ``Interval`` class example also illustrates two methods,
``contains()`` and ``intersects()``, decorated with
:class:`.hybrid_method`. This decorator applies the same idea to
methods that :class:`.hybrid_property` applies to attributes.   The
methods return boolean values, and take advantage of the Python ``|``
and ``&`` bitwise operators to produce equivalent instance-level and
SQL expression-level boolean behavior::

    >>> i1.contains(6)
    True
    >>> i1.contains(15)
    False
    >>> i1.intersects(Interval(7, 18))
    True
    >>> i1.intersects(Interval(25, 29))
    False

    >>> print Session().query(Interval).filter(Interval.contains(15))
    SELECT interval.id AS interval_id, interval.start AS interval_start,
    interval."end" AS interval_end
    FROM interval
    WHERE interval.start <= :start_1 AND interval."end" > :end_1

    >>> ia = aliased(Interval)
    >>> print Session().query(Interval, ia).filter(Interval.intersects(ia))
    SELECT interval.id AS interval_id, interval.start AS interval_start,
    interval."end" AS interval_end, interval_1.id AS interval_1_id,
    interval_1.start AS interval_1_start, interval_1."end" AS interval_1_end
    FROM interval, interval AS interval_1
    WHERE interval.start <= interval_1.start
        AND interval."end" > interval_1.start
        OR interval.start <= interval_1."end"
        AND interval."end" > interval_1."end"

.. _hybrid_distinct_expression:

Defining Expression Behavior Distinct from Attribute Behavior
--------------------------------------------------------------

Our usage of the ``&`` and ``|`` bitwise operators above was
fortunate, considering our functions operated on two boolean values to
return a new one.   In many cases, the construction of an in-Python
function and a SQLAlchemy SQL expression have enough differences that
two separate Python expressions should be defined.  The
:mod:`~sqlalchemy.ext.hybrid` decorators define the
:meth:`.hybrid_property.expression` modifier for this purpose.   As an
example we'll define the radius of the interval, which requires the
usage of the absolute value function::

    from sqlalchemy import func

    class Interval(object):
        # ...

        @hybrid_property
        def radius(self):
            return abs(self.length) / 2

        @radius.expression
        def radius(cls):
            return func.abs(cls.length) / 2

Above the Python function ``abs()`` is used for instance-level
operations, the SQL function ``ABS()`` is used via the :data:`.func`
object for class-level expressions::

    >>> i1.radius
    2

    >>> print Session().query(Interval).filter(Interval.radius > 5)
    SELECT interval.id AS interval_id, interval.start AS interval_start,
        interval."end" AS interval_end
    FROM interval
    WHERE abs(interval."end" - interval.start) / :abs_1 > :param_1

.. note:: When defining an expression for a hybrid property or method, the
   expression method **must** retain the name of the original hybrid, else
   the new hybrid with the additional state will be attached to the class
   with the non-matching name. To use the example above::

    class Interval(object):
        # ...

        @hybrid_property
        def radius(self):
            return abs(self.length) / 2

        # WRONG - the non-matching name will cause this function to be
        # ignored
        @radius.expression
        def radius_expression(cls):
            return func.abs(cls.length) / 2

   This is also true for other mutator methods, such as
   :meth:`.hybrid_property.update_expression`. This is the same behavior
   as that of the ``@property`` construct that is part of standard Python.

Defining Setters
----------------

Hybrid properties can also define setter methods.  If we wanted
``length`` above, when set, to modify the endpoint value::

    class Interval(object):
        # ...

        @hybrid_property
        def length(self):
            return self.end - self.start

        @length.setter
        def length(self, value):
            self.end = self.start + value

The ``length(self, value)`` method is now called upon set::

    >>> i1 = Interval(5, 10)
    >>> i1.length
    5
    >>> i1.length = 12
    >>> i1.end
    17

.. _hybrid_bulk_update:

Allowing Bulk ORM Update
------------------------

A hybrid can define a custom "UPDATE" handler for when using the
:meth:`.Query.update` method, allowing the hybrid to be used in the
SET clause of the update.

Normally, when using a hybrid with :meth:`.Query.update`, the SQL
expression is used as the column that's the target of the SET.  If our
``Interval`` class had a hybrid ``start_point`` that linked to
``Interval.start``, this could be substituted directly::

    session.query(Interval).update({Interval.start_point: 10})

However, when using a composite hybrid like ``Interval.length``, this
hybrid represents more than one column.   We can set up a handler that will
accommodate a value passed to :meth:`.Query.update` which can affect
this, using the :meth:`.hybrid_property.update_expression` decorator.
A handler that works similarly to our setter would be::

    class Interval(object):
        # ...

        @hybrid_property
        def length(self):
            return self.end - self.start

        @length.setter
        def length(self, value):
            self.end = self.start + value

        @length.update_expression
        def length(cls, value):
            return [
                (cls.end, cls.start + value)
            ]

Above, if we use ``Interval.length`` in an UPDATE expression as::

    session.query(Interval).update(
        {Interval.length: 25}, synchronize_session='fetch')

We'll get an UPDATE statement along the lines of::

    UPDATE interval SET end=start + :value

In some cases, the default "evaluate" strategy can't perform the SET
expression in Python; while the addition operator we're using above
is supported, for more complex SET expressions it will usually be necessary
to use either the "fetch" or False synchronization strategy as illustrated
above.

.. versionadded:: 1.2 added support for bulk updates to hybrid properties.

Working with Relationships
--------------------------

There's no essential difference when creating hybrids that work with
related objects as opposed to column-based data. The need for distinct
expressions tends to be greater.  The two variants we'll illustrate
are the "join-dependent" hybrid, and the "correlated subquery" hybrid.

Join-Dependent Relationship Hybrid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Consider the following declarative
mapping which relates a ``User`` to a ``SavingsAccount``::

    from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.ext.hybrid import hybrid_property

    Base = declarative_base()

    class SavingsAccount(Base):
        __tablename__ = 'account'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
        balance = Column(Numeric(15, 5))

    class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=False)

        accounts = relationship("SavingsAccount", backref="owner")

        @hybrid_property
        def balance(self):
            if self.accounts:
                return self.accounts[0].balance
            else:
                return None

        @balance.setter
        def balance(self, value):
            if not self.accounts:
                account = Account(owner=self)
            else:
                account = self.accounts[0]
            account.balance = value

        @balance.expression
        def balance(cls):
            return SavingsAccount.balance

The above hybrid property ``balance`` works with the first
``SavingsAccount`` entry in the list of accounts for this user.   The
in-Python getter/setter methods can treat ``accounts`` as a Python
list available on ``self``.

However, at the expression level, it's expected that the ``User`` class will
be used in an appropriate context such that an appropriate join to
``SavingsAccount`` will be present::

    >>> print Session().query(User, User.balance).\
    ...     join(User.accounts).filter(User.balance > 5000)
    SELECT "user".id AS user_id, "user".name AS user_name,
    account.balance AS account_balance
    FROM "user" JOIN account ON "user".id = account.user_id
    WHERE account.balance > :balance_1

Note however, that while the instance level accessors need to worry
about whether ``self.accounts`` is even present, this issue expresses
itself differently at the SQL expression level, where we basically
would use an outer join::

    >>> from sqlalchemy import or_
    >>> print (Session().query(User, User.balance).outerjoin(User.accounts).
    ...         filter(or_(User.balance < 5000, User.balance == None)))
    SELECT "user".id AS user_id, "user".name AS user_name,
    account.balance AS account_balance
    FROM "user" LEFT OUTER JOIN account ON "user".id = account.user_id
    WHERE account.balance <  :balance_1 OR account.balance IS NULL

Correlated Subquery Relationship Hybrid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We can, of course, forego being dependent on the enclosing query's usage
of joins in favor of the correlated subquery, which can portably be packed
into a single column expression. A correlated subquery is more portable, but
often performs more poorly at the SQL level. Using the same technique
illustrated at :ref:`mapper_column_property_sql_expressions`,
we can adjust our ``SavingsAccount`` example to aggregate the balances for
*all* accounts, and use a correlated subquery for the column expression::

    from sqlalchemy import Column, Integer, ForeignKey, Numeric, String
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.ext.hybrid import hybrid_property
    from sqlalchemy import select, func

    Base = declarative_base()

    class SavingsAccount(Base):
        __tablename__ = 'account'
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
        balance = Column(Numeric(15, 5))

    class User(Base):
        __tablename__ = 'user'
        id = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=False)

        accounts = relationship("SavingsAccount", backref="owner")

        @hybrid_property
        def balance(self):
            return sum(acc.balance for acc in self.accounts)

        @balance.expression
        def balance(cls):
            return select([func.sum(SavingsAccount.balance)]).\
                    where(SavingsAccount.user_id==cls.id).\
                    label('total_balance')

The above recipe will give us the ``balance`` column which renders
a correlated SELECT::

    >>> print s.query(User).filter(User.balance > 400)
    SELECT "user".id AS user_id, "user".name AS user_name
    FROM "user"
    WHERE (SELECT sum(account.balance) AS sum_1
    FROM account
    WHERE account.user_id = "user".id) > :param_1

.. _hybrid_custom_comparators:

Building Custom Comparators
---------------------------

The hybrid property also includes a helper that allows construction of
custom comparators. A comparator object allows one to customize the
behavior of each SQLAlchemy expression operator individually.  They
are useful when creating custom types that have some highly
idiosyncratic behavior on the SQL side.

.. note::  The :meth:`.hybrid_property.comparator` decorator introduced
   in this section **replaces** the use of the
   :meth:`.hybrid_property.expression` decorator.  They cannot be used together.

The example class below allows case-insensitive comparisons on the attribute
named ``word_insensitive``::

    from sqlalchemy.ext.hybrid import Comparator, hybrid_property
    from sqlalchemy import func, Column, Integer, String
    from sqlalchemy.orm import Session
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class CaseInsensitiveComparator(Comparator):
        def __eq__(self, other):
            return func.lower(self.__clause_element__()) == func.lower(other)

    class SearchWord(Base):
        __tablename__ = 'searchword'
        id = Column(Integer, primary_key=True)
        word = Column(String(255), nullable=False)

        @hybrid_property
        def word_insensitive(self):
            return self.word.lower()

        @word_insensitive.comparator
        def word_insensitive(cls):
            return CaseInsensitiveComparator(cls.word)

Above, SQL expressions against ``word_insensitive`` will apply the ``LOWER()``
SQL function to both sides::

    >>> print Session().query(SearchWord).filter_by(word_insensitive="Trucks")
    SELECT searchword.id AS searchword_id, searchword.word AS searchword_word
    FROM searchword
    WHERE lower(searchword.word) = lower(:lower_1)

The ``CaseInsensitiveComparator`` above implements part of the
:class:`.ColumnOperators` interface.   A "coercion" operation like
lowercasing can be applied to all comparison operations (i.e. ``eq``,
``lt``, ``gt``, etc.) using :meth:`.Operators.operate`::

    class CaseInsensitiveComparator(Comparator):
        def operate(self, op, other):
            return op(func.lower(self.__clause_element__()), func.lower(other))

.. _hybrid_reuse_subclass:

Reusing Hybrid Properties across Subclasses
-------------------------------------------

A hybrid can be referred to from a superclass, to allow modifying
methods like :meth:`.hybrid_property.getter`, :meth:`.hybrid_property.setter`
to be used to redefine those methods on a subclass.  This is similar to
how the standard Python ``@property`` object works::

    class FirstNameOnly(Base):
        # ...

        first_name = Column(String)

        @hybrid_property
        def name(self):
            return self.first_name

        @name.setter
        def name(self, value):
            self.first_name = value

    class FirstNameLastName(FirstNameOnly):
        # ...

        last_name = Column(String)

        @FirstNameOnly.name.getter
        def name(self):
            return self.first_name + ' ' + self.last_name

        @name.setter
        def name(self, value):
            self.first_name, self.last_name = value.split(' ', 1)

Above, the ``FirstNameLastName`` class refers to the hybrid from
``FirstNameOnly.name`` to repurpose its getter and setter for the subclass.

When overriding :meth:`.hybrid_property.expression` and
:meth:`.hybrid_property.comparator` alone as the first reference
to the superclass, these names conflict
with the same-named accessors on the class-level :class:`.QueryableAttribute`
object returned at the class level.  To override these methods when
referring directly to the parent class descriptor, add
the special qualifier :attr:`.hybrid_property.overrides`, which will
de-reference the instrumented attribute back to the hybrid object::

    class FirstNameLastName(FirstNameOnly):
        # ...

        last_name = Column(String)

        @FirstNameOnly.overrides.expression
        def name(cls):
            return func.concat(cls.first_name, ' ', cls.last_name)

.. versionadded:: 1.2 Added :meth:`.hybrid_property.getter` as well as the
   ability to redefine accessors per-subclass.


Hybrid Value Objects
--------------------

Note in our previous example, if we were to compare the
``word_insensitive`` attribute of a ``SearchWord`` instance to a plain
Python string, the plain Python string would not be coerced to lower
case - the ``CaseInsensitiveComparator`` we built, being returned by
``@word_insensitive.comparator``, only applies to the SQL side.

A more comprehensive form of the custom comparator is to construct a
*Hybrid Value Object*. This technique applies the target value or
expression to a value object which is then returned by the accessor in
all cases.   The value object allows control of all operations upon
the value as well as how compared values are treated, both on the SQL
expression side as well as the Python value side.   Replacing the
previous ``CaseInsensitiveComparator`` class with a new
``CaseInsensitiveWord`` class::

    class CaseInsensitiveWord(Comparator):
        "Hybrid value representing a lower case representation of a word."

        def __init__(self, word):
            if isinstance(word, basestring):
                self.word = word.lower()
            elif isinstance(word, CaseInsensitiveWord):
                self.word = word.word
            else:
                self.word = func.lower(word)

        def operate(self, op, other):
            if not isinstance(other, CaseInsensitiveWord):
                other = CaseInsensitiveWord(other)
            return op(self.word, other.word)

        def __clause_element__(self):
            return self.word

        def __str__(self):
            return self.word

        key = 'word'
        "Label to apply to Query tuple results"

Above, the ``CaseInsensitiveWord`` object represents ``self.word``,
which may be a SQL function, or may be a Python native.   By
overriding ``operate()`` and ``__clause_element__()`` to work in terms
of ``self.word``, all comparison operations will work against the
"converted" form of ``word``, whether it be SQL side or Python side.
Our ``SearchWord`` class can now deliver the ``CaseInsensitiveWord``
object unconditionally from a single hybrid call::

    class SearchWord(Base):
        __tablename__ = 'searchword'
        id = Column(Integer, primary_key=True)
        word = Column(String(255), nullable=False)

        @hybrid_property
        def word_insensitive(self):
            return CaseInsensitiveWord(self.word)

The ``word_insensitive`` attribute now has case-insensitive comparison
behavior universally, including SQL expression vs. Python expression
(note the Python value is converted to lower case on the Python side
here)::

    >>> print Session().query(SearchWord).filter_by(word_insensitive="Trucks")
    SELECT searchword.id AS searchword_id, searchword.word AS searchword_word
    FROM searchword
    WHERE lower(searchword.word) = :lower_1

SQL expression versus SQL expression::

    >>> sw1 = aliased(SearchWord)
    >>> sw2 = aliased(SearchWord)
    >>> print Session().query(
    ...                    sw1.word_insensitive,
    ...                    sw2.word_insensitive).\
    ...                        filter(
    ...                            sw1.word_insensitive > sw2.word_insensitive
    ...                        )
    SELECT lower(searchword_1.word) AS lower_1,
    lower(searchword_2.word) AS lower_2
    FROM searchword AS searchword_1, searchword AS searchword_2
    WHERE lower(searchword_1.word) > lower(searchword_2.word)

Python only expression::

    >>> ws1 = SearchWord(word="SomeWord")
    >>> ws1.word_insensitive == "sOmEwOrD"
    True
    >>> ws1.word_insensitive == "XOmEwOrX"
    False
    >>> print ws1.word_insensitive
    someword

The Hybrid Value pattern is very useful for any kind of value that may
have multiple representations, such as timestamps, time deltas, units
of measurement, currencies and encrypted passwords.

.. seealso::

    `Hybrids and Value Agnostic Types
    <http://techspot.zzzeek.org/2011/10/21/hybrids-and-value-agnostic-types/>`_
    - on the techspot.zzzeek.org blog

    `Value Agnostic Types, Part II
    <http://techspot.zzzeek.org/2011/10/29/value-agnostic-types-part-ii/>`_ -
    on the techspot.zzzeek.org blog

.. _hybrid_transformers:

Building Transformers
----------------------

A *transformer* is an object which can receive a :class:`.Query`
object and return a new one.   The :class:`.Query` object includes a
method :meth:`.with_transformation` that returns a new :class:`.Query`
transformed by the given function.

We can combine this with the :class:`.Comparator` class to produce one type
of recipe which can both set up the FROM clause of a query as well as assign
filtering criterion.

Consider a mapped class ``Node``, which assembles using adjacency list
into a hierarchical tree pattern::

    from sqlalchemy import Column, Integer, ForeignKey
    from sqlalchemy.orm import relationship
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

    class Node(Base):
        __tablename__ = 'node'
        id = Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('node.id'))
        parent = relationship("Node", remote_side=id)

Suppose we wanted to add an accessor ``grandparent``.  This would
return the ``parent`` of ``Node.parent``.  When we have an instance of
``Node``, this is simple::

    from sqlalchemy.ext.hybrid import hybrid_property

    class Node(Base):
        # ...

        @hybrid_property
        def grandparent(self):
            return self.parent.parent

For the expression, things are not so clear.   We'd need to construct
a :class:`.Query` where we :meth:`~.Query.join` twice along
``Node.parent`` to get to the ``grandparent``.   We can instead return
a transforming callable that we'll combine with the
:class:`.Comparator` class to receive any :class:`.Query` object, and
return a new one that's joined to the ``Node.parent`` attribute and
filtered based on the given criterion::

    from sqlalchemy.ext.hybrid import Comparator

    class GrandparentTransformer(Comparator):
        def operate(self, op, other):
            def transform(q):
                cls = self.__clause_element__()
                parent_alias = aliased(cls)
                return q.join(parent_alias, cls.parent).\
                            filter(op(parent_alias.parent, other))
            return transform

    Base = declarative_base()

    class Node(Base):
        __tablename__ = 'node'
        id =Column(Integer, primary_key=True)
        parent_id = Column(Integer, ForeignKey('node.id'))
        parent = relationship("Node", remote_side=id)

        @hybrid_property
        def grandparent(self):
            return self.parent.parent

        @grandparent.comparator
        def grandparent(cls):
            return GrandparentTransformer(cls)

The ``GrandparentTransformer`` overrides the core
:meth:`.Operators.operate` method at the base of the
:class:`.Comparator` hierarchy to return a query-transforming
callable, which then runs the given comparison operation in a
particular context. Such as, in the example above, the ``operate``
method is called, given the :attr:`.Operators.eq` callable as well as
the right side of the comparison ``Node(id=5)``.  A function
``transform`` is then returned which will transform a :class:`.Query`
first to join to ``Node.parent``, then to compare ``parent_alias``
using :attr:`.Operators.eq` against the left and right sides, passing
into :class:`.Query.filter`:

.. sourcecode:: pycon+sql

    >>> from sqlalchemy.orm import Session
    >>> session = Session()
    {sql}>>> session.query(Node).\
    ...        with_transformation(Node.grandparent==Node(id=5)).\
    ...        all()
    SELECT node.id AS node_id, node.parent_id AS node_parent_id
    FROM node JOIN node AS node_1 ON node_1.id = node.parent_id
    WHERE :param_1 = node_1.parent_id
    {stop}

We can modify the pattern to be more verbose but flexible by separating
the "join" step from the "filter" step.  The tricky part here is ensuring
that successive instances of ``GrandparentTransformer`` use the same
:class:`.AliasedClass` object against ``Node``.  Below we use a simple
memoizing approach that associates a ``GrandparentTransformer``
with each class::

    class Node(Base):

        # ...

        @grandparent.comparator
        def grandparent(cls):
            # memoize a GrandparentTransformer
            # per class
            if '_gp' not in cls.__dict__:
                cls._gp = GrandparentTransformer(cls)
            return cls._gp

    class GrandparentTransformer(Comparator):

        def __init__(self, cls):
            self.parent_alias = aliased(cls)

        @property
        def join(self):
            def go(q):
                return q.join(self.parent_alias, Node.parent)
            return go

        def operate(self, op, other):
            return op(self.parent_alias.parent, other)

.. sourcecode:: pycon+sql

    {sql}>>> session.query(Node).\
    ...            with_transformation(Node.grandparent.join).\
    ...            filter(Node.grandparent==Node(id=5))
    SELECT node.id AS node_id, node.parent_id AS node_parent_id
    FROM node JOIN node AS node_1 ON node_1.id = node.parent_id
    WHERE :param_1 = node_1.parent_id
    {stop}

The "transformer" pattern is an experimental pattern that starts
to make usage of some functional programming paradigms.
While it's only recommended for advanced and/or patient developers,
there's probably a whole lot of amazing things it can be used for.

"""
from .. import util
from ..orm import attributes, interfaces

HYBRID_METHOD = util.symbol('HYBRID_METHOD')
"""Symbol indicating an :class:`InspectionAttr` that's
   of type :class:`.hybrid_method`.

   Is assigned to the :attr:`.InspectionAttr.extension_type`
   attibute.

   .. seealso::

    :attr:`.Mapper.all_orm_attributes`

"""

HYBRID_PROPERTY = util.symbol('HYBRID_PROPERTY')
"""Symbol indicating an :class:`InspectionAttr` that's
    of type :class:`.hybrid_method`.

   Is assigned to the :attr:`.InspectionAttr.extension_type`
   attibute.

   .. seealso::

    :attr:`.Mapper.all_orm_attributes`

"""


class hybrid_method(interfaces.InspectionAttrInfo):
    """A decorator which allows definition of a Python object method with both
    instance-level and class-level behavior.

    """

    is_attribute = True
    extension_type = HYBRID_METHOD

    def __init__(self, func, expr=None):
        """Create a new :class:`.hybrid_method`.

        Usage is typically via decorator::

            from sqlalchemy.ext.hybrid import hybrid_method

            class SomeClass(object):
                @hybrid_method
                def value(self, x, y):
                    return self._value + x + y

                @value.expression
                def value(self, x, y):
                    return func.some_function(self._value, x, y)

        """
        self.func = func
        self.expression(expr or func)

    def __get__(self, instance, owner):
        if instance is None:
            return self.expr.__get__(owner, owner.__class__)
        else:
            return self.func.__get__(instance, owner)

    def expression(self, expr):
        """Provide a modifying decorator that defines a
        SQL-expression producing method."""

        self.expr = expr
        if not self.expr.__doc__:
            self.expr.__doc__ = self.func.__doc__
        return self


class hybrid_property(interfaces.InspectionAttrInfo):
    """A decorator which allows definition of a Python descriptor with both
    instance-level and class-level behavior.

    """

    is_attribute = True
    extension_type = HYBRID_PROPERTY

    def __init__(
            self, fget, fset=None, fdel=None,
            expr=None, custom_comparator=None, update_expr=None):
        """Create a new :class:`.hybrid_property`.

        Usage is typically via decorator::

            from sqlalchemy.ext.hybrid import hybrid_property

            class SomeClass(object):
                @hybrid_property
                def value(self):
                    return self._value

                @value.setter
                def value(self, value):
                    self._value = value

        """
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.expr = expr
        self.custom_comparator = custom_comparator
        self.update_expr = update_expr
        util.update_wrapper(self, fget)

    def __get__(self, instance, owner):
        if instance is None:
            return self._expr_comparator(owner)
        else:
            return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

    def _copy(self, **kw):
        defaults = {
            key: value
            for key, value in self.__dict__.items()
            if not key.startswith("_")}
        defaults.update(**kw)
        return type(self)(**defaults)

    @property
    def overrides(self):
        """Prefix for a method that is overriding an existing attribute.

        The :attr:`.hybrid_property.overrides` accessor just returns
        this hybrid object, which when called at the class level from
        a parent class, will de-reference the "instrumented attribute"
        normally returned at this level, and allow modifying decorators
        like :meth:`.hybrid_property.expression` and
        :meth:`.hybrid_property.comparator`
        to be used without conflicting with the same-named attributes
        normally present on the :class:`.QueryableAttribute`::

            class SuperClass(object):
                # ...

                @hybrid_property
                def foobar(self):
                    return self._foobar

            class SubClass(SuperClass):
                # ...

                @SuperClass.foobar.overrides.expression
                def foobar(cls):
                    return func.subfoobar(self._foobar)

        .. versionadded:: 1.2

        .. seealso::

            :ref:`hybrid_reuse_subclass`

         """
        return self

    def getter(self, fget):
        """Provide a modifying decorator that defines a getter method.

        .. versionadded:: 1.2

        """

        return self._copy(fget=fget)

    def setter(self, fset):
        """Provide a modifying decorator that defines a setter method."""

        return self._copy(fset=fset)

    def deleter(self, fdel):
        """Provide a modifying decorator that defines a deletion method."""

        return self._copy(fdel=fdel)

    def expression(self, expr):
        """Provide a modifying decorator that defines a SQL-expression
        producing method.

        When a hybrid is invoked at the class level, the SQL expression given
        here is wrapped inside of a specialized :class:`.QueryableAttribute`,
        which is the same kind of object used by the ORM to represent other
        mapped attributes.   The reason for this is so that other class-level
        attributes such as docstrings and a reference to the hybrid itself may
        be maintained within the structure that's returned, without any
        modifications to the original SQL expression passed in.

        .. note::

           when referring to a hybrid property  from an owning class (e.g.
           ``SomeClass.some_hybrid``), an instance of
           :class:`.QueryableAttribute` is returned, representing the
           expression or comparator object as well as this  hybrid object.
           However, that object itself has accessors called ``expression`` and
           ``comparator``; so when attempting to override these decorators on a
           subclass, it may be necessary to qualify it using the
           :attr:`.hybrid_property.overrides` modifier first.  See that
           modifier for details.

        .. seealso::

            :ref:`hybrid_distinct_expression`

        """

        return self._copy(expr=expr)

    def comparator(self, comparator):
        """Provide a modifying decorator that defines a custom
        comparator producing method.

        The return value of the decorated method should be an instance of
        :class:`~.hybrid.Comparator`.

        .. note::  The :meth:`.hybrid_property.comparator` decorator
           **replaces** the use of the :meth:`.hybrid_property.expression`
           decorator.  They cannot be used together.

        When a hybrid is invoked at the class level, the
        :class:`~.hybrid.Comparator` object given here is wrapped inside of a
        specialized :class:`.QueryableAttribute`, which is the same kind of
        object used by the ORM to represent other mapped attributes.   The
        reason for this is so that other class-level attributes such as
        docstrings and a reference to the hybrid itself may be maintained
        within the structure that's returned, without any modifications to the
        original comparator object passed in.

        .. note::

           when referring to a hybrid property  from an owning class (e.g.
           ``SomeClass.some_hybrid``), an instance of
           :class:`.QueryableAttribute` is returned, representing the
           expression or comparator object as this  hybrid object.  However,
           that object itself has accessors called ``expression`` and
           ``comparator``; so when attempting to override these decorators on a
           subclass, it may be necessary to qualify it using the
           :attr:`.hybrid_property.overrides` modifier first.  See that
           modifier for details.

        """
        return self._copy(custom_comparator=comparator)

    def update_expression(self, meth):
        """Provide a modifying decorator that defines an UPDATE tuple
        producing method.

        The method accepts a single value, which is the value to be
        rendered into the SET clause of an UPDATE statement.  The method
        should then process this value into individual column expressions
        that fit into the ultimate SET clause, and return them as a
        sequence of 2-tuples.  Each tuple
        contains a column expression as the key and a value to be rendered.

        E.g.::

            class Person(Base):
                # ...

                first_name = Column(String)
                last_name = Column(String)

                @hybrid_property
                def fullname(self):
                    return first_name + " " + last_name

                @fullname.update_expression
                def fullname(cls, value):
                    fname, lname = value.split(" ", 1)
                    return [
                        (cls.first_name, fname),
                        (cls.last_name, lname)
                    ]

        .. versionadded:: 1.2

        """
        return self._copy(update_expr=meth)

    @util.memoized_property
    def _expr_comparator(self):
        if self.custom_comparator is not None:
            return self._get_comparator(self.custom_comparator)
        elif self.expr is not None:
            return self._get_expr(self.expr)
        else:
            return self._get_expr(self.fget)

    def _get_expr(self, expr):

        def _expr(cls):
            return ExprComparator(cls, expr(cls), self)
        util.update_wrapper(_expr, expr)

        return self._get_comparator(_expr)

    def _get_comparator(self, comparator):

        proxy_attr = attributes.create_proxied_attribute(self)

        def expr_comparator(owner):
            return proxy_attr(
                owner, self.__name__, self, comparator(owner),
                doc=comparator.__doc__ or self.__doc__)
        return expr_comparator


class Comparator(interfaces.PropComparator):
    """A helper class that allows easy construction of custom
    :class:`~.orm.interfaces.PropComparator`
    classes for usage with hybrids."""

    property = None

    def __init__(self, expression):
        self.expression = expression

    def __clause_element__(self):
        expr = self.expression
        if hasattr(expr, '__clause_element__'):
            expr = expr.__clause_element__()
        return expr

    def adapt_to_entity(self, adapt_to_entity):
        # interesting....
        return self


class ExprComparator(Comparator):
    def __init__(self, cls, expression, hybrid):
        self.cls = cls
        self.expression = expression
        self.hybrid = hybrid

    def __getattr__(self, key):
        return getattr(self.expression, key)

    @property
    def info(self):
        return self.hybrid.info

    def _bulk_update_tuples(self, value):
        if isinstance(self.expression, attributes.QueryableAttribute):
            return self.expression._bulk_update_tuples(value)
        elif self.hybrid.update_expr is not None:
            return self.hybrid.update_expr(self.cls, value)
        else:
            return [(self.expression, value)]

    @property
    def property(self):
        return self.expression.property

    def operate(self, op, *other, **kwargs):
        return op(self.expression, *other, **kwargs)

    def reverse_operate(self, op, other, **kwargs):
        return op(other, self.expression, **kwargs)
