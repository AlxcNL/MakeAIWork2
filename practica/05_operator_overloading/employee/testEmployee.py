#!/usr/bin/env python

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    employee1 = Employee(firstName="Marc", lastName="R", pay=6000, bonus=500)
    employee2 = Employee(firstName="Anton", lastName="D", pay=4500, bonus=1000)

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.employee1.fullname, "Marc R")
        self.assertEqual(self.employee2.fullname, "Anton D")

    def test_annualSalary(self):
        print("test_apply_raise")
        self.employee1.annualSalary
        self.employee2.annualSalary


if __name__ == "__main__":
    unittest.main()
