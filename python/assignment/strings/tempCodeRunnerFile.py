text=input("please enter the name you wnat to find the text in")
n=input("enter the letter you want to remove")
text_list=list((text))
#print(text_list)
for i in range(len(text_list)-1):
    if text_list[i]==n:
        text_list[i]=""
    else:
        pass
print(text_list)