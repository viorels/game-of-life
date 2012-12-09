

def evolve_universe(universe):
    return universe


def cell_transition(state, neighbours):
    """Implements game rules and returns the new state of the cell based on
    previous conditons passed as arguments"""

    if state is True:               # previous state is live
        if neighbours < 2:          # underpopulation
            return False
        elif 2 <= neighbours <= 3:  # healthy
            return True
        else:                       # overpopulation
            return False
    else:                           # previous state is dead
        if neighbours == 3:         # reproduction
            return True
        else:                       # no reproduction
            return False


def all_cell_neighbours(cell):
    """Return coordinates for all neighbours of the given cell, dead or alive"""

    x, y = cell
    offsets = ((-1,  1), (0,  1), (1,  1),
               (-1,  0),          (1,  0),
               (-1, -1), (0, -1), (1, -1))
    return [(x + ox, y + oy) for ox, oy in offsets]


def cell_neighbours_count(cell, universe):
    """Count the live neighbour cells of the given cell in the given universe"""

    return len(set(all_cell_neighbours(cell)) & universe)
