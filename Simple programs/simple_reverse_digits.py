a=int(input("Enter the  value"));
sum=0;
r=0;
while(a!=0):
	r=int(a%10);
	sum=int(sum*10+r);	
	a=int(a/10);
print("The reverse of the digits is=%d "%sum);
