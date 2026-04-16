# replace word with anything 

word = "Mihir"

with open(f"Chapter_9_file/practice set file/file.txt", "r") as f:
    content = f.read()
    #print(content)

contentNew = content.replace(word, "######")

with open(f"Chapter_9_file/practice set file/file.txt", "w") as f:
    f.write(contentNew)