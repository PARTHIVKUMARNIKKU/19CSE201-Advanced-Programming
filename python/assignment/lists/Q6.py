sum=13
my_lis=[1,2,3,4,5,6,5,8,9,10,11]
my_set=set(my_lis)
my_list=list(my_set)
for i in my_list:
    for j in my_list:
        if (i+j==sum and my_list.index(i) <= my_list.index(j)):
            print(i,j)