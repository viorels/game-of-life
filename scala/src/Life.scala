case class Cell(val x: Int, val y: Int)

class Universe(val liveCells: Set[Cell]) {
  def cellNeighbours(cell: Cell) =
    for (dx <- -1 to 1; dy <- -1 to 1 if (dx, dy) != (0, 0))
      yield Cell(cell.x + dx, cell.y + dy)
  
  def cellTransition(alive: Boolean , neighbours: Int) =
    (alive && 2 <= neighbours && neighbours <= 3) || (!alive && neighbours == 3)
  
  def evolveUniverse = new Universe(liveCells)
}