from rearragne import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase="suresh,rathod"
        expected="rathod suresh"
        self.assertEqual(rearrange_name(testcase),expected)
unittest.main()