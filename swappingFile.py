



def swapFileData():
    print("Enter the names of the files that you want to have their data swapped.")

    file1 = input("Enter the first file to be swapped.")
    file2 = input("ENter the second file to be swapped.")

    data_a = ""
    with open ("file1","r+") as f:
        data_a = f.read
    
    data_b = ""
    with open ("file2","r+") as f:
        data_b = f.read

    
    file1.write(data_b)

    
    file2.write(data_a)

    print("This is the first file now: ",file1)

    print("This is the second file now: ",file2)
    


swapFileData()


#data = ""
#with open("/documents/sample.txt", "r+") as f:
#    data = f.read()
