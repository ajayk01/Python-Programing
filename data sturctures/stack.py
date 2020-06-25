stack=[];
size=30;
i=0;
def isempty():
    if(i==0):
        return 1;
    else:
        return 0;
def isfull():
    if(i==30):
        return 1;
    else:
        return 0;
def push(a):
    if(isfull()):
        print("The stack is full cannot push elements");
    else:
        stack.append(a);
        i+=1;
def pop():
    if(isempty()):
        print("The stack is empty");
    else:
        return stack.pop();
        i-=1;
while(True):
    l=int(input("Enter the the choice \n 1.Isempty \n 2.Isfull \n 3.Push \n 4.Pop\n"));
    if(l==1):
        if(isempty()):
            print("The stack is empty");
        else:
            print("The stack is full");
    elif(l==2):
        if(isfull()):
            print("The stack is full");
        else:
            print("The stack is empty");
    elif(l==3):
        a=int(input("Enter the element to be pushed\n"));
        push(a);
    elif(l==4):
        a=pop();
        print("The poped element is ",a);
    else:
        print("Enter the from 1 to 4");
    k=int(input("1.To continue \n 0. To End\n"));
    if(k==0):
        break;
print("Thank you");
        
        