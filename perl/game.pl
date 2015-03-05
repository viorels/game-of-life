#!/usr/bin/perl

use Modern::Perl '2014';
use autodie;

use Set::Object qw(set);
use Cell qw(Cell cell);

my $universe = set(
	cell(0, 1),
	cell(0, 2),
	cell(0, 3),
);

for my $cell (@$universe) {
	say $cell;
}

=item live_neighbours_count(cell, universe)
Count the live neighbour cells of the given cell in the given universe
=cut

# sub live_neighbours_count {
# 	my ($cell, $universe) = @_;
#     return len(set(cell_neighbours(cell)) & universe)
# }

=item cell_neighbours(cell)
Return coordinates for all neighbours of the given cell, dead or alive
=cut

sub cell_neighbours {
	my $cell = shift;
	my @range = -1 .. 1;
	my @range_product = map { my $dx = $_; map { [$dx, $_] } @range } @range;
	my @neighbour_deltas = grep { !($_->[0] == 0 && $_->[1] == 0) } @range_product;
	my @neighbours = map { cell($cell->x + $_->[0], $cell->y + $_->[1]) } @neighbour_deltas;
	return @neighbours;
}

say cell_neighbours(cell(10,20));
