def default(name,age=10):
    if(age>10):
        print("Your name is ",name ,"and your above age 10");
    else:
        print("Your name is ",name ,"and your below age 10");
c=input("Enter your name");
a=int(input("Enter your Age"));
default(c,a);
default(c);