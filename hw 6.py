#hw 6

#1 ch 7 diss prob 2
#Both try/except and ordinary decision structures run through various outcomes to avoid errors or the program crashing on the user.
#Try/except structure look for specific Python reported error types to fix. Other structures look for possible errors or just inputs from the user to evaluate.



#2 ch 7 prog exer 3

def main():
    n=int(input("enter score 0-5: "))
    if n==5:
        print("A")
    elif n==4:
        print("B")
    elif n==3:
        print("C")
    elif n==2:
        print("D")
    elif n==1:
        print("F")
    elif n==0:
        print("F")
    else:
        print("not viable score")
main()




#3 ch 7 prog exer 7
def wage():
    sh=int(input("enter starting hour (24-hr format): "))
    sm=int(input("enter starting minute (24-hr format): "))
    eh=int(input("enter ending hour (24-hr format): "))
    em=int(input("enter ending minute (24-hr format): "))
    if sh > eh or (sh==eh and sm > em):
        print("Error: End time cannot be before start time")
        return
    if sh < 21 and eh < 21:
        timehhr=float((eh-sh)*2.5)
        timehmin=float(((60-sm)/60)*2.5) if sm != 0 else 0
        timehmin2=float((em/60)*2.5)
        hmintotal=timehmin+timehmin2
        finalhw=(float(timehhr+hmintotal))
        bill=round(finalhw,2)
        print("The total bill is $",bill)
        return
    elif sh < 21 and eh >= 21:
        hwh=(21-sh-1)*2.5
        hwm=((60-sm)/60)*2.5 if sm != 0 else 0
        hwt=float(hwh+hwm)
        bill1=round(hwt,2)
        lwh=(eh-21)*1.75
        lwm=(em/60)*1.75
        lwt=float(lwh+lwm)
        bill2=round(lwt,2)
        bill=round(bill1+bill2,2)
        print("The total bill is $",bill)
        return
    elif sh >= 21 and eh >= 21:
        timelhr=float((eh-sh)*1.75)
        timelmin=float(((60-sm)/60)*1.75)
        timelmin2=float((em/60)*1.75)
        lmintotal=timelmin+timelmin2
        finallw=(float(timelhr+lmintotal))
        bill=round(finallw,2)
        print("The total bill is $",bill)
        return
wage()
                 



#4 ch 7 prog exer 8
def main():
    age=int(input("enter age in years:"))
    cit=int(input("enter years of citizenship in US:"))
    if age >= 25 and cit >= 7:
        print("You are eligible to run for US Rep!")
    else:
        print("You are not eligible to run for US Rep.")
    if age >= 30 and cit >= 9:
        print("You are eligible to run for US Sentate!")
    else:
        print("You are not eligible to run for US Senate.")
main()
        


#5 old problem rewrite
#5 ch 5 prog ex 3
def exam():
    try:
        st = "FFFFFFDCBAA"
        score = int(input("Enter exam score: "))
        pos = score//10
        LG = st[pos]
        print("Your grade is: ",LG)
    except ValueError or IndexError:
        print("Value given not computable.")
exam()
#This decision structure gives an error message for exams scores given as
#either integers not between o-100 or given as non-integers.


















