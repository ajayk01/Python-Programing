import math
def Merge(b,c,a):
    p=len(b)
    q=len(c)
    i,j,k=0,0,0
    while(i<p and j<q):
        if(b[i]<=c[j]):
            a[k]=b[i]
            i=i+1
        else:
            a[k]=c[j]
            j=j+1
        k=k+1
    if(i==p):
        for l in range(j,q):
            a[k]=c[j]
            j=j+1
            k=k+1
    else:
        for l in range(i,p):
            a[k]=b[i]
            i=i+1
            k=k+1
    
def MergeSort(a,n):
    if(n>1):
        m=math.floor(n/2)
        b=a[0:m]
        c=a[m:n]
        MergeSort(b,len(b))
        MergeSort(c,len(c))
        Merge(b,c,a)

n=int(input("Enter number of values : "))
a=[]
for i in range(0,n):
    d=int(input("Enter value : "))
    a.append(d)
MergeSort(a,len(a))
print("Merge Sorted : ",a)