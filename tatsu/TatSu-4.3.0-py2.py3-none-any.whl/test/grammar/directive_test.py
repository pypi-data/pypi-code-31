# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

import tatsu
from tatsu.util import trim
from tatsu.codegen import codegen


EXEC = str('exec')


class DirectiveTests(unittest.TestCase):

    def test_whitespace_directive(self):
        grammar = '''
            @@whitespace :: /[\t ]+/

            test = "test" $;
        '''
        model = tatsu.compile(grammar, "test")
        code = codegen(model)
        compile('test.py', code, EXEC)

    def test_eol_comments_re_directive(self):
        grammar = '''
            @@eol_comments :: /#.*?$/

            test = "test" $;
        '''
        model = tatsu.compile(grammar, "test")
        code = codegen(model)
        compile(code, 'test.py', EXEC)

    def test_left_recursion_directive(self):
        grammar = '''
            @@left_recursion :: False

            test = "test" $;
        '''
        model = tatsu.compile(grammar, "test")
        self.assertFalse(model.directives.get('left_recursion'))
        self.assertFalse(model.left_recursion)

        code = codegen(model)
        compile('test.py', code, EXEC)

    def test_whitespace_no_newlines(self):
        grammar = """
            @@whitespace :: /[\t ]+/
            # this is just a token with any character but space and newline
            # it should finish before it capture space or newline character
            token = /[^ \n]+/;
            # expect whitespace to capture spaces between tokens, but newline should be captured afterwards
            token2 = {token}* /\n/;
            # document is just list of this strings of tokens
            document = {@+:token2}* $;
        """
        text = trim("""\
            a b
            c d
            e f
        """)

        expected = [
            [
                [
                    "a",
                    "b"
                ],
                "\n"
            ],
            [
                [
                    "c",
                    "d"
                ],
                "\n"
            ],
            [
                [
                    "e",
                    "f"
                ],
                "\n"
            ]
        ]

        model = tatsu.compile(grammar, "document")
        ast = model.parse(text, start='document')
        self.assertEqual(expected, ast)

    def test_grammar_directive(self):
        grammar = '''
            @@grammar :: Test

            start = test $;
            test = "test";
        '''
        model = tatsu.compile(grammar=grammar)
        self.assertEqual('Test', model.directives.get('grammar'))
        self.assertEqual('Test', model.name)

        code = codegen(model)
        module = compile(code, 'test.py', EXEC)

        assert 'TestParser' in module.co_names

    def test_parseinfo_directive(self):
        grammar = '''
            @@parseinfo
            @@parseinfo :: True

            test = value:"test" $;
        '''
        model = tatsu.compile(grammar, "test")
        ast = model.parse("test")
        self.assertIsNotNone(ast.parseinfo)

        code = codegen(model)
        self.assertTrue('parseinfo=True' in code)
        compile(code, 'test.py', EXEC)

        grammar = '''
            @@parseinfo :: False

            test = value:"test" $;
        '''
        model = tatsu.compile(grammar, "test")
        ast = model.parse("test")
        self.assertIsNone(ast.parseinfo)

        code = codegen(model)
        self.assertTrue('parseinfo=False' in code)
        compile(code, 'test.py', EXEC)
