from unittest import TestCase

from hestia.memoize_decorators import memoize


class MemoizeMethodTest(TestCase):
    """
    A test case for the `memoize` decorator.
    """
    def setUp(self):
        class TestClass(object):
            def __init__(self):
                self.test0_execution_count = 0
                self.test1_execution_count = 0
                self.test2_execution_count = 0

            @memoize
            def test0(self):
                self.test0_execution_count += 1
                return 42

            @memoize
            def test1(self, a):
                self.test1_execution_count += 1
                return a

            @memoize
            def test2(self, a, b):
                self.test2_execution_count += 1
                return a ** b

        self.obj1 = TestClass()
        self.obj2 = TestClass()

    def test_function_is_executed_on_first_request(self):
        result0 = self.obj1.test0()
        result1 = self.obj1.test1(1)
        result2 = self.obj1.test2(2, 3)
        self.assertEqual(42, result0)
        self.assertEqual(1, result1)
        self.assertEqual(8, result2)
        self.assertEqual(1, self.obj1.test0_execution_count)
        self.assertEqual(1, self.obj1.test1_execution_count)
        self.assertEqual(1, self.obj1.test2_execution_count)

    def test_results_are_cached(self):
        self.obj1.test0()
        self.obj1.test1(1)
        self.obj1.test2(2, 3)
        result0 = self.obj1.test0()
        result1 = self.obj1.test1(1)
        result2 = self.obj1.test2(2, 3)
        self.assertEqual(42, result0)
        self.assertEqual(1, result1)
        self.assertEqual(8, result2)
        self.assertEqual(1, self.obj1.test0_execution_count)
        self.assertEqual(1, self.obj1.test1_execution_count)
        self.assertEqual(1, self.obj1.test2_execution_count)

    def test_function_is_executed_for_new_parameter_combination(self):
        self.obj1.test2(2, 3)
        result = self.obj1.test2(3, 2)
        self.assertEqual(9, result)
        self.assertEqual(2, self.obj1.test2_execution_count)

    def test_result_is_not_cached_across_instances(self):
        self.obj1.test2(2, 3)
        self.assertEqual(0, self.obj2.test2_execution_count)
        self.obj2.test2(2, 3)
        self.assertEqual(1, self.obj2.test2_execution_count)
