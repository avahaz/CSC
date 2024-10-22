#hw 2


#1 ch2 diss prob 4
#a
for i in range (5):
    print(i*i)
print()
#output: "0" "1" "4" "9" "16" each in their own line

#b
for d in [3,1,4,1,5]:
    print(d,end=" ")
print()
print()
#output: "3 1 4 1 5" all on the same line, like as seen here

#c
for i in range(4):
    print("Hello")
print()
#output: "Hello" printed on 4 separate lines

#d
for i in range(5):
        print(i,2**i)
print()
#output: "0 1" on one line, then "1 2" on the next, then "2 4" then "3 8" then "4 16" on the 5th line



#2 ch 3 diss prob 1

#a
4.0/10.0 + 3.5 * 2
#result: 7.4

#c
abs(4-20//3)**3
#result: 8

#e
3*10//3+10%3
#result:11



#3 ch 3 diss prob 2

#b
#(n*(n-1))/2

#c
#4*pi*(r**2)



#4 ch 3 diss prob 4

#b
for i in [1,3,5,7,9]:
    print(i, ":", i**3)
print(i)
#output: "1 : 1" on one line, "3 : 27" on the next, then "5 : 125", then "7 : 343", then "9 : 729" on the 5th line, and 9 on the 6th line
print()

#c
x=2
y=10
for j in range(0,y,x):
    print(j,end="")
    print(x+y)
print("done")
#output: 012 on one line, then 212 on the next, then 412, then 612, then 812, then done on the 6th line
print()


#5 ch 3 prog ex 6
def main():
    x1=int(input("enter x1 coordinate: "))
    y1=int(input("enter y1 coordinate: "))
    x2=int(input("enter x2 coordinate: "))
    y2=int(input("enter y2 coordinate: "))
    slope=(y2-y1)/(x2-x1)
    print("the slope is ",slope)
main()
print()

#6 ch 3 prog ex 7
import math
def main():
    x1=int(input("enter x1 coordinate: "))
    y1=int(input("enter y1 coordinate: "))
    x2=int(input("enter x2 coordinate: "))
    y2=int(input("enter y2 coordinate: "))
    dis=math.sqrt((y2-y1)**2 + (x2-x1)**2)
    print("the distance is ",dis)
main()

