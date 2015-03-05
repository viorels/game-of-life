use Test::More tests => 6;

use Cell qw(cell);

$c = cell(1, 2);

ok(defined $c);
ok($c->isa('Cell'));
is($c->x, 1);
is($c->y, 2);
is("$c", "(1,2)");
is_deeply([$c->neighbours()], [qw[(0,1) (0,2) (0,3) (1,1) (1,3) (2,1) (2,2) (2,3)]]);
