f = open("poem.txt", "r")

c = f.read()

if("twinkle" in c):
    print("word present")
else:
    print("Not present")