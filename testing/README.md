# Testing

Testing is a complex topic because testing has a several ways to do it. Testing starts with a docstring, pydoc, doctest, unittest and more complex stuff like pytest, selenium and other more. In this documentation the way to attack these topics will be to start with the most basic: docstring, and after that we can advance to pydoc/doctest and finally unittest.

After Unittest the next steps is take a course of read a lot of documentation about advanced topics like pytest, automated tests or integration test, in a particular case we need to learn about Flask test (or other framework).

## Doctest

We have several ways to generate documentation 

```cmd
python file.py 
python file.py -v
python -m doctest -v file.py
```

For example, we can generate documentation inside the each function like __doctest/file.py__ 

and also we can work with a text file like __file.txt__ and __file\_doctest.py__

## Unittest

We have severals concepts to learn before to start our testing process:

- test fixture: Represents the preparation needed to perform one or more tests, and any associated cleanup actions.
- test case: Is the individual unit of testing. It checks for a specific responses to a particular set of inputs.
- test suite: Is a collection of test cases, test suites or both. It is used to aggregate tests that should be executed together.
- test runner: Is a component which orchestrates the execution of tests and provides the outcome to the user.

We can run test with the next commands:

```cmd
python test.py -v
ptyhon -m unittest -v test_module
ptyhon -m unittest -v test_module/test.py
python -m unittest
python -m unittest -h
```

## About the Test Discovery

In order to be compatible with test discovery, all of the test files must be modules or packages importable from the top-level directory of the project. 

```cmd
cd project_directory
python -m unittest discover
```

We have three different parameters: 
* -v, --verbose 
* -s, --start-directory Directory to start discovery (. default)
* -p, --pattern Patterno to match test files (test*.py default)
* -t, --top-level-directory directory Top level directory of project (default to starts directory)

```cmd 
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"
```

## Organizing Test Code

- setUp(): This functions help us to write once the general information in a TestCase, help us to write information that will be used in the future (in other functions inside our testcase)
- tearDown(): will be run whether the test method succeeded or not.

## Skipping test and expected failures

```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass

class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```

The basic skips decorators are:

- @unittest.skip(reason)
- @unittest.skipIf(condition, reason)
- @unittest.skipUnless(condition, reason)
- @unittest.expectedFailure
- @unittest.SkipTest(reason)