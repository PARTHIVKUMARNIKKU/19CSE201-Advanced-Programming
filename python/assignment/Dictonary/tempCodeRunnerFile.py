D1 = {'first_name' : 'Jim', 'age' : 23, 'height' : 6.0 , 'job' : 'developer', 'company': 'XYZ'}
D2 = {'age' : 35, 'job' : 'senior data analyst'}
for key in D1:
    for key2 in D2:
        if key==key2:
            D1[key]=D2[key2]
print("updated dictionary:",D1)
print(D2)