s=set();
s={1,2,3,4,5,6}
for i in s:
    print(i);
s.add(8);
print("The removed element from the set is ",s.pop());
print("The set 1 is ",s);
s1={1,2,3,4}
print("The set 2 is",s1);
print("The intersection of set is ",s.intersection(s1));
print("The union of set is ",s.union(s1));
print("The set difference is ",s.difference(s1));
print("The symmentric difference",s.symmetric_difference_update(s1));
if(s.issubset(s1)):
    print("S is subset of s1");
else:
    print("S is not a subset of s1");
if(s.issuperset(s1)):
     print("S is super class  of s1");
else:
    print("S is not a super class of s1");
print("The length of the set is ",len(s));