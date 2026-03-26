with open("sample.txt", "r") as f:
    file=f.read()
    print()

with open("sample.txt", "w") as f:
     f.write("Hello! My name is Mary and I a 14 years old. \n I am a student at ABC High School. \n I love to play soccer and read books. \n I am currently learning how to code on python")
with open("sample.txt", "r") as f:
     file=f.read()
     print(file)