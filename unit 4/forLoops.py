# a list and filters the values

fruits == ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'banana':
        fruits.remove(x)
        print(x)


grades =[80,90,70,70,100,60] 
for x in grades:
    if x < 80:
        grades.remove(x)
        countinue
    print(x)


