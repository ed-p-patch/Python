def odd_even():
    # for x in range(1, 2001):
      for x in range(1, 9):
        if x % 2 == 0:
            print "Number is ", x, " This is an even number"
        else:
            print "Number is ", x, " This is an odd number"

def multiply(list, y):
    new_list = []
    for x in range(0, len(list)):
        new_list.append(y * list[x])
    return new_list

def layered_multiples(arrr):
    final_arr = []
    length = len(arrr)
    
    for x in range(0, length):
        new_arr = []
        for y in range(0, arrr[x]):
            new_arr.append(1)
        final_arr.append(new_arr)
    return final_arr

print "Odd/Even Function"
odd_even()
print "Multiple Function"
arr = [1, 2, 3, 4, 5]
print multiply(arr)
print "Hacker Challenge"
t = layered_multiples(multiply([2,4,5], 3))
print t