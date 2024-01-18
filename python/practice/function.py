'''def my_function(name):#thid name is the parameter
    if name=="pardhu":
        print("pardhu is invoked")
    else:
        print("ima not pardhu")
name=input("enter the name please")
my_function(name)#this name is an arguement'''

def  many_attributes(*classs):
    print("1st one is ", classs[0])
    print("second one is", classs[1])
    print("third one is", classs[2])
many_attributes("1st","2nd","3rd")