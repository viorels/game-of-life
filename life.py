

def evolve_universe(universe):
    return universe


def cell_transition(state, neighbours):
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

