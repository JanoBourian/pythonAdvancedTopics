from test_order import WidgetTestCase
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase())
    suite.addTest(WidgetTestCase())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())