num = int(input("Enter the number of row for pyramid"))
for i in range (num):
    for j in range (i+1):
        print(j+1, end = " ")
    print()