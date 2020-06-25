def uses_only(s,l):
    for i in s:
        if(i not in l):
            return False;
            break;
    return True;

n=int(input("Enter the no of letters"));
s=[];
for i in range(0,n):
    l=input("Enter the letter : ");
    s.append(l);
l=input("Enter the word");
print(uses_only(s,l));
