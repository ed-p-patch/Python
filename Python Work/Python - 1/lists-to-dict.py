name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(l1, l2):
    new_dict = {}
    
    for x in range(0, len(l1)):
        if len(l1) > len(l2):
            new_dict.update({l1[x]:l2[x]})
        else:
            new_dict.update({l2[x]:l1[x]})
    return new_dict

print make_dict(name, favorite_animal)