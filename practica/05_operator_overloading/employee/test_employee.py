#!/usr/bin/env python

from employee import Employee
import logging
import unittest

logging.basicConfig(level=logging.INFO)


class TestEmployee(unittest.TestCase):
    def testGetFullName(self):
        hansen = list()
        employee1 = Employee("Hans", "O", 5000)
        employee2 = Employee("Hans", "W", 4800, 1200)
        logging.info(self.assertEqual(employee1.getFullName(), "Hans O"))
        self.assertEqual(employee2.getFullName(), "Hans W")


if __name__ == "__main__":
    unittest.main()
