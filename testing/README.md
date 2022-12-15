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