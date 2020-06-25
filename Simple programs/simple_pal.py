a=int(input("Enter the  value"));3
b=a;
sum=0;
r=0;
while(a!=0):
	r=int(a%10);
	sum=int(sum*10+r);	
	a=int(a/10);
print("The reverse of the digits is=%d "%sum);
if(sum==b):
	print("The number is palindrome");
else:
	print("The number is not palindrome");
