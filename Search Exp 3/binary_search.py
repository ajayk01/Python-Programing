def search(a,s,l,e):
	while (s<= l):
		m =int((s+l)/2);
		if (e>a[m]):
			s= m+1;
		elif (e<a[m]):
			l= m-1;
		elif (e == a[m]):
			return m;
	return -1
	
c=int(input("Enter the number of elements"));
a=[];
for i in range(0,c,1):
	d=int(input());
	a.append(d);
e=int(input("Enter the element to be searched"));
a=sorted(a);
s = 0
l= len(a)-1
flag =int(search(a,s,l,e))
if (flag==-1):
	print("element not present in array");
else:
	print("element is present");
