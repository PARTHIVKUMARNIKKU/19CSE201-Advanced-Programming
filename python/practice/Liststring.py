given_list=["abc", "xyz", "aba", "1221"]
counter=0
for i in range (len(given_list)):
    x=len(given_list[i])-1
    if(given_list[i][0]==given_list[i][x] and len(given_list[i])>2):
        counter=counter+1
print(counter)