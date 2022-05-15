# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.




def shopping_cart(cart1 = {}):
    running = True
    print("Welcome to Bruce's Grocery! ")
    while running == True:
        # clear_output()
        
        ask = input("What would you like to do? Please enter 'add', 'delete', 'see cart', or 'quit'. ").lower()
        while ask not in {'add', 'delete', 'see cart', 'quit'}:
            ask = input("Response invalid. Please enter 'add', 'delete', 'see cart', or 'quit'.")
        if ask == 'quit':
            running = False
            print("Thank you for shopping at Bruce's Grocery!\n")      
            break
        elif ask == 'add':
            item = input("What would you like to add to your cart? ").title()
            price = float(input("What is the individual price of the item selected? "))
            cart1[item] = price 
            if ask:
                print(f"{item} has been added to your cart.")

        elif ask == 'delete':
            remove = input("What item would you like to delete? ").title()
            if remove in cart1: 
                del cart1[remove]
                print(f"{remove} has been deleted from your cart.")
            else:
                print("That item is not in your cart.")
        
        elif ask == 'see cart':
            if cart1:
                for item, price in cart1.items():
                    print(f"{item} x ${price}")
            else:
                print("Your cart is currently empty.")


    total_price = 0
       

    print("Here is your receipt:\n")


    for item, price in cart1.items():
        total_price += price  
        print(f"{item} x ${price}")
        

    
    print(f"Your total is ${total_price:.2f}.\n")    
    print("Have a wonderful day! ")

    


            
shopping_cart()


