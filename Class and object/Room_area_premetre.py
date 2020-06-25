class Room:
    def __init__(self):
        self.square=int(input("Enter the side of the room"));
    def cal(self):
        self.premetre=4*self.square;
        self.area=self.square*self.square;
    def display(self):
        print("The area of the room is ",self.square);
        print("The premetre of the room is ",self.premetre);
r=Room();
r.cal();
r.display();