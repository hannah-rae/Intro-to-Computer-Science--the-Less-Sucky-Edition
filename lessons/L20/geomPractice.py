from geom import Point
from geom import Rectangle
import math

p1 = Point(7, 11)
p2 = Point(8, 21)

diff_x = p2.x - p1.x
diff_y = p2.y - p1.y
distance = math.sqrt( math.pow(diff_x, 2) + math.pow(diff_y, 2) )

print "Distance between p1 and p2 =", distance

aRectangle = Rectangle(Point(0,3.5), Point(4,3.5), Point(0,0), Point(4,0))
print "Width =", aRectangle.getWidth()
print "Height =", aRectangle.getHeight()
print "Area =", aRectangle.getArea()