from graphics import *

window = GraphWin("Window", 1000, 1000)
window.setCoords(0, 0, 1000, 1000)

triangle = Polygon(Point(50, 50), Point(50, 200), Point(200, 50))
triangle.setFill(color_rgb(255, 0, 0))
triangle.draw(window)

square = Polygon(Point(50, 950), Point(200,950), Point(200, 800), Point(50, 800))
square.setFill(color_rgb(0, 255, 0))
square.draw(window)

pentagon = Polygon(Point(875, 950), Point(950, 875), Point(925, 800), Point(825, 800), Point(800, 875))
pentagon.setFill(color_rgb(0, 0, 255))
pentagon.draw(window)

hexagon = Polygon(Point( 832.5, 200), Point(917.5, 200), Point(950, 125), Point(917.5, 50), Point(832.5, 50), Point(800, 125))
hexagon.setFill(color_rgb(0, 0, 0))
hexagon.draw(window)

window.getMouse()
window.close()
