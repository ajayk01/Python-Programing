a=int(input("Enter the  value"));
sum=0;
r=0;
while(a!=0):
	r=a%10;
	sum=int(sum+r);	
	a=a/10;
print("The sum of the digits is ",sum);
