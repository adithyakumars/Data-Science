# # n=int(input("Enter the water u need:"))
# response=input("What type of water u need:\n1.Hot_water__(h) \n2.Cold_water__(c) \n3.Normal_water__(n):").lower()
# valid_response=['h','c','n']
# response=response.lower()
# cold=100
# hot=100
# normal=100
# count=0
# if response=='h':
#     # print("The Hot water u got:",n)
#     hot_out=int(input("The Hot Water u need:"))
#     if hot_out%10!=0:
#         print("The Hot water u got",hot_out)
#     elif hot_out>hot[hot]:
#         print("The hot Water Empty or refillling in tank")
#     else:
#         hot_out=hot_out-hot
#         print("The Hot water left Balance in Tank:",hot_out)
    
# if response=='c':
#     print("The Cold water u got:",n)
#     print("The Cold water left in balance:",cold-n)

# elif response=='n':
#     print("The Normal water u got:",n)
#     print("The normal water left balance in tank",normal-n)
    
# else:
#     print("The water is refilling or Empty in tank")

# Define the initial water levels in liters
hot = 100
cold = 100
normal = 100

# Define the minimum water level to trigger refilling
min_level = 4

# Define the amount of water dispensed per request in liters
dispense_amount = 4

# Define a function to dispense water of a given type
def dispense_water(water_type):
    # Use the global variables for water levels
    global hot, cold, normal
    
    # Check which water type is requested
    if water_type == "hot":
        # Check if there is enough hot water
        if hot >= dispense_amount:
            # Dispense hot water
            print("Dispensing hot water...")
            # Update the hot water level
            hot -= dispense_amount
            # Print the remaining hot water level
            print(f"Remaining hot water: {hot} liters")
        else:
            # Print a message that the hot water is empty or refilling
            print("The hot water is empty or refilling. Please wait.")
    elif water_type == "cold":
        # Check if there is enough cold water
        if cold >= dispense_amount:
            # Dispense cold water
            print("Dispensing cold water...")
            # Update the cold water level
            cold -= dispense_amount
            # Print the remaining cold water level
            print(f"Remaining cold water: {cold} liters")
        else:
            # Print a message that the cold water is empty or refilling
            print("The cold water is empty or refilling. Please wait.")
    elif water_type == "normal":
        # Check if there is enough normal water
        if normal >= dispense_amount:
            # Dispense normal water
            print("Dispensing normal water...")
            # Update the normal water level
            normal -= dispense_amount
            # Print the remaining normal water level
            print(f"Remaining normal water: {normal} liters")
        else:
            # Print a message that the normal water is empty or refilling
            print("The normal water is empty or refilling. Please wait.")
    else:
        # Print a message that the water type is invalid
        print("Invalid water type. Please choose hot, cold, or normal.")

# Define a function to refill water of a given type
def refill_water(water_type):
    # Use the global variables for water levels
    global hot, cold, normal
    
    # Check which water type needs refilling
    if water_type == "hot":
        # Refill hot water to the maximum level
        print("Refilling hot water...")
        hot = 10
        # Print the refilled hot water level
        print(f"Refilled hot water: {hot} liters")
    elif water_type == "cold":
        # Refill cold water to the maximum level
        print("Refilling cold water...")
        cold = 10
        # Print the refilled cold water level
        print(f"Refilled cold water: {cold} liters")
    elif water_type == "normal":
        # Refill normal water to the maximum level
        print("Refilling normal water...")
        normal = 10
        # Print the refilled normal water level
        print(f"Refilled normal water: {normal} liters")
    else:
        # Print a message that the water type is invalid
        print("Invalid water type. Please choose hot, cold, or normal.")

# Define a loop to ask the user for water type
while True:
    # Ask the user for water type
    water_type = input("What type of water do you need? (hot, cold, normal, or quit): ").lower()
    
    # Check if the user wants to quit
    if water_type == "quit":
        # Break the loop
        break
    
    # Dispense water of the requested type
    dispense_water(water_type)
    
    # Check if any water type needs refilling
    if hot <= min_level:
        # Refill hot water
        refill_water("hot")
    if cold <= min_level:
        # Refill cold water
        refill_water("cold")
    if normal <= min_level:
        # Refill normal water
        refill_water("normal")
