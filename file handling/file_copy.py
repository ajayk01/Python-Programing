f=open("E:file.txt","r");
f1=open("file1.txt","w");
l=f.read();
f.close();
l=l.split();
l1=[];
for i in l:
    if(i not in l1):
        l1.append(i);
for i in l1:
    f1.write(i);
    f1.write(" : ");
    f1.write(str(l.count(i)));
    f1.write("\n");
f1.close();
f1=open("file1.txt","r");
print(f1.read());
f1.close();
