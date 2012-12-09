import unittest

from life import evolve_universe, cell_transition


class GameRulesTest(unittest.TestCase):
    def setUp(self):
        self.live_cell_state = True
        self.dead_cell_state = False

    def test_rule_1_underpopulation(self):
        for neighbours in (0, 1):
            new_state = cell_transition(state=self.live_cell_state,
                                        neighbours=neighbours)
            self.assertEqual(new_state, self.dead_cell_state)

    def test_rule_2_healthy(self):
        for neighbours in (2, 3):
            new_state = cell_transition(state=self.live_cell_state,
                                        neighbours=neighbours)
            self.assertEqual(new_state, self.live_cell_state)

    def test_rule_3_overpopulation(self):
        for neighbours in (4, 5, 6, 7, 8):
            new_state = cell_transition(state=self.live_cell_state,
                                        neighbours=neighbours)
            self.assertEqual(new_state, self.dead_cell_state)

    def test_rule_4_reproduction(self):
        new_state = cell_transition(state=self.dead_cell_state,
                                    neighbours=3)
        self.assertEqual(new_state, self.live_cell_state)

    def test_rule_4_no_reproduction(self):
        for neighbours in (0, 1, 2, 4, 5, 6, 7, 8):
            new_state = cell_transition(state=self.dead_cell_state,
                                        neighbours=neighbours)
            self.assertEqual(new_state, self.dead_cell_state)


class UniverseTest(unittest.TestCase):
    def setUp(self):
        self.empty_universe = set()
        self.block_universe = set([(0, 0), (0, 1), (1, 0), (1, 1)])
        self.live_cell_state = True
        self.dead_cell_state = False

    def test_empty_universe_evolves_into_empty_universe(self):
        new_universe = evolve_universe(self.empty_universe)
        self.assertEqual(new_universe, self.empty_universe)

    def test_universe_with_block_evolves_into_block(self):
        new_universe = evolve_universe(self.block_universe)
        self.assertEqual(new_universe, self. block_universe)


if __name__ == '__main__':
    unittest.main()
