string_output=[]
string_input=input("enter the string")
if len(string_input)>=0 and len(string_input)<=1000:
    for i in string_input:
        res=i.isupper()
        if res==True:
            ans=i.lower()
            string_output.append(ans)
        elif res==False:
            ans=i.upper()
            string_output.append(ans)
    result="".join(string_output)
    print(result)