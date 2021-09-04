"""Tests for type checking test code."""

from pytype.tests import test_base


class AssertionTest(test_base.BaseTest):
  """Tests for test assertions."""

  def test_assert_not_none(self):
    self.Check("""
      import unittest
      from typing import Optional
      def foo():
        return '10' if __random__ else None
      class FooTest(unittest.TestCase):
        def test_foo(self):
          x = foo()
          assert_type(x, Optional[str])
          self.assertIsNotNone(x)
          assert_type(x, str)
    """)

  def test_assert_isinstance(self):
    self.Check("""
      import unittest
      from typing import Union
      def foo():
        return '10' if __random__ else 10
      class FooTest(unittest.TestCase):
        def test_foo(self):
          x = foo()
          assert_type(x, Union[int, str])
          self.assertIsInstance(x, str)
          assert_type(x, str)
    """)


if __name__ == "__main__":
  test_base.main()