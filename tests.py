import unittest

from life import evolve_universe


class LifeTest(unittest.TestCase):
    def setUp(self):
        self.empty_universe = set()

    def test_empty_universe_evolves_into_empty_universe(self):
        new_universe = evolve_universe(self.empty_universe)
        self.assertEqual(new_universe, self.empty_universe)

if __name__ == '__main__':
    unittest.main()
