n=""
n=(input())
x=len(n)
a=0
for i in n:
    
    a=int(i)**3+a
if a==int(n):
    print("Armstrong")
else:
    print("Not Armstrong")