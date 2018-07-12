l = ['magical unicorns', 19, 'hello', 98.98, 'world']

new_string = ""
new_sum = 0
new_bool_list = []

for x in range(0, len(l)-1):
    if type(l[x]) is str:
        new_string += l[x]
        lt = "string"
    if type(l[x]) is int: # I realize this wont catch floats
        new_sum += l[x]
        lt = "integer"

# First, check list for type-consistency for mixed
for x in range(0, len(l)-1): # we use len(l)-1 to stop from checking an index that doesnt exist
    if type(l[x]) != type(l[x+1]):
        lt = "mixed"
        print "The list you entered is of mixed type"
        print "String:", new_string
        print "Sum:", new_sum
        break

if lt == "string":
    print "The list you entered is of string type"
    print "String:", new_string
elif lt == "integer":
    print "The list you entered is of type integer"
    print "Integer:", new_sum