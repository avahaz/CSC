#hw 7

#1 ch 8 diss question 1

#a
#Definite loops iterate a specified number of times through either a given
#number or finite list. Indefinite loops iterate as long as a condition is
#met- this could be infinite.

#b
#The for loop iterates a variable through a specified sequence. The while loop
#iterates until a condition is no longer met.

#c
#Interactive loops take in input from the user as they run. Sentinel loops
#run until a specifc data entry is given that tells the program to stop.

#d
#Sentinel loops can be combined with end-of-file loops. The sentinel data entry
# is put at the end of the file to tell the program when to stop processing data.





#2
# ***submitted in separate file***


#3 ch 8 diss question 3
#a
def sum1():
    n = int(input("enter how many counting numbers to sum: "))
    total = 0
    x = 1
    while x <= n:
        total = total + x
        x= x + 1
    print("The sum is ", total)
sum1()

#c
def sum2():
    total = 0
    n = float(input("enter a number to add, 999 to quit: "))
    while n != 999:
        total = total + n
        n = float(input("enter a number to add, 999 to quit: "))
    print("the sum is", total)
sum2()



#4 ch 8 prog exer 1
def fib():
    n = int(input("enter the Fibonacci number to compute: "))
    if n <= 0:
        print("Error, enter a positive integer.")
    elif n == 1 or n == 2:
        print("the sequence number is 1")
    else:
        a, b = 1, 1
        for i in range(3, n+1):
            a, b = b, a + b 
        print(f"The sequece number is:",b)
fib()


    
        
        
