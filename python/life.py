from itertools import chain, product


live_cell = True
dead_cell = False


def evolve_universe(universe):
    """Evolve each cell of the current universe into a new parallel one"""
    return set(cell for cell in universe | all_dead_neighbours(universe)
               if evolve_cell(cell, universe) is live_cell)


def evolve_cell(cell, universe):
    """Return the next state of the cell at the given coordinates"""
    return cell_transition(cell in universe, live_neighbours_count(cell, universe))


def cell_transition(state, neighbours):
    """Implements game rules and returns the new state of the cell based on
    previous conditons passed as arguments"""
    new_state = None
    if state is live_cell:
        if neighbours < 2:          # underpopulation
            new_state = dead_cell
        elif 2 <= neighbours <= 3:  # healthy
            new_state = live_cell
        elif neighbours > 3:        # overpopulation
            new_state = dead_cell
    elif state is dead_cell:
        if neighbours == 3:         # reproduction
            new_state = live_cell
        else:                       # no reproduction
            new_state = dead_cell
    return new_state


def cell_neighbours(cell):
    """Return coordinates for all neighbours of the given cell, dead or alive"""
    x, y = cell
    relative = [offset for offset in product((-1, 0, 1), repeat=2)
                if offset != (0, 0)]
    return [(x + rx, y + ry) for rx, ry in relative]


def live_neighbours_count(cell, universe):
    """Count the live neighbour cells of the given cell in the given universe"""
    return len(set(cell_neighbours(cell)) & universe)


def all_dead_neighbours(universe):
    """Return a set of all dead neighbours of all cells in the universe.
    This is useful to search for reproduction candidates"""
    all_neighbours = set(chain(*(cell_neighbours(cell) for cell in universe)))
    return all_neighbours - universe
