'''

    kabaret.flow2.values

    Defines the basic value types:
        Value:          Stores a python object. Provides set() and get() methods
                        The Value is the base for all other values types.
        
        SessionValue:   Store a python object, but does not save it to the value store.
                        This means the value get reset to its default for each session,
                        and that it is not shared with other sessions.

        IntValue
        FloatValue
        StringValue
        DictValue:     Subclasses of Value each with their suitable methods (see sources...)

        OrderedStringSetValue:      
                        Stores an ordered by score set of strings.

        HashValue:      Stores a 2D list of (str, str)
                        This should be prefered over DictValue if:
                            - Your keys and values are strings.
                            - You need direct key access has/get/set.

        ComputedValue:  Stores a python object generated by the parent's compute_child_value(value) method.
                        The parent Object must implement this method and call value.set(something).
                        If set_cached(True) is called, the computation is not requested unless touch() is
                        called.
                        If store_value(True) is called, the computed value is also stored in the
                        value store (may be usefull if other applications read it...).

        ChoiceValue:    Stores a value which is one of a predifined possible values.

        MultiChoiceValue: Stores a list where each item is one of a predifined possible values.

        Ref:            References an Ojbect.
'''
from __future__ import print_function

from .exceptions import WIPException
from .exceptions import MissingChildError, MissingRelationError, RefSourceError, RefSourceTypeError
from .object import Object


class Value(Object):

    ICON = 'value'
    DEFAULT_EDITOR = None

    def __init__(self, parent, name):
        super(Value, self).__init__(parent, name)
        self._default_value = None
        self._watched = False

    def set_watched(self, b):
        self._watched = bool(b)

    def notify(self):
        '''
        Subclasses can override this to do something after values change.
        Default implementation calls 'child_value_changed' in the parent object if
        self._watched is True.
        '''
        if self._watched:
            self._mng.parent.child_value_changed(self)

    def set_default_value(self, value):
        self._default_value = value

    def revert_to_default(self):
        self.set(self._default_value)

    def set(self, value):
        if value == self._default_value:
            self._mng.del_value()
        else:
            self._mng.set_value(value)
        self.notify()

    def get(self):
        return self._mng.get_value(self._default_value)


class SessionValue(Value):
    '''
    This Value does not store itself in the value store.
    It will reset to its default value for each session.
    '''

    def set_default_value(self, value):
        super(SessionValue, self).set_default_value(value)
        self._value = value

    def set(self, value):
        self._value = value
        self._mng._on_value_changed()
        self.notify()

    def get(self):
        return self._value


class _TypedValue(Value):

    def validate(self, value):
        raise NotImplementedError()


class IntValue(_TypedValue):

    DEFAULT_EDITOR = 'int'

    def validate(self, value):
        if not value and value != 0:
            return self._default_value
        try:
            return int(value)
        except TypeError:
            raise TypeError(
                'Invalid value type %r for %s (must be a int)' % (
                    value, self.oid(),
                )
            )

    def set(self, value):
        value = self.validate(value)
        super(IntValue, self).set(value)

    def incr(self, by=1):
        self._mng.incr_value(by)

    def decr(self, by=1):
        self._mng.decr_value(by)


class BoolValue(_TypedValue):

    DEFAULT_EDITOR = 'bool'

    def validate(self, value):
        try:
            return bool(value)
        except TypeError:
            raise TypeError(
                'Invalid value type %r for %s (must be a bool)' % (
                    value, self.oid(),
                )
            )

    def set(self, value):
        value = self.validate(value)
        super(BoolValue, self).set(value)

    # deprecated, not needed (yet...)
    # def toggle(self):
    #     #FIXME: do this in the value store to be able to use redis pipeline !
    #     self.set(not self.get())


class FloatValue(_TypedValue):

    DEFAULT_EDITOR = 'float'

    def validate(self, value):
        if not value and value != 0:
            return self._default_value
        try:
            return float(value)
        except TypeError:
            raise TypeError(
                'Invalid value type %r for %s (must be a float)' % (
                    value, self.oid(),
                )
            )

    def set(self, value):
        super(FloatValue, self).set(self.validate(value))


class StringValue(_TypedValue):

    DEFAULT_EDITOR = 'string'

    def validate(self, value):
        try:
            return str(value)
        except TypeError:
            raise TypeError(
                'Invalid value type %r for %s (must be a str)' % (
                    value, self.oid(),
                )
            )

    def set(self, value):
        super(StringValue, self).set(self.validate(value))


class DictValue(_TypedValue):

    DEFAULT_EDITOR = 'mapping'

    def validate(self, value):
        try:
            return dict(value)
        except TypeError:
            raise TypeError(
                'Invalid value type %r for %s (must be a dict)' % (
                    value, self.oid(),
                )
            )

    def set(self, value):
        super(DictValue, self).set(self.validate(value))


class OrderedStringSetValue(Value):
    '''
    A list off string ordered by score.
    You cant set that value, you can only edit it.
    '''

    DEFAULT_EDITOR = 'set'

    def set_default_value(self, value):
        # We dont support default value but the Relation will give us one.
        # So the only acceptable value is None:
        if value is not None:
            raise Exception(
                'You cant configure the default of an OrderedStringSetValue')

    def revert_to_default(self):
        self._mng.del_value()

    def set(self, value):
        raise Exception('You cant set an OrderedStringSetValue')

    def get(self):
        return self._mng.oss_get()

    def get_range(self, first, last):
        return self._mng.oss_get_range(first, last)

    def has(self, member):
        self._mng.oss_has(member)
        self.notify()

    def add(self, member, score):
        self._mng.oss_add(member, score)
        self.notify()

    def remove(self, member):
        self._mng.oss_remove(member)
        self.notify()

    def len(self):
        return self._mng.oss_len()

    def get_score(self, member):
        return self._mng.oss_get_score(member)

    def set_score(self, member, score):
        self._mng.oss_set_score(member, score)
        self.notify()


class HashValue(_TypedValue):

    DEFAULT_EDITOR = 'mapping'

    def validate(self, value):
        if isinstance(value, dict):
            values = value.items()
        else:
            values = value
        try:
            return [(str(i), str(j)) for i, j in values]
        except:
            raise TypeError(
                'Invalid value type %r for %s (must be a mapping: dict or 2d list/tuple)' % (
                    value, self.oid(),
                )
            )

    def get_key(self, key):
        # hget
        return self._mng.hash_get_key(key)

    def has_key(self, key):
        # hexists
        return self._mng.hash_has_key(key)

    def del_key(self, key):
        # hdel
        self._mng.del_hash_key(key)
        self.notify()

    def as_dict(self):
        # hgetall
        return self._mng.get_hash_as_dict()

    def keys(self):
        # hkeys
        return self._mng.get_hash_keys()

    def len(self):
        # hlen
        return self._mng.get_hash_len()

    def update(self, **new_values):
        # hmset
        self._mng.update_hash(new_values)
        self.notify()

    def set_key(self, key, value):
        # hset
        self._mng.set_hash_key(key, value)
        self.notify()

    def set(self, value):
        value = self.validate(value)
        self._mng.set_hash(value)
        self.notify()

    def get(self):
        return self._mng.get_hash()


class ComputedValue(Value):

    def __init__(self, parent, name):
        super(ComputedValue, self).__init__(parent, name)
        self._cached = False
        self._value = None
        self._dirty = True

    def set_cached(self, b):
        self._cached = bool(b)

    def set_store_value(self, b):
        self._store_value = bool(b)

    def touch(self):
        self._dirty = True
        super(ComputedValue, self).touch()

    def compute(self):
        '''
        Subclasses can override this to compute the value (and call set()).
        Default implementation calls 'compute_child_value' in the parent object.
        '''
        self._mng.parent.compute_child_value(self)

    def get(self):
        if self._dirty:
            self.compute()
        return self._value

    def set(self, value):
        if self._store_value:
            super(ComputedValue, self).set(value)
        self._value = value
        if self._cached:
            self._dirty = False
        self.notify()


class ChoiceValue(Value):
    '''
    This Value provides a list of potential/acceptable values.
    You can set the CHOICE class attribute to define this list.

    If STRICT_CHOICES is True, the value must exists in the CHOICES attribute
    or a ValueError will be raised by set()
    If STRICT_CHOICES is False, any value can do.

    '''
    DEFAULT_EDITOR = 'choice'

    STRICT_CHOICES = True
    CHOICES = []

    def choices(self):
        return self.__class__.CHOICES

    def set(self, value):
        if self.STRICT_CHOICES and value not in self.choices():
            # we still touch ourself, so we sure GUI refresh with the unchanged value:
            self.touch()
            raise ValueError('Invalid value %r. Should be one of %r' %
                             (value, self.choices()))
        super(ChoiceValue, self).set(value)


class MultiChoiceValue(ChoiceValue):
    '''
    A MultiChoiceValue is like a Choice but stores a list of those acceptable values.
    '''
    DEFAULT_EDITOR = 'multichoice'

    def set(self, value):
        if self.STRICT_CHOICES:
            if not isinstance(value, list):
                value = [value]
            for v in value:
                if v not in self.choices():
                    raise ValueError(
                        'Invalid value %r. Should be one of %r' % (v, self.choices()))
        super(ChoiceValue, self).set(value)


class Ref(Value):
    '''
    A Ref stores a reference to an Object.
    The set() method accepts only Object of the type (or list of types) in SOURCE_TYPE class attribute.
    The get() method returns the Object.
    If you only need the Object's oid, use get_source_oid() as it does not require object lookup.
    '''

    ICON = 'ref'
    DEFAULT_EDITOR = 'ref'

    SOURCE_TYPE = None  # class_or_type_or_tuple

    @staticmethod
    def resolve_refs(object):
        max = 10
        nb = 0
        #print('?', object.oid(), object)
        while isinstance(object, Ref):
            object = object.get()
            # print('  ->', object.oid(), object)
            nb += 1
            if nb > max:
                1 / 0
        #print('=', object.oid(), object)
        return object

    def __init__(self, parent, name):
        super(Ref, self).__init__(parent, name)
        self.source_object = None

    def get(self):
        # print('GET SOURCE FOR', self.oid())
        # print('   >', self.get_source_oid())
        if self.source_object is None:
            source_oid = self.get_source_oid()
            if source_oid is None:
                return None
            try:
                self.source_object = self._mng.get_object(source_oid)
            except (MissingChildError, MissingRelationError):
                raise RefSourceError(self.oid(), source_oid)

        return self.source_object

    def get_source_oid(self):
        return super(Ref, self).get()

    def can_set(self, source_object):
        try:
            self._assert_source_compatible(source_object)
        except ValueError:
            return False

        source_object = self.resolve_refs(source_object)

        try:
            self._validate_source_object(source_object)
        except RefSourceTypeError:
            return False
        else:
            return True

    def _assert_source_compatible(self, object):
        if object.root() is not self.root():
            raise ValueError('Cannot connect to another flow!')

    def _validate_source_object(self, source_object):
        if source_object is not None:
            if self.SOURCE_TYPE is not None and not isinstance(source_object, self.SOURCE_TYPE):
                if 0:
                    # was too geeky :/
                    raise RefSourceTypeError(
                        'Ref %s cannot point to %r (should be a %r, but is a %s)' % (
                            self.oid(), source_object.oid(), self.SOURCE_TYPE, source_object.__class__
                        )
                    )
                else:
                    raise RefSourceTypeError(
                        'This is not a %s' % (self.SOURCE_TYPE.__name__,))
        return source_object

    def set(self, new_source_object):

        if new_source_object is not None:
            self._assert_source_compatible(new_source_object)
            new_source_object = self.resolve_refs(new_source_object)
            new_source_object = self._validate_source_object(new_source_object)
            new_oid = new_source_object.oid()
        else:
            new_oid = None

        old_source_oid = self.get_source_oid()
        if old_source_oid == new_oid:
            return

        super(Ref, self).set(new_oid)
        if old_source_oid is not None:
            try:
                old_source_object = self._mng.get_object(old_source_oid)
            except (MissingChildError, MissingRelationError):
                pass
            else:
                old_source_object._mng.remove_ref(self)

        self.source_object = new_source_object
        if self.source_object is not None:
            self.source_object._mng.add_ref(self)

#---OLD
    def source_touched(self):
        raise WIPException('I dont think this is still in use.')
        #print('++SOURCE TOUCHED', self.oid(), self.source_object.oid())
        self.touch()  # will touch my parent.

#---OLD
    def source_value_changed(self, old_value, new_value):
        raise WIPException('I think this is obsolete')
        #print('----->source_value_changed', self.oid(), old_value, new_value)
        self._mng._on_value_changed(old_value, new_value)
