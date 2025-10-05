import os

with open("./sample.txt","w") as file:
    file.write("Hello, World!")

with open("./sample.txt","r") as file:
    content = file.read()
    print(content)

os.remove("./sample.txt")