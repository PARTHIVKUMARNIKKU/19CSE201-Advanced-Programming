text=input()
text=text.lower()
if text== text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")