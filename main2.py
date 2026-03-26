import os

if os.path.exists("example.txt"):
    print("file already exists")
else:
    file=open("example.txt", "x")
    print("file created succesfully")