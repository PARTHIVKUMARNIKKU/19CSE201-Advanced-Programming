nv=[]
i=int(input())
for x in range(i):
    prodname=input()
    prodq=int(input())
    prodc=input()

    prod_tuple=(prodname,prodq,prodc)

    Inv.append(prod_tuple)

Cat=set()
Cat_list=list(Cat)
x=len(Cat_list)
quan=set()
sorted_quan=set()
for inner_list in Inv:
    if len(inner_list)>=3:
        Cat_v=inner_list[2]
        Cat.add(Cat_v)
print(Cat)
for y in range(i):