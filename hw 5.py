#hw 5

#1 ch 6 prog ex 1
def line():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    
def OM(animal,sound):
    line()
    print("And on that farm he had a", animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a", sound + ",", sound + " here and a", sound + ",", sound + " there.")
    print("Here a", sound + ", there a", sound + ", everywhere a", sound + ",", sound + ".")
    line()
    print()
    
def cow():
    OM("cow","moo")
def sheep():
    OM("sheep","baa")
def horse():
    OM("horse","neigh")
def duck():
    OM("duck","quack")
def pig():
    OM("pig","oink")

def main():
    cow()
    sheep()
    horse()
    duck()
    pig()
main()




#2 ch 3 prog ex 14 + extra
def average(count):
    numbers:[]
    first=0
    for i in range(count):
        x=float(input("enter number in series "))
        first=first+x
        avg=first/count
    return avg

def main():
    count=int(input("how many numbers to average? "))
    avg = average(count)
    print("the average is ", avg)
main()




#3 ch 4 prog ex 8 + extra
from graphics import*
import math

def slo(dx,dy):
    slope = dy/dx
    return slope
def dis(dx,dy):
    distance=math.sqrt((dx**2)+(dy**2))
    return distance
def main():
    win=GraphWin("Line",200,200)
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
    midpt = Point((x1 + x2) / 2, (y1 + y2) / 2)
    midpt.setFill("cyan")
    midpt.draw(win)
    slope=slo(dx,dy)
    distance=dis(dx,dy)
    print("the slope is ", slope, "the length is ", distance)
main()




#4 ch 6 prog ex 12
def adding(nums):
    return sum(nums)
def main():
    numblist=[1,2,3,4,5]
    total = adding(numblist)
    print(total)
main()




#5
def get_some_strings(n):
    storage=[]
    for i in range(n):
        user_input=(input("enter string:"))
        storage.append(user_input)
    return storage
def main():
    numb= int(input("enter number of strings: "))
    strings= get_some_strings(numb)
    print("You entered these strings: ")
    for i in strings:
        print(i)
main()
    
























