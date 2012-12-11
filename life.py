from itertools import chain, product


live_cell = True
dead_cell = False


def evolve_universe(universe):
    """Evolve each cell of the current universe into a new parallel one"""
    return set(cell for cell in universe | dead_neighbours_set(universe)
               if evolve_cell(cell, universe) is live_cell)


def evolve_cell(cell, universe):
    """Return the next state of the cell at the given coordinates"""
    return cell_transition(cell in universe, live_neighbours_count(cell, universe))


def cell_transition(state, neighbours):
    """Implements game rules and returns the new state of the cell based on
    previous conditons passed as arguments"""
    new_state = None
    if state is True:               # previous state is live
        if neighbours < 2:          # underpopulation
            new_state = False
        elif 2 <= neighbours <= 3:  # healthy
            new_state = True
        elif neighbours > 3:        # overpopulation
            new_state = False
    else:                           # previous state is dead
        if neighbours == 3:         # reproduction
            new_state = True
        else:                       # no reproduction
            new_state = False
    return new_state


def all_cell_neighbours(cell):
    """Return coordinates for all neighbours of the given cell, dead or alive"""
    x, y = cell
    relative = [offset for offset in product((-1, 0, 1), repeat=2)
                if offset != (0, 0)]
    return [(x + rx, y + ry) for rx, ry in relative]


def live_neighbours_count(cell, universe):
    """Count the live neighbour cells of the given cell in the given universe"""
    return len(set(all_cell_neighbours(cell)) & universe)


def dead_neighbours_set(universe):
    """Return a set of all dead neighbours of all cells in the universe.
    This is useful to search for reproduction candidates"""
    all_neighbours = set(chain(*(all_cell_neighbours(cell) for cell in universe)))
    all_dead_neighbours = all_neighbours - universe
    return all_dead_neighbours
