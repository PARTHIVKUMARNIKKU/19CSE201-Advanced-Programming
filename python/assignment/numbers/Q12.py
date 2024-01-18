a=int(input())
b=int(input())

while b:
    carry =a&b
    a=a^b
    b= carry << 1
    
print(a)