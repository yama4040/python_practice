lines = ["Line 1", "Line 2", "Line 3", "Line 4", "Line 5"]

with open("output.txt", "w") as file:
    file.writelines("\n".join(lines))

with open("output.txt", "r") as file:
    content = file.read()
    print(content)