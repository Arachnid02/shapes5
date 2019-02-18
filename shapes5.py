#Imports graphics module
from graphics import *

#Sets the max coordinates for the x and y values for the window
winX = int(900)
winY = int(900)

#Creates the window where the shapes will be drawn
window = GraphWin("Window", winX, winY)
#Sets the lower left side of the window to be 0,0 and upper right side
#to be 1000,1000
window.setCoords(0, 0, 1000, 1000)

#Creates a triangle, makes it red, and draws it in the lower left side
#of the window
triangle = Polygon(Point(50, 50), Point(50, 200), Point(200, 50))
triangle.setFill(color_rgb(255, 0, 0))
triangle.draw(window)

#Creates a square, makes it green, and draws it in the upper left side
#of the window
square = Polygon(Point(50, 950), Point(200,950),
                 Point(200, 800), Point(50, 800))
square.setFill(color_rgb(0, 255, 0))
square.draw(window)

#Creates a pentagon, makes it blue, and draws it in the upper right side
#of the window
pentagon = Polygon(Point(875, 950), Point(950, 875),
                   Point(925, 800), Point(825, 800),
                   Point(800, 875))
pentagon.setFill(color_rgb(0, 0, 255))
pentagon.draw(window)

#Creates a heaxagon, makes it black, and draws it in the lower right side
#of the window
hexagon = Polygon(Point( 832.5, 200), Point(917.5, 200),
                  Point(950, 125), Point(917.5, 50),
                  Point(832.5, 50), Point(800, 125))
hexagon.setFill(color_rgb(0, 0, 0))
hexagon.draw(window)

#Creates a rhombus, makes it olive, and draws it in the center of the window
rhombus = Polygon(Point(winX / 2 + 50, winY / 2 + 150),
                  Point(winX / 2 + 100, winY / 2 + 50),
                  Point(winX / 2 + 50, winY / 2 - 50),
                  Point(winX / 2, winY / 2 + 50))
rhombus.setFill(color_rgb(150, 150, 0))
rhombus.draw(window)

#When the window is clicked on, exit the window/program
window.getMouse()
window.close()
