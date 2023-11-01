#Joshua Hall PIRATE GAME!
import random

crew_size = 30
officers = 5
cannons = 12
morale = 5
treasure = 0

captain_name = input("Enter the captain's name:")

while morale > 0:
    print("Captain", captain_name, "your crew's status is :",)
    print("Crew size:", str(crew_size))
  
    print("Officers:", str(officers))
    print("Cannons:", str(cannons))
    print("Morale:", str(morale))
    print("Treasure:",str(treasure))
  
    print("What would you like to do?")
  
    print("1. Attack a town")
    print("2. Attack a ship")
    print("3.Bury the treasure")
    print("4. Divide the treasure")
  
    choice = input("Enter your choice(1/2/3/4): ")
  
    if choice == "1":
      morale += 1 
      town_type = random.choice(["American", "English", "French", "Spanish"])
      treasure_gained = random.randint(1,100)   
      treasure += treasure_gained
      print("You attacked a", town_type,"town and gained", str(treasure_gained), "treasure.")

    elif choice == "2":
      morale -= 1 
      ship_type = random.choice(["American", "English", "French", "Spanish"])
      treasure_gained = random.randint(1,100)
      treasure += treasure_gained
      print("You attacked a", ship_type, "ship and gained", str(treasure_gained), "treasure.")

    elif choice == "3":
      morale = 2
      treasure = 0
      print("You buried the treasure and your crew's morale is now 2")

    elif choice == "4":
      total_shares = crew_size + (1.5 * officers) + 2
      crew_share = int(treasure // total_shares)
      officers_share =int(1.5 * crew_share) 
      captain_share = int(2 * crew_share)
      print("You divided the treasure:")
      print("Crew members each get", str(crew_share), "shares.")
      print("Officers each get", str(officers_share),"shares.")
      print("The captain gets", str(captain_share), "shares.")

    else: 
      print("Invalid choice, please select 1/2/3/4.")

    if morale <= 0:
      print("Game over, your crew has mutinied and marooned you Captain", captain_name, "!")
      break

  
  
  









