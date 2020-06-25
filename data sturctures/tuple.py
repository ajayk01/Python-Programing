t=(1,2,3,4,3,5,3,7,8);
print("The tuple is ",t);
s=str(t);
print("The converted string from the tuple is ",s);
l=list(t);
print("The converted list from the tuple is ",l);
length=len(t);
print("The 4th length in tuple is ",t[3]);
print("The 4th length in tuple from the last is ",t[length-4]);
print("The repeated elements are ");
for i in range(0,length-1):
    for j in range(i+1,length):
        if(t[i]==t[j]):
            print(t[j])
k=int(input("enter the element to searched in tuple"));
for i in range(0,length):
    if(k==t[i]):
        flag=1;
    else:
        flag=0;
if(flag):
    print("The element is present");
else:
    print("The element is present");
l.pop();
t=tuple(l);
print("The last element is removed in tuple");
n=int(input("Enter the range from which the tuple is sliced"));
print("The tuple after the slice is ",t[0:n]);
print("The length of the tuple is ",len(t));
l1=[(1,2,3,40),(93,4,5),(0,1,2,3,4)];
for i in l1:
    print(list(i));
l=list(t);
print(l);
l.reverse();
print("The reserve of tuple is",l);
