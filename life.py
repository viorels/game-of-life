

def evolve_universe(universe):
    return universe


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
    offsets = ((-1,  1), (0,  1), (1,  1),
               (-1,  0),          (1,  0),
               (-1, -1), (0, -1), (1, -1))
    return [(x + ox, y + oy) for ox, oy in offsets]


def live_neighbours_count(cell, universe):
    """Count the live neighbour cells of the given cell in the given universe"""

    return len(set(all_cell_neighbours(cell)) & universe)
