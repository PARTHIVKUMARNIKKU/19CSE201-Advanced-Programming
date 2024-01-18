n=int(input())
n=str(n)
x=len(n)
a=0
for i in n:
    if i=='0' or i=='1':
        a=a+1
if a==x:
    print("Binary")
else:
    print("Not Binary")