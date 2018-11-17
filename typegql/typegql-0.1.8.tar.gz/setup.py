# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['typegql', 'typegql.core']

package_data = \
{'': ['*']}

install_requires = \
['graphql-core-next>=1.0,<2.0', 'uvloop>=0.11.2,<0.12.0']

setup_kwargs = {
    'name': 'typegql',
    'version': '0.1.8',
    'description': 'A Python GraphQL library that makes use of type hinting and concurrency support with the new async/await syntax.',
    'long_description': ".. role:: python(code)\n    :language: python\n\nTypeGQL\n========\n\nA Python `GraphQL <https://graphql.org>`_ library that makes use of type hinting and concurrency support with the new async/await syntax.\n\n\nDISCLAIMER\n==========\n\nThis library is still in it's infancy, so **use with caution** and feel free to contribute.\n\n\nInstallation\n============\n\n.. code-block:: python\n\n    pip install typegql\n\n\nUsage\n=====\n\nThe following demonstrates how to use **typegql** for implementing a *GraphQL API* for a library of books.\nThe example can be found in *typegql/core/examples* and you can run it with Sanic by executing ``python <path_to_example>/server.py``\n\nDefine your query\n-----------------\n\n.. code-block:: python\n\n    from typing import List\n    from typegql.core.graph import Graph, Connection\n    from typegql.examples.library.types import Author, Category\n    from typegql.examples.library.types import Book\n    from typegql.examples.library import db\n\n    class Query(Graph):\n        books: List[Book]\n        authors: List[Author]\n        categories: List[Category]\n\n        books_connection: Connection[Book]\n\n        async def resolve_authors(self, info, **kwargs):\n            return db.get('authors')\n\n        async def resolve_books(self, info, **kwargs):\n            return db.get('books')\n\n        async def resolve_categories(self, info, **kwargs):\n            return db.get('categories')\n\n       async def resolve_books_connection(self, info, **kwargs):\n            data = db.get('books')\n            return {\n                'edges': [{\n                    'node': node\n                } for node in data]}\n\n\nDefine your types\n-----------------\n\n.. code-block:: python\n\n    from datetime import datetime\n    from decimal import Decimal\n    from enum import Enum\n    from typing import List\n\n    from typegql.core.graph import Graph, ID, GraphInfo\n    from examples.library import db\n\n\n    class Gender(Enum):\n        MALE = 'male'\n        FEMALE = 'female'\n\n\n    class GeoLocation:\n        latitude: Decimal\n        longitude: Decimal\n\n        def __init__(self, latitude, longitude):\n            self.latitude = latitude\n            self.longitude = longitude\n\n\n    class Author(Graph):\n        id: ID\n        name: str\n        gender: Gender\n        geo: GeoLocation\n\n\n    class Category(Graph):\n        id: ID\n        name: str\n\n\n    class Book(Graph):\n        id: ID\n        author_id: ID\n        title: str\n        author: Author\n        categories: List[Category]\n        published: datetime\n        tags: List[str]\n\n        class Meta:\n            description = 'Just a book'\n            id = GraphInfo(required=True, description='Book unique identifier')\n\n        def __init__(self, **kwargs):\n            super().__init__(**kwargs)\n            self.published = datetime.strptime(self.published, '%Y-%m-%d %H:%M:%S')\n\n        async def resolve_author(self, info):\n            data = filter(lambda x: x['id'] == self.author_id, db.get('authors'))\n            data = next(data)\n            author = Author(**data)\n            author.gender = Gender[author.gender.upper()].value\n            if 'geo' in data:\n                author.geo = GeoLocation(**data.get('geo'))\n            return author\n\n        async def resolve_categories(self, selections, name=None):\n            data = filter(lambda x: x['id'] in self.categories, db.get('categories'))\n            for d in data:  # showcasing async generator\n                yield Category(**d)\n\n        def resolve_tags(self, selections):\n            return ['testing', 'purpose']\n\n\n\nRun your query\n--------------\n\n.. code-block:: python\n\n    from typegql.core.schema import Schema\n    from examples.library.query import Query\n\n\n    schema = Schema(Query)\n    query = '''\n    query BooksConnection {\n      books_connection {\n        edges {\n          node {\n            id\n            title\n            published\n            author {\n              id\n              name\n            }\n          }\n        }\n      }\n    }\n    '''\n\n    async def run():\n        result = await schema.run(query)\n\n\nChange Log\n==========\n\n    - added `graphql-core-next <https://github.com/graphql-python/graphql-core-next>`_ as a baseline for all GraphQL operations\n",
    'author': 'Ciprian Tarta',
    'author_email': 'ciprian@cipriantarta.ro',
    'url': 'https://github.com/cipriantarta/typegql',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
