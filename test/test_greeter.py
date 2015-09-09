import unittest
import greeter


class TestGreeter(unittest.TestCase):
    def test(self):
        self.assertEqual(greeter.greet(), 'hello')
