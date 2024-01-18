#EMPTY list
my_list = []
print ("choice 1 = do you want to create task \n" )
print ("choice 2 = new task at priority \n")
print ("choice 3 = complete task\n")
print ("choice 4 = clear task\n")
print ("choice 5 = remove a particular task\n")
print ("choice 6 = sort ascending\n")
print ("choice 7 = sort descending\n")

while True:
    choice = int(input("please enter the choice: number \n"))
    if(choice==1):
        #new task
        taskInput= str(input("enter the task that to be added\n"))
        my_list.append(taskInput)
    elif(choice==2):
        taskInput= str(input("priority task"))
        my_list.insert(0,taskInput)
    elif(choice==3):
        taskInput=str(input("please enter the task that is completed\n"))
        index=my_list.index(taskInput)
        print("index of the item removed is",index)
        my_list.remove(taskInput)
        print("And the new list is",my_list)
    elif(choice==4):
        my_list.clear()
        print("new list is",my_list)
    elif(choice==5):
        print("new list is",my_list)
        taskInput=int(input("please enter the input of the index from which it should be removed\n"))
        my_list.pop(taskInput)
        print("new list is",my_list)
    elif(choice==6):
        my_list.sort()
        print("sorted list",my_list)
    elif(choice==7):
        my_list.sort(reverse=True)
        print("sorted list",my_list)
    else:
        break
