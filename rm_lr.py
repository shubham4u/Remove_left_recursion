#!/usr/bin/python3
import sys
non_terminal=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
op=("+","-","/","*","^","(",")")
x=("|")
n=int(input("Enter the number of terminal :- "))
for i in range(n):
    s=input("Enter the starting terminal :- ")
    p=input("Enter the production  :- ")
    grammer=("grammer is "+s+ "->" +p)
    print(grammer)
    if s[0]==p[0]:
        p=p.split("|")
        #if(p!=x):
        p.append("EPS")
        print(p)
        f=("1st production is :-"+s+"->"+p[1]+""+s+"`")
        print(f)
        s=("2nd production is :-"+s+"`->"+p[0][1:]+""+s+"`|"+p[-1])
        print(s)
    else:
        print("Grammer is not recursive")
if s in non_terminal:
	print("Grammer is incorrect")
elif s[0]==p[0]:
	print("It Is Recuursive")
elif p[0] in op:
	print("Grammer is not recursive")
else:
	print("Solve")

