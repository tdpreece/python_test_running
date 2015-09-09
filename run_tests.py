#!/usr/bin/env python
import os
import sys
import unittest

from pprint import pprint
from StringIO import StringIO


def load_tests(test_dir):
    pattern = r'*.py'
    loader = unittest.TestLoader()
    tests = loader.discover(
        start_dir=test_dir,
        pattern=pattern
    )
    return tests


def add_to_path(a_dir):
    sys.path.insert(0, a_dir)


def main():
    this_dir = os.path.dirname(__file__)
    test_dir = os.path.join(this_dir, 'test')
    src_dir = os.path.join(this_dir, 'src')
    add_to_path(src_dir)
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    tests = load_tests(test_dir)
    result = runner.run(tests)
    print 'Tests run ', result.testsRun
    print 'Errors ', result.errors
    pprint(result.failures)
    stream.seek(0)
    print 'Test output\n', stream.read()


if __name__ == '__main__':
    main()
