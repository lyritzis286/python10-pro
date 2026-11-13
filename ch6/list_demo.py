my_list = [1, 2, 3]
my_list2 = [0] * 5 #dimiourgei mia lista me 5 midenika , like repeat(0,5) in other lang

#ektiposi tis listas me range
for i in range(len(my_list)):
    print(my_list[i])

#print list
for item in my_list:
    print(item)

print(*my_list, sep=", ")

my_slice = my_list[1:3]