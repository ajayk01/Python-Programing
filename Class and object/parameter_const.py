class upper:
    def __init__(self,s):
        self.s=s;
    def print_string(self):
        print(self.s.upper());
s=input("Enter the string to be printed in upper case");
u=upper(s);
u.print_string();