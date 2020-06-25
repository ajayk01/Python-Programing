while(True):
    i=int(input("Enter the divisor"));
    j=int(input("Enter the Dividend"));
    try:
        value = i/j;
        print("The answer is ",value);
        break;
    except (ZeroDivisionError):
        print("The dividend is zero");
    finally:
        if(j==0):
            print("Try Again")
        else:
            print("Thank you");