class stackfull(Exception):
    pass;
class stackempty(Exception):
    pass;
stack=[];
size=30;
i=0;
try:
    def isempty():
        if(i==0):
            raise stackempty;
    def isfull():
        if(i==30):
            raise stackfull;
    def push(a):
        global i;
        if(isfull()):
            pass;
        else:
            stack.append(a);
            i+=1;
    def pop():
        global i;
        if(isempty()):
            pass;
        else:
            return stack.pop();
            i-=1;
    while(True):
        l=int(input("Enter the the choice \n 1.Isempty \n 2.Isfull \n 3.Push \n 4.Pop\n"));
        if(l==1):
            if(isempty()):
                pass;
        elif(l==2):
            pass;        
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
except stackfull:
     print("The stack is full");
except stackempty:
     print("Stack is empty");