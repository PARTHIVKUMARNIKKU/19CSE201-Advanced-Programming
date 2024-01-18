import random
p1=random.randint(1,100)
p2=random.randint(1,160)
p3=random.randint(1,130)
p4=random.randint(1,123)
p5=random.randint(1,130)
p6=random.randint(1,123)
inventory=[["apple",11,"fruits"],
           ["orange",13,"fruits"],
           ["potato",5,"vegetables"],
           ["tomato",4,"vegetables"],
           ["cashew",8,"dry_fruits"],
           ["pistha",50,"dry_fruits"]]
catagories=set()
inv_quantity_list=[]
cat_total_list=[]
total=0

for i in range(0,6):
    catagories.add(inventory[i][2])
print(catagories)
for i in range(0,6):
    inv_quantity_list.append(inventory[i][1])
    inv_quantity_list.sort()
print(inv_quantity_list)
max=inv_quantity_list[5]
for i in range(0,6):
    if(inventory[i][1]==max):
        print(inventory[i])
for i in range(0,6):
    if(inventory[i][2])=="fruits":
        cat_total_list.append(inventory[i][1])
print(cat_total_list)
for num in cat_total_list:
    total += num
print("Total Quantity per Category:",total)