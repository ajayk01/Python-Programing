dic1={"one":1,"two":2,"three":3}
dic2={"four":4}
dic3={"five":5}
l=list(dic1.values());
print(sorted(dic1.values()))
print(l[::-1]);
print(l);
sum=0
m=1
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
ke=input("Enter key to be searched")
for i in dic1:
    if(ke==i):
        print("Key found")
        break;
else:
    print("Not found")
for i in dic1.values():
    sum+=i
print("Sum is =",sum)
for i in dic1.values():
    m*=i
print("product is =",m)
print("MAX=")
print(max(dic1.values()))
print("MIN=")
print(min(dic1.values()))
d={}
n=int(input("Enter the range"))
for x in range(1,n+1):
    d[x]=x*x
print(d)
print(sorted(dic1.keys()));
if not  bool(dic1):
    print("The dict is empty");
else:
    print("The dict is not empty");
d1 = {'a': 100, 'b': 200}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}
d3.update(d2);
for i, j in d1.items():
    for x, y in d2.items():
        if i == x:
            d3[i]=(j+y)
print("The updated list is ",d3);
dic1=sorted(dic1.values());
l=len(dic1);
a=l-3;
for i in range(a,l):
    print(dic1[i],end=" ");


            
