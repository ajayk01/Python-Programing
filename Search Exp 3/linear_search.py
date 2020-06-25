def linear(a):
	flag=0;
	b=float(input("Enter the number to be searched"));
	j=-1;
	for i in a:
		if(i==b):
			flag=1;
			j+=1;
			break;
		else:
			flag=0;
			j+=1;
	if(flag):
		print("The element",b,"is present at ",j);
	else:
		print("The element",b,"is not present");
	
c=int(input("Enter the number of elements"));
l=[];
for i in range(0,c,1):
	d=float(input());
	l.append(d);
print(l);
linear(l);
