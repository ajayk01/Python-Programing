a=10
b=0
try:
    quotient=a/b
    print("Result: ",quotient)
except ZeroDivisionError:
    print("Divide by zero error")
finally:
    print("The program has been ended")
    
    
try:
    a=int(input("Enter a number"))
    print("Input given is: ",a)
except ValueError:
    print("ERROR!Enter a valid number")
    

try:
    file=open("sample.txt","r")
    print(file.read())
except IOError:
    print("File does not exists")


try:
    a=[37,15,26]
    print(a[5])
except IndexError:
    print("Index error")
try:
    b=10
    print(d)
except NameError:
    print("Name Error")
try:
    c=5+'a'
    print(c)
except TypeError:
    print("Type Error")
try:
    res=math.pow(2,3)
    print(res)
except NameError:
    print("Name Error")
try:
    import power
    power.square();
except ImportError:
    print("Import Error")
try:
    dict={1:'a',2:'b',3:'c'}
    print(dict[4])
except KeyError:
    print("Key Error")


