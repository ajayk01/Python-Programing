class vechicle:
    def __init__(self):
        self.name=input("Enter the name of the vechicle");
        self.color=input("Enter the color of the vechicle");
        self.price=input("Enter the price of the vechicle");
    def display(self):
        print("The name of the vechicle is ",self.name);
        print("The color of the vechicle is ",self.color);
        print("The price of the vechicle is ",self.price);
car1=vechicle();
car2=vechicle();
car1.display();
car2.display();