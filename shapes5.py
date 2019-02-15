from graphics import *

winX = int(900)
winY = int(900)

window = GraphWin("Window", winX, winY)
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

rhombus = Polygon(Point(winX / 2 + 50, winY / 2 + 150), Point(winX / 2 + 100, winY / 2 + 50), Point(winX / 2 + 50, winY / 2 - 50), Point(winX / 2, winY / 2 + 50))
rhombus.setFill(color_rgb(150, 150, 0))
rhombus.draw(window)

window.getMouse()
window.close()
