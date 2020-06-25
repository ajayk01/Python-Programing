a=int(input("Enter the A value"));
i=1;
t1=0;
t2=1;
while(i<=a):
	print(t1," + ");
	sum=t1+t2;
	t1=t2;
	t2=sum;	
	i+=1; 
