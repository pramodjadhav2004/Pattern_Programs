string = input()
string_list = string.split()

small = 999999999
for i in string_list:
    i = int(i)
    if i < small:
        small = i
print(small)