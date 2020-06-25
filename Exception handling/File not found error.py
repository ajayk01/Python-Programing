f=input("Enter the file name");
try:
    f1=open(f,"r");
    print("File is successfully opened");
except(FileNotFoundError):
    print("The file is not found");
else:
    print("Thank you");
    

