while True:
 price = float(input("Enter shirt price: "))
 quantity = int(input("Enter quantity of items: "))

 total = price * quantity
 print("Your total is: " + str(total))

 cash = float(input("Enter payment amount: "))
 change = cash - total
 
 if cash < total:
     print("Insufficient amount")
 else:
     print("Your change is: " + str(change))

     choice = input("Do you want to make another transaction? y/n")
     if choice != 'y':
         break
