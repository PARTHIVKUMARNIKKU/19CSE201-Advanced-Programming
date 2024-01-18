n=int(input())
n=str(n)
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")