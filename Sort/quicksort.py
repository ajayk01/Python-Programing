def part(a,l,h): 
	i = (l-1 )		  
	pivot = a[h]	 

	for j in range(l,h): 
		if a[j] <= pivot: 
			i = i+1
			a[i],a[j] = a[j],a[i] 
	a[i+1],a[h] = a[h],a[i+1] 
	return ( i+1 )  
def quickSort(a,l,h): 
	if l< h: 
		pi = part(a,l,h) 
		quickSort(a,l, pi-1) 
		quickSort(a, pi+1, h) 
a=[];
n = int(input("Enter the no of the elements"))
for i in range(0,n):
    k=int(input());
    a.append(k);
print("The entered array is",a);
quickSort(a,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d" %a[i]), 
