def createFile(fileName):
    file=open(fileName,"x")
    return f"file created successfully: \nFile name: {fileName}"

def writeInFile(content, fileName):
    with open(fileName, "w") as f:
        f.write(content)
    return "file updated successfully!"

def read(fileName):
    with open(fileName, "r") as f:
        file=f.read()
        return file
    
while True:
    print("Select option below:\n1. Create file \n2. Write into a file \n3. Read a file")
    choice=input("Enter choice:  ")
    if choice=="1":
        fileName=input("enter file name:  ")
        createFile(fileName)
        continue
    elif choice=="2":
        fileName=input("enter file name:  ")
        input=input("enter the contentof file:  ")
        writeInFile(input, fileName)
        continue
    elif choice=="3":
        fileName=input("enter file name:  ")
        print(read(fileName))
        continue
    if choice=="exit":
        break