#hw 3

#1 ch 3 prog ex 13
#sum numbers
def main():
    n=int(input("how many numbers to be summed? "))
    first=0
    for i in range(n):
        x=float(input("what number to add? "))
        first=first+x
    print("the sum is ", first)
main()
print()
print()



#2 ch 3 prog ex 14
#average numbers
def main():
    n=int(input("how many numbers to be averaged? "))
    first=0
    for i in range(n):
        x=float(input("enter number in series "))
        first=first+x
        avg=first/n
    print("the average is ", avg)
main()




#3 ch 4 diss prob 2
import graphics
from graphics import*
win=graphics.GraphWin()
#a
p=Point(130,130)
#This point information is stored in the computer. When assigned a variable
#and drawn in the window, it is a dot in black in the lower right quadrant of the plane

#b
c=Circle(Point(30,40),25)
c.setFill("blue")
c.setOutline("red")
#this circle holds information to be drawn with a center at (30,40) and a radius of 25 pixels. The circle will be filled in blue with a red outline.
#This circle will be in the upper left hand corner of the window.

#c
r=Rectangle(Point(20,20),Point(40,40))
r.setFill(color_rgb(0,255,150))
r.setWidth(3)
#This is a rectangle that would be drawn in the upper left corner of the window.
#the outline is black and thick. the inside of the rectangle is green. it is small and more squareish.

#d
l=Line(Point(100,100), Point(100,200))
l.setOutline("red4")
l.setArrow("first")
#this is a red vertical line with an arrow head at the first point given. this point is in the center of the window. the other end of the arrow in at teh center of the botton axis (x-axis)

#e
Oval(Point(50,50), Point(60,100))
#this is an oval drawn within the box created by the two given points. this oval is thin, vertical, and drawn in a black outline iwth no fill.

#f
shape=Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
shape.setFill("orange")
#this is a polygon that is shaped like an hourglass. it is very small in the upper left had corner. a line is drawn from teh first given poin to teh next given point all the way thorugh the last, which is connected to the first.

#g
t= Text(Point(100,100), "Hello World!")
t.setFace("courier")
t.setSize(16)
t.setStyle("italic")
#this draws the phrase "Hello World! in the courier font in italics at size 16 at the given point, center of the graph.


print()
print()



#4 ch 4 diss prob 3
def main():
    win=GraphWin()
    shape=Circle(Point(50,50),20)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p=win.getMouse()
        c=shape.getCenter()
        dx=p.getX()-c.getX()
        dy=p.getY()-c.getY()
        shape.move(dx,dy)
    win.close()
# this program draws red filled and outlines circle in the upper left corner of the graph. the user can then click the graph anywhere 10 times, moving the circle's center at the clicked point. after the 10th click the window closes.



#5 ch 4 prog ex 2
def archery():
    win=GraphWin()
    c1=Circle(Point(100,100),100)
    c1.setFill("white")
    c2=Circle(Point(100,100),80)
    c2.setFill("black")
    c3=Circle(Point(100,100),60)
    c3.setFill("blue")
    c4=Circle(Point(100,100),40)
    c4.setFill("red")
    c5=Circle(Point(100,100),20)
    c5.setFill("yellow")
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    c4.draw(win)
    c5.draw(win)
archery()



#6 ch 4 prog ex 3
def face():
    win=GraphWin()
    eye1=Circle(Point(50,50),20)
    eye2=Circle(Point(150,50),20)
    mouth=Line(Point(50,150), Point(150,150))
    eye1.draw(win)
    eye2.draw(win)
    mouth.draw(win)
face()



#7 ch 4 prog ex 8
def main():
    import math
    win=GraphWin()
    print("Click the graph twice where you want the endpoints")
    p1=win.getMouse()
    p2=win.getMouse()
    p1.draw(win)
    p2.draw(win)
    l=Line(p1,p2)
    l.draw(win)
    x1=p1.getX()
    y1=p1.getY()
    x2=p2.getX()
    y2=p2.getY()
    dx=x2-x1
    dy=y2-y1
    midpt=Point(dx,dy)
    midpt.setFill("cyan")
    midpt.draw(win)
    slope=dy/dx
    length=math.sqrt((dx**2)+(dy**2))
    print("the slope is ",slope, "the length is ", length)
main()




