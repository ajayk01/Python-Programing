class Event:
    def get(self):
        self.Name=input("Enter the name" );
        self.ownerName=input("Enter the owner name");
        self.noOfDays=int(input("Enter the no of days"));
        self.costPerDay=float(input("Enter the cost per day"));
class Exhibition(Event):
    
    def calulate(self):
        self.gamount=self.costPerDay*self.noOfDays;
        self.gst=self.gamount*5/100;
        self.namount=self.gst+self.gamount;
    def display(self):
        print("The Gross amount:",self.gamount,"\nGST: ",self.gst,"\n Net amount:",self.namount);
class StageEvent(Event):
    def calulate(self):
        self.gamount=self.costPerDay*self.noOfDays;
        self.gst=self.gamount*5/100;
        self.namount=self.gst+self.gamount;
    def display(self):
        print("The Gross amount:",self.gamount,"\nGST: ",self.gst,"\n Net amount:",self.namount);
p=int(input("Menu \n 1.Exhibition\n2.Stage Event"));
if(p==1):
    ex=Exhibition();
    ex.get();
    ex.calulate();
    ex.display();
elif(p==2):
    st=StageEvent();
    st.get();
    st.calulate();
    st.display();
else:
    print("Enter the valid event");
    
        
        