# using function remove the given word from the list 
# and strip it at same time


def rem(l, word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n 

l = ["Vimal", "Rohan", "Shubham", "an"]

print(rem(l, "an"))