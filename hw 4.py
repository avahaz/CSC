#hw 4

#1 ch 5 diss prob 1
s1="spam"
s2="ni!"
#c
s1[1]
#result= p

#e
s1[2]+s2[:2]
#result= ani

#g
s1.upper()
#result= SPAM




#2 ch 5 diss prob 2
s1="spam"
s2="ni!"
#a: show "NI"
s2[:2].upper()

#d: show spam
s1

#e: show ["sp","m"]
s1[:2],s1[3]




#3 ch 5 diss prob
#b
for ch in "aardvark":
    print(ch)
a
a
r
d
v
a
r
k

#c
for w in "Mississippi".split("i"):
    print(w,end=" ")
M ss ss pp

#e
msg=" "
for ch in "secret":
    msg = msg +chr(ord(ch)+1)
    print(msg)
t
tf
tfd
tfds
tfdsf
tfdsfu




#4 loop of grades
print("grades= ",end='')
for f in range(60):
    print("F",end="")
for d in range(10):
    print("D",end="")
for c in range(10):
    print("C", end="")
for b in range(10):
    print("B", end="")
for a in range(10):
    print("A", end="")




#5 ch 5 prog ex 3
def exam():
    st = "FFFFFFDCBAA"
    score = int(input("Enter exam score: "))
    pos = score//10
    LG = st[pos]
    print("Your grade is: ",LG)
exam()




#6 ch 5 prog ex 4
def shorter():
    string = input("Enter a phrase: ")
    phrase = string.split()
    firsts = []
    for word in phrase:
        L1= word[0].upper()
        firsts.append(L1)
    acronym="".join(firsts)
    print("Your acronym is: ",acronym)
shorter()
               

    

#7 ch 5 prog ex 5
def nv():
    name=input("enter name: ")
    name = name.lower()
    total = 0
    for letter in name:
        let_val = ord(letter)-96
        total = total + let_val
    print("Your name value is ", total)
nv()





















