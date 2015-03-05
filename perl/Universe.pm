package Universe;

use Exporter 'import';
our @EXPORT_OK = qw(make_universe live_neighbours_count cell_transition evolve_cell);

no warnings qw(experimental::smartmatch);

sub make_universe {
	my %universe = map { $_ => $_ } @_;
	return \%universe;
}

=item live_neighbours_count
Count the live neighbour cells of the given cell in the given universe
=cut

sub live_neighbours_count {
	my ($cell, $universe) = @_;
    return scalar grep { exists $universe->{$_} } $cell->neighbours();
}

=item cell_transition(state, neighbours)
Implements game rules and returns the new state of the cell based on previous
conditons passed as arguments
=cut

sub cell_transition {
	my ($state, $neighbours) = @_;
    my $new_state;
    if ($state == Cell->LIVE) {
        if ($neighbours ~~ [2, 3]) {	# healthy
            $new_state = Cell->LIVE;
        }
        else {        					# underpopulation/overpopulation
            $new_state = Cell->DEAD;
        }
    }
    elsif ($state == Cell->DEAD) {
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

1;