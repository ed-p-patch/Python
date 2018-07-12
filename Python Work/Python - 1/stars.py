# Part 1
def draw_stars(arr):
    for x in range(0, len(arr)):
        new_string = ''
        for y in range(0, arr[x]):
            new_string += '*'
        print new_string

# Part 2
def draw_stars_v2(arr):
    for x in range(0, len(arr)):
        new_string = ''
        if isinstance(arr[x], str):
            s = arr[x]
            for z in range(0, len(s)):
                new_string += s[0].lower()
        elif isinstance(arr[x], int):
            for y in range(0, arr[x]):
                new_string += '*'
        print new_string

a = [4, 6, 1, 3, 5, 7, 25]
b = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(a)
draw_stars_v2(b)