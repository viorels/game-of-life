package Cell {
	use Moose;

	use constant { LIVE => 1, DEAD => 0 };

	has 'x', is => 'ro', isa => 'Int';
	has 'y', is => 'ro', isa => 'Int';

	use overload
		'""' => \&stringify,
		'cmp' => \&compare;

	sub stringify {
		my $self = shift;
		return sprintf '(%d,%d)', $self->x, $self->y;
	}

	sub compare {
		my ($self, $other) = @_;
		return $self->x <=> $other->x || $self->y <=> $other->y;
	}
}

sub cell {
	my ($x, $y) = @_;
	return Cell->new(x => $x, y => $y);
}

1;