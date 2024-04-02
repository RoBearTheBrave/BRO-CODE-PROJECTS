
food_response = input("Would you like food? (Y/N): ")
food_response = food_response.upper()
if food_response == "Y": #use == for comparison 
    print("Have some food!")
else:
    print("No food for you!")


name_response = input("Enter your name: ")

if name_response == "":
    print("You did not type in your name!")
else: 
    print(f"Hello {name_response}")