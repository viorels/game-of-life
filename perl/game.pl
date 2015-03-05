#!/usr/bin/perl

use Modern::Perl '2014';
use autodie;
no warnings qw(experimental::smartmatch);

use List::Util qw(pairs pairgrep);
use Cell qw(Cell cell);

sub make_universe {
	my %universe = map { $_ => $_ } @_;
	return \%universe;
}

=item cell_neighbours(cell)
Return all neighbour cells of the given cell, dead or alive
=cut

sub cell_neighbours {
	my $cell = shift;
	my @range = -1 .. 1;
	my @range_product = map { my $dx = $_; map { $dx, $_ } @range } @range;
	my @neighbour_deltas = pairgrep { [$a, $b] !~~ [0, 0] } @range_product;
	my @neighbours = map { cell($cell->x + $_->[0], $cell->y + $_->[1]) } pairs @neighbour_deltas;
	return @neighbours;
}

=item live_neighbours_count
Count the live neighbour cells of the given cell in the given universe
=cut

sub live_neighbours_count {
	my ($cell, $universe) = @_;
    return scalar grep { exists $universe->{$_} } cell_neighbours($cell);
}

=item cell_transition(state, neighbours)
Implements game rules and returns the new state of the cell based on previous
conditons passed as arguments
=cut

sub cell_transition {
	my ($state, $neighbours) = @_;
    my $new_state;
    if ($state ~~ Cell->LIVE) {
        if ($neighbours ~~ [2, 3]) {	# healthy
            $new_state = Cell->LIVE;
        }
        else {        					# underpopulation/overpopulation
            $new_state = Cell->DEAD;
        }
    }
    elsif ($state ~~ Cell->DEAD) {
        if ($neighbours == 3) {      	# reproduction
            $new_state = Cell->LIVE;
        }
        else {                      	# no reproduction
            $new_state = Cell->DEAD;
        }
    }
    return $new_state;
}

=item evolve_cell(cell, universe)
Return the next state of the cell at the given coordinates
=cut

sub evolve_cell {
	my ($cell, $universe) = @_;
    return cell_transition(exists $universe->{$cell}, live_neighbours_count($cell, $universe));
}

my $universe = make_universe(
	cell(0, 1),
	cell(0, 2),
	cell(0, 3),
);

say cell_neighbours(cell(0, 0));
say live_neighbours_count(cell(1, 2), $universe);
say cell_transition(Cell->DEAD, 3);
say evolve_cell(cell(1, 2), $universe);
