while(True):
     try:
         x = int(input("Please enter a number: "));
     except(ValueError):
         print("The entered number is not a integer");
     else:
         print("The entered number is a valid number");
         break;
     finally:
         print("Try again");