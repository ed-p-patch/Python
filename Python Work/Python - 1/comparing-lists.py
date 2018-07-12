list_one = [1, 2, 3, 4, 5, 6]
list_two = [1, 2, 3, 4, 5, 6]
array_end = len(list_one)

for x in range(0, len(list_one)):
    if len(list_one) != len(list_two): # if the arrays are different sizes
        print "The lists are not the same!"
        break
    if list_one[x] != list_two[x]: # check contents of matching index
        print "The lists are not the same!"
        break
    if (x+1 == array_end): # Are we at the end of the array?
        print "The lists are the same"