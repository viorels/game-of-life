

def evolve_universe(universe):
    return set()


class World():
    def __init__(self):
        self.cells = {}
    
    def add(self, cell):
        if isinstance(cell, LiveCell):
            self.cells[(cell.x, cell.y)] = cell
            for neighbour in self.get_neighbours(cell):
                if isinstance(neighbour, LiveCell):
                    cell.neighbour(neighbour)
        
    def get_neighbours(self, cell):
        print "get_n %s (%s)" % (cell, type(cell))
        offsets = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        neighbours = []
        for dx, dy in offsets:
            nx = cell.x + dx
            ny = cell.y + dy
            if self.cells.has_key((nx, ny)):
                neighbours.append(self.cells[(nx, ny)])
            else:
                neighbours.append(DeadCell(nx, ny))
        return neighbours

    def next_gen(self):
        new_world = World()
        candidates = self.cells.copy()
        for cell in self.cells.values():
            print "checking cell %s" % cell
            for neighbour in self.get_neighbours(cell):
                candidates[(neighbour.x, neighbour.y)] = neighbour
        for cell in candidates.values():
            print cell
            new_world.add(cell.next_gen())
        return new_world
        
    def __str__(self):
        return ', '.join([str(v) for v in self.cells.values()])
        
class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = 0
        
    def neighbour(self, other):
        self.n += 1
        other.n += 1
        
    def __str__(self):
        return "[%d, %d]" % (self.x, self.y)
        
class LiveCell(Cell):
    def next_gen(self):
        if 2 <= self.n <= 3:
            return Cell(self.x, self.y)
        else:
            return DeadCell(self.x, self.y)
            
class DeadCell(Cell):
    def next_gen(self):
        if self.n == 3:
            return LiveCell(self.x, self.y)
        else:
            return DeadCell(self.x, self.y)

# w = World()
# for x, y in ((1, 1), (1, 2), (1, 3)):
#     w.add(LiveCell(x, y))
# print w
# print w.next_gen()

