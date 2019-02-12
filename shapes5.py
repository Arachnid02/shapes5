from graphics import *

window = GraphWin("Window", 1000, 1000)
window.setCoords(0, 0, 1000, 1000)

triangle = Polygon(Point(50, 50), Point(50, 200), Point(200, 50))
triangle.setFill(color_rgb(255, 0, 0))
triangle.draw(window)

window.getMouse()
window.close()
