num= int(input("Enter the no of rows: "))
for i in range(1,num+1):
    space = (num - i) * ". "
    for j in range(i):
        pattern = (i+j)*"0 "
    print(space+pattern+space)
for i in range(1,num):
    space = i * ". "
    for j in range(i):
        pattern = (2*(num - i) - 1) * "0 "
    print(space+pattern+space)