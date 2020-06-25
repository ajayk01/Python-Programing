s=[];
for i in range(0,10):
    a=input("Enter the String");
    s.append(a);
print("The string are \n",s);
for i in s:
    l=len(i);
    count=0;
    for j in range(0,l-1):
        if(i[j]==i[j+1]):
            count+=1;
    if(count>=3):
        print(i);

    
