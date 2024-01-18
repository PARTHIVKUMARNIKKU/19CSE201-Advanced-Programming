string_input=input("please enter the string")
str_list=[]
new_list=[]
string_length=len(string_input)
if string_length%2==0:
    print(string_input.upper())
else:
    str_list=string_input.split()
    #print(str_list)
    for i in str_list:
        x=i.capitalize()
        new_list.append(x)
    #print(new_list)
    new_list="-".join(new_list)
    print(new_list)