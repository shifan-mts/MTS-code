#elif = else if
i = int(input("enter your value")) #5
j = int(input("enter your second value")) #2
if i < j: #5<2
    print(i,"is the lowest") #false
elif j<i: #2<5
    print(j,"is the lowest")
else:
    print("both",i,"and",j,"are equal")        