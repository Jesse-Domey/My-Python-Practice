#this program asks the kind of car a user wants and returns a message to the customer

#ask the name of the customer and greet them
name = input("Please enter your name!: ")
print(f"Hello, {name.title()}")

#action when customer meets requirement
#ask customer about car information
def car ():
    car = input("What type of car would you want to rent today?: ")
    color = input("Enter color of car: ") 
    print(f"Order Summary\n{car.title()}\n{color.title()}")


#let user confirm their order or make changes to it  
def confirmation(): 
    order_confirmation = input("Press y to confirm order or n to make changes: ")
    if order_confirmation == 'y':
        print("Your order is being processed")
        print("Thank you for your order")
    if order_confirmation == 'n':
        car()
        confirmation()
    

#action when a customer doesn't meet requirement for renting a car
def quit():
    quit = input("Press q to exit: ")
    if quit == 'q':
        print("\nexit succesful")
        print("\nThank You")

        
    

#ask customer their age and if they have a license, customer must be at least 21 years  and must have a to rent a car
age = input("How old are you? ")
age = int(age)
license_status = input("Do you have a license? ")
#consumer passes rental requirement, proceed to give order details and confirm
if age >= 21:
    if license_status == 'yes':
        print(f"\nYou are good to go {name.title()}")
        car()
        confirmation()

        
#consumer doesn't meet order requirement, exit order page       
if age < 21:
    if license_status == 'yes':
        print(f"\nSorry, you are not old enough to rent a car {name.title()}")
        quit()
if age >= 21:
    if license_status != 'yes':
        print(f"\nSorry you need a license to rent a car {name.title()}")
        quit()
if age < 21:
    if license_status != 'yes':
        print(f"\nSorry {name.title()}, you are not eligible to rent a car")
        quit()
        