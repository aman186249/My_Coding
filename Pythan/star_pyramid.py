num = int(input("Enter the number of row for pyramid"))
for i in range (num):
    for j in range (1,num-1):
        print(' ', end = " ")
    for k in range (i*2+1):
        print('*', end = " ")
    print()