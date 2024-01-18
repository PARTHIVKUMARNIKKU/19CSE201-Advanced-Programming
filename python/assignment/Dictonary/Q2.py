D1 = {2: 8, 5: 20, 3: 15}
keys=list(D1.keys())
values=list(D1.values())
sum_list=[]
for i in range(len(D1)):
    sum=keys[i]+values[i]
    sum_list.append(sum)
print(sum_list)