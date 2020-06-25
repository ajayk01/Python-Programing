class employee:
    def __init__(self):
        self.name=input("Enter the name of the employee");
        self.age=int(input("Enter the age of the employee"));
        self.id=int(input("Enter the ID of the employee"));
        self.basic= int(input("Enter the Basic salary of the employee"));
        self.da=float(input("Enter the DA of the employee"));
        self.ta=float(input("Enter the TA of the employee"));
        self.hra=float(input("Enter the HRA of the employee"));
    def display(self):
        print("The name of the employee :",self.name);
        print("The ID of the employee :",self.id);
        print("The AGE of the employee :",self.age);
        salary=self.basic+(self.basic*self.da/100)+(self.basic*self.ta/100) -self.hra;
        print("The total salary is :",salary);
e=employee();
e.display();
        
        