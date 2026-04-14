# write the data in file 
# w - if file not exist then create new file

file = open("example.txt", "w")
file.write("Hello World!")
file.close()


# read the file and print the data
# r - reading the file

file = open("example.txt", "r")
data = file.read()
print(data)
file.close()