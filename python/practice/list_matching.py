key=list(input())
lists = []

number_of_students=int(input())
for i in range(number_of_students):
    lists.append(input())
for i in range(number_of_students):
    marks=0
    for j in range(len(key)):
        if(key[j]==lists[i][j]):
            marks=marks+1
    print(marks)