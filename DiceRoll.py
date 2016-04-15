import random
#ask user for number of dice sides
side_of_dice=int(input("Please enter the number of sides on the dice:"))
#create variable to prime loop and continue loop if user wants
keep_going='y'
#Prevent uppercase y from continuing loop
while keep_going.lower() == 'y':
    number_rolled=random.randint(1,side_of_dice)
    print (number_rolled)
    keep_going=input("Do you want to roll again? Type y to roll again.")
    if keep_going.lower() =='y':
        side_of_dice=int(input("Please enter the number of sides on the dice:"))
