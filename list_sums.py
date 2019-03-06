"""Given two lists, find if there are any combinations that sum to 8."""

list1 = [1,1,3,6]
list2 = [1,2,3,6]

combs = ([(x,y) for x in list1 for y in list2])

for i in combs:
    if sum(i) == 8:
        print('The following combination sums to 8: ')
        print(i)
