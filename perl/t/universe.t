use Test::More tests => 3;

use Universe qw(make_universe live_neighbours_count cell_transition evolve_cell);
use Cell qw(Cell cell);

my $universe = make_universe(
    cell(0, 1),
    cell(0, 2),
    cell(0, 3),
);

my $cell_1_2 = cell(1, 2);

is(live_neighbours_count($cell_1_2, $universe), 3);
is(cell_transition(Cell->DEAD, 3), Cell->LIVE);
is(evolve_cell($cell_1_2, $universe), Cell->LIVE);
