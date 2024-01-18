n=int(input())
div=[]
for i in range(1,n):
    if n%i==0:
        div.append(i)
        
if sum(div)==n:
    print("Perfect Nummber")
else:
    print("Not a Perfect Number")