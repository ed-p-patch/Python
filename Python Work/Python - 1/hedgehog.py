import ipyturtle
# the distance we want the pointer to travel each time
DIST = 100
t = Turtle().ipyturtle
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        t.right(90)
        # advance according to set distance
        t.forward(DIST)
    # add to set distance
    DIST += 20