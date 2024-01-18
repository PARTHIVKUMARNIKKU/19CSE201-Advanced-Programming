n=int(input())
x=[0,1]
for i in range(2,n):
    y=x[i-1]+x[i-2]
    x.append(y)
    
print(x)