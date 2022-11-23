import unittest
import main

class TestPerevorot(unittest.TestCase):
    def test(self):
        self.assertEqual(main.Perevorot('per'), 'vor')

if __name__ == '__main__':
    unittest.main()


class Perevorot:
    pass