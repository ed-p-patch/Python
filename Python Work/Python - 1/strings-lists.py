# E Patch
words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day') # returns 18
print words.find('day', 19) # returns 36
print words.replace('day', 'month') # replaces day for month
x = [2,54,-2,7,12,98]
print min(x) # returns -2
print max(x) # returns 98
y = ["hello",2,54,-2,7,12,98,"world"]
print y[0], y[-1] # returns hello world
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
length = (len(z)/2) # rounded down
w = []
for index in range(0, length): # obtain the first half of the list 
    w.append(z[index])
for index in range(1, length): # delete each index except the one we will insert the new list
    del z[0]
z[0] = w
print z