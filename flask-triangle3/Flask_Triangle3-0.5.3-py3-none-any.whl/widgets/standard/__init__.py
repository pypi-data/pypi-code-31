# -*- encoding: utf-8 -*-
"""
    flask_triangle.widgets.standard
    -------------------------------

    HTML5's standard widget collection.

    :copyright: (c) 2013 by Morgan Delahaye-Prat.
    :license: BSD, see LICENSE for more details.
"""





from .text import (Input, TextInput)
from .select import Select

__all__ = ['Input', 'TextInput', 'PasswordInput', 'EmailInput', 'Textarea',
           'NumberInput', 'Select']
