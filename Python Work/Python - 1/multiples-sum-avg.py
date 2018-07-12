# E Patch
# --- Multiples - Part 1 --- #
for num in range(1, 1000):
    if num % 2 == 0:
        pass # Do Nothing
    else:
        print num # Print odd number
# --- Multiples - Part 2 --- #
for num in range(5, 1000000):
    if num % 5 == 0:
        print num # Print multiples of 5
    else:
        pass # Do Nothing
# --- Sum List ------------- #
a = [1, 2, 5, 10, 255, 3]
b = 0
for num in range(0, len(a)):
    b += a[num]
print b
# --- Average List --------- #
a = [1, 2, 5, 10, 255, 3]
b = 0
for num in range(0, len(a)):
    b += a[num]
print (b/len(a))
# -------------------------- #