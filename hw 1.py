#chapter 1 hw

#2
#PE 1
#a
print("Hello, world!")
#b
print("Hello","world!")
#a prints the ful phrase "hello, world" while b print "hello" then "world"

#c
print(3)
#d
print(3.0)
#c print the number 3 and d prints the decimal 3.0

#e
print(2+3)
#f
print(2.0+3.0)
#g
print("2"+"3")
#e prints the sum of 2 and 3, f prints the sum of the decimals 2.0 and 3.0 and a decimal, and g prints the number 2 with the number 3

#i
print(2*3)
#j
print(2**3)
#i print the product of 2 times three and j prints the product of 2 to the third power

#k
print(7/3)
print(2//3)
#k prints the the quotient of 7 divided by 3 and the second prints the floor quotient (whole number quotient) of 2 divided by 3



#3
#PE 5
#File: chaos.py
#A simple program illustrating chaotic behavior.
def main():
    print("This program illustrates a chaotic function")
    n=eval(input("How many numbers should I print?"))
    x=eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x=3.9*x*(1-x)
        print(x)

main()



#4
#PE 10
def convert():
    print("This program will convert kilometers to miles.")
    x=eval(input("How many kilometers?: "))
    m=0.62*x
    print(m,"miles")
    
convert()



#5
#5 from think like a comp chapter
def earning():
    t=int(input("Enter number of years: "))
    p=10000
    r=.08
    n=12
    a=p*(1+(r/n))**(n*t)
    print("$",a)

earning()

    
