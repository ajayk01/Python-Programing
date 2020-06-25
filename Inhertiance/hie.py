class RC:
    def set1(self):
        self.dis=int(input("Enter the discount "));
    def get1(self):
        print("The discount is ",self.dis);
class PC:
    def set2(self):
        self.mtype=input("Enter the membership type");
    def get2(self):
        print("The discount is ",self.mtype);
class Cus(RC,PC):
    def get(self):
        self.cid=int(input("Enter the customer id:"));
        self.cname=input("Enter the customer name:");
        self.type=int(input("1.RC \n 2.PC"));
        if(self.type==1):
            self.set1();
        else:
            self.set2();
    def put(self):
        print("Customer Id ",self.cid,"\nCustomer Name:",self.cname);
        if(self.type==1):
            self.get1();
        else:
            self.get2();
C=Cus();
C.get();
C.put();
            
    