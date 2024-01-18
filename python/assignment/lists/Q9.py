from random import randint
my_list = []
for i in range(10):
    my_list.append(randint(1,500))
my_list.sort()
print("list is",my_list)
print("second maximum number is ",my_list[len(my_list)-2])
