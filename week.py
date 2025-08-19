# WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc

a = int(input("enter day no. : sunday = 1 ......."))
if a<=1:
    if a==1:
        print("sunday")
    elif a==2:
        print("monday")
    elif a==3:
        print("tuesday")
    elif a==4:
        print("wednesday")
    elif a==5:
        print("thursday")
    elif a==6:
        print("friday")
    elif a==7:
        print("saturday")
else:
    print("enter a valid number more than zero ")



#match day:
  #  case 1:
  #  print("Sunday")
   # case 2:
      #  print("Monday")
 #   case 3:
     #   print("Tuesday")
   # case 4:
     #   print("Wednesday")
  #  case 5:
     #   print("Thursday")
  #  case 6:
      #  print("Friday")
  #  case 7:
      #  print("Saturday")
  #  case _:
     #   print("Invalid input! Please enter a number between 1 and 7.")
