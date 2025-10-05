import shutil

with open("source.txt", "w") as file:
    file.write("This is the source file.")

shutil.copyfile("source.txt", "destination.txt")
print("ファイルをコピーしました")