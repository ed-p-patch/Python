def is_prime(n):
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 7 == 0:
        return False
    for x in range(100, 100000):
        if n % x == 0:
            return False
    return True

def is_perfect_square(n):
    for x in range(1, 317):
        if (x * x) == n:
            return True
    return False

for x in range(100, 100000):
    if is_prime(x):
        print "Foo ", x
    else:
        if is_perfect_square(x):
            print "Bar ", x
        else:
            print "FooBar", x