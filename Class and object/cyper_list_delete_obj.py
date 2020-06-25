class cyber:
    def __init__(self):
        self.name=input("Enter the name of the user:");
        self.phone_num=int(input("Enter the mobile number of the user:"));
        self.username=input("Enter the username of the user:");
        self.password=input("Enter the password of the user:");
    def display(self):
        print("The name of the user:",self.name);
        print("The Mobile number of the user:",self.phone_num);
        print("The username of the user:",self.username);
n=int(input("Enter the no of user"));
l=[];
for i in range(0,n):
    c=cyber();
    l.append(c);
s=input("enter the username to be searched");
for i in range(0,n):
    if(l[i].username == s):
        l.remove(l[i]);
for i in l:
    i.display();
    