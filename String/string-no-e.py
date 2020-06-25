n=int(input("Enter the no of words"));
s=[];
s1=[];
for i in range(0,n):
    a=input("Enter the word");
    s.append(a);
print("The enter words are ",s);
count=0;
for i in s:
    if("e" not in i):
        s1.append(i);
print(s1);
print("The no of words that has no e is ",len(s1));
print("The percentage of words that has no e is",(len(s1)/len(s))*100,"%")
