from graphics import circle,rectangle
from graphics.dgraphics import cuboid,sphere
r=int(input("enter the radius"))
circle.areac(r)
circle.peric(r)
l=int(input("enter the length of the rectangle"))
b=int(input("enter the breadth of the rectangle"))
rectangle.rectarea(l,b)
rectangle.rectperi(l,b)
l=int(input("enter the length of the cuboid"))
b=int(input("enter the breadth of the cuboid"))
h=int(input("enter the height of the cuboid"))
cuboid.cuboidarea(l,b,h)
cuboid.cuboidperi(l,b,h)
r=int(input("enter the radius"))
sphere.spherearea(r)
sphere.sphereperi(r)


