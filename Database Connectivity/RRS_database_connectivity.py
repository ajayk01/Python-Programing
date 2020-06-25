import MySQLdb
mydb = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="", db="RRS")
cursor1 = mydb.cursor()
while(True):
  ch=int(input("1.To display the tickets\n2.To book a new ticket\n3.Delete a ticket\n4.Update\n5.Exit"));
  if(ch==2):
    n=int(input("1.To book a one ticket\n 2. To book a More than one ticket"));
    if(n==1):
        Name=input("Enter the name of the passenger");
        age=input("Enter the age of the passenger");
        Source=input("Enter the source station");
        des=input("Enter the source station");
        date=input("Enter the age of the journey");
        cursor1.execute("""INSERT INTO Reser(Name,Age,source,des,date) VALUES (%s, %s, %s, %s, %s)""" , (Name,age,Source,des,date));
        mydb.commit();
    else:
        n=int(input("Enter the no of passengers"));
        if(n>6):
            print("You can book upto 6 passengers only");
        else:
            for i in range(0,n):
                print("Enter the details for :",i+1," passenger");
                Name=input("Enter the name of the passenger");
                age=input("Enter the age of the passenger");
                Source=input("Enter the source station");
                des=input("Enter the source station");
                date=input("Enter the age of the journey");
                cursor1.execute("""INSERT INTO Reser(Name,Age,source,des,date) VALUES (%s, %s, %s, %s, %s)""" , (Name,age,Source,des,date));
                mydb.commit()
  elif(ch==1):
      Name =input("Enter the name of the passenger in the ticket");
      age =input("Enter the age of the passenger in the ticket");
      cursor1.execute("""SELECT * FROM Reser WHERE Name=%s AND Age=%s""",(Name,age))
      results=cursor1.fetchall();
      for row in results:
          print(row);
  elif(ch==5):
      print("Thank you");
      break;
  elif(ch==3):
      Name =input("Enter the name of the passenger in the ticket to be cancelled");
      age =input("Enter the age of the passenger in the ticket to be deleted ");
      cursor1.execute("""DELETE  FROM Reser WHERE Name=%s AND Age=%s""",(Name,age));
      mydb.commit();
  elif(ch==4):
      Name =input("Enter the name of the passenger in the ticket to be updated :");
      age =input("Enter the age of the passenger in the ticket to be updated :");
      n=int(input("Enter the Column to be updated 1.Name \n 2.Age \n 3.Source station \n 4.destination station \n 5. Date" ));
      if(n==1):
          name1=input("Enter the new name");
          cursor1.execute("""UPDATE Reser SET  Name=%s WHERE Name=%s AND Age=%s""",(name1,Name,age));
          mydb.commit();
      elif(n==2):
          age1=input("Enter the age to be updated");
          cursor1.execute("""UPDATE Reser SET  Age=%s WHERE Name=%s AND Age=%s""",(age1,Name,age));
          mydb.commit();
      elif(n==3):
          s1=input("Enter the sourse station to be updated");
          cursor1.execute("""UPDATE Reser SET  source=%s WHERE Name=%s AND Age=%s""",(s1,Name,age));
          mydb.commit();
      elif(n==4):
          d1=input("Enter the destination station  to be updated");
          cursor1.execute("""UPDATE Reser SET  des=%s WHERE Name=%s AND Age=%s""",(d1,Name,age));
          mydb.commit();
      elif(n==5):
          d1=input("Enter the date to be updated");
          cursor1.execute("""UPDATE Reser SET  date=%s WHERE Name=%s AND Age=%s""",(d1,Name,age));
          mydb.commit();
mydb.close();
        
