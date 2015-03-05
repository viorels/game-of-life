
package Cell {
	use Moose;
	use Modern::Perl '2014';
	use List::Util qw(pairs pairgrep);
	no warnings qw(experimental::smartmatch);

	use constant { LIVE => 1, DEAD => 0 };

	has 'x', is => 'ro', isa => 'Int';
	has 'y', is => 'ro', isa => 'Int';

	use overload '""' => \&stringify;

	sub stringify {
		my $self = shift;
		return sprintf '(%d,%d)', $self->x, $self->y;
	}

=item neighbours()
Return all neighbour cells of self, dead or alive
=cut

	sub neighbours {
		my $self = shift;
		my @range = -1 .. 1;
		my @range_product = map { my $dx = $_; map { $dx, $_ } @range } @range;
		my @neighbour_deltas = pairgrep { !([$a, $b] ~~ [0, 0]) } @range_product;
		my @neighbours = map { Cell->new(x => $self->x + $_->[0],
									     y => $self->y + $_->[1]) } pairs @neighbour_deltas;
		return @neighbours;
	}
}

sub cell {
	my ($x, $y) = @_;
	return Cell->new(x => $x, y => $y);
}

1;