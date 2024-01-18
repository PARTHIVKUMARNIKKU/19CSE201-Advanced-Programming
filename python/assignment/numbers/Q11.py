n=int(input("enter the number please"))
factors=[]
i=2
while n>1:
    while (n%i==0):
        n=n/i
        factors.append(i)
    i=i+1
print(factors)