n=int(input("Enter the no of words"));
s=[];
for i in range(0,n):
    a=input("Enter the word");
    s.append(a);
print("The enter words are ",s);
count=0;
for i in s:
    for j in i:
        if(j!=" "):
            count+=1;
    if(count>=20):
        print(i);
