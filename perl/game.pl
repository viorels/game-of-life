#!/usr/bin/perl

use Modern::Perl '2014';

use Universe qw(make_universe live_neighbours_count cell_transition evolve_cell);
use Cell qw(cell);

my $universe = make_universe(
    cell(0, 1),
    cell(0, 2),
    cell(0, 3),
);
