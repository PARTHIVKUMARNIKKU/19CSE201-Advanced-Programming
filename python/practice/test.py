my_dict=dict({})
strength = int(input("enter the strength of the class\n "))
for i in range(1,strength+1):
    templete_rollnumber = "CB.EN.U4CYS220XX"
    roll_number = i
    #roll_number = int(input("please enter the roll number "))
    if roll_number < 10:
      templete_rollnumber = templete_rollnumber.replace("XX", "")
      templete_rollnumber = templete_rollnumber + "0" + str(roll_number)
      #print(templete_rollnumber)
      name= input("please enter the name \n")
      my_dict[templete_rollnumber]=name
    else:
       templete_rollnumber=templete_rollnumber.replace("XX", str(roll_number))
       #print(templete_rollnumber)
       name= input("please enter the name \n")
       my_dict[templete_rollnumber]=name
print(my_dict)
print("number of elements in the dictionary=", my_dict, "\n")
