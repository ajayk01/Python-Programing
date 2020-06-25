a=int(input("Enter the  value"));3
b=a;
c=a;
count=0;
r=0;
sum=0;
while(a!=0):
	r=int(a%10);
	count+=1;	
	a=int(a/10);
print(count);
while(b!=0):
	r=int(b%10);
	sum=int(sum+(r**count));
	b=int(b/10);
if(sum==c):
	print("The number is Amstrong");
else:
	print("The number is not Amstrong");
