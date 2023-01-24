import unittest
from script import do_stuff
# python3 -m unittest -v


class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to test a function")

    def test_do_stuff(self):
        '''
        verify is a number
        '''
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'nnifenin'
        result = do_stuff(test_param)
        self.assertEqual(isinstance(result, ValueError), True)
        self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print("cleaning up")


if __name__ == '__main__':
    unittest.main()
