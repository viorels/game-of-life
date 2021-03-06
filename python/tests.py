import unittest

from life import evolve_universe, evolve_cell, cell_transition, live_neighbours_count


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
        self.live_cell_state = True
        self.dead_cell_state = False
        self.empty_universe = set()
        self.block_universe = set([(0, 0), (0, 1), (1, 0), (1, 1)])
        self.horizontal_blinker_universe = set([(0, 1), (1, 1), (2, 1)])
        self.vertical_blinker_universe = set([(1, 0), (1, 1), (1, 2)])

    def test_empty_universe_cell_has_0_neighbours(self):
        a_cell = (0, 0)
        count = live_neighbours_count(a_cell, self.empty_universe)
        self.assertEqual(count, 0)

    def test_cell_has_1_neighbours(self):
        cell_with_1_neighbour = (3, 0)
        count = live_neighbours_count(cell_with_1_neighbour, self.horizontal_blinker_universe)
        self.assertEqual(count, 1)

    def test_cell_has_2_neighbours(self):
        cell_with_2_neighbours = (2, 0)
        count = live_neighbours_count(cell_with_2_neighbours, self.horizontal_blinker_universe)
        self.assertEqual(count, 2)

    def test_cell_has_3_neighbours(self):
        cell_with_3_neighbours = (1, 0)
        count = live_neighbours_count(cell_with_3_neighbours, self.horizontal_blinker_universe)
        self.assertEqual(count, 3)

    def test_cell_does_not_reproduce_in_empty_universe(self):
        a_cell = (0, 0)
        next_state = evolve_cell(a_cell, self.empty_universe)
        self.assertEqual(next_state, self.dead_cell_state)

    def test_cell_dies_in_lonely_universe(self):
        cell = (0, 0)
        lonely_universe = set([cell])
        next_state = evolve_cell(cell, lonely_universe)
        self.assertEqual(next_state, self.dead_cell_state)

    def test_cell_survives_in_horizontal_blinker_universe(self):
        cell = (1, 1)
        next_state = evolve_cell(cell, self.horizontal_blinker_universe)
        self.assertEqual(next_state, self.live_cell_state)

    def test_cell_reproduces_in_horizontal_blinker_universe(self):
        cell = (1, 0)
        next_state = evolve_cell(cell, self.horizontal_blinker_universe)
        self.assertEqual(next_state, self.live_cell_state)

    def test_cell_does_not_reproduces_in_horizontal_blinker_universe(self):
        cell = (0, 0)
        next_state = evolve_cell(cell, self.horizontal_blinker_universe)
        self.assertEqual(next_state, self.dead_cell_state)

    def test_empty_universe_evolves_into_empty_universe(self):
        new_universe = evolve_universe(self.empty_universe)
        self.assertEqual(new_universe, self.empty_universe)

    def test_universe_with_block_evolves_into_block(self):
        new_universe = evolve_universe(self.block_universe)
        self.assertEqual(new_universe, self. block_universe)

    def test_universe_with_horizontal_blinker_evolves_into_vertical_blinker(self):
        new_universe = evolve_universe(self.horizontal_blinker_universe)
        self.assertEqual(new_universe, self.vertical_blinker_universe)

    def test_universe_with_vertical_blinker_evolves_into_horizontal_blinker(self):
        new_universe = evolve_universe(self.vertical_blinker_universe)
        self.assertEqual(new_universe, self.horizontal_blinker_universe)


if __name__ == '__main__':
    unittest.main()
