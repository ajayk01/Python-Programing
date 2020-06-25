def abcd(a):
    l=sorted(a)
    b=[]
    for i in a:
        b.append(i)
    if(b==ls):
        return True
    else:
        return False
s=input("Enter the word to check whether it is alpabatical order");
if(abcd(s)):
    print("It is in alpabatical order");
else:
    print("It is not in alpabatical order");
            
