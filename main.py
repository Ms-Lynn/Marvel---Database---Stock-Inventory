#------------------------------------------------------------------------------
# Title: Example of a Nested List Comprehension
# Coder: Ms. Lynn
# Version: 001
#------------------------------------------------------------------------------
'''Example Code - Using Databases for game.'''
#------------------------------------------------------------------------------
# Imports and Global Variables ------------------------------------------------
# Database
Marvel_Superheros = {
  "Spiderman" : {
           "Name" : "Peter Parker", 
           "Weapons" : ["Webbing"],
           "Super Powers" : ["Speed", "Reflexes",
                             "Spider-Sense"], 
           "Weaknesses" : ["Ethyl Chloride Pesticide"] },
  "Thing" : {
           "Name": "Ben Grimm",
           "Weapons": ["Fists"],
           "Powers": ["Immortal", "Super Strength",
                      "Enhanced Lung Capacity", "Good Fighter"],
         "Weakness": [None] },  
  "Baby_Groot" : {
           "Name" : "Baby Groot",
           "Weapons" : ["Strong Branches"],
           "Super Powers" : ["Self-Healing", "Controls Plant", 
                            "Immune to Fire"],
           "Weaknesses" : ["Termites"] },
  "Ironman" : {
           "Name" : "Tony Stark",
           "Weapons" : ["Ironman Suit", "AI", "Blasters"], 
           "Superpowers" : ["Smart", "Rich"],
           "Weaknesses" : ["Arrogant"] },
  "Deadpool" : {
           "Name" : "Wade Wilson",
           "Weapons" : ["Katanas", "Grenade", "Gun"],
           "Super Powers" : ["Speed", "Bullet Proof",
                             "Self-Healing"],
           "Weaknesses" : ["Women", "Ugly"] },
  "Antman" : {
           "Name" : "Scott Lang",
           "Weapons" : ["Antman Suit"],
           "Super Powers" : ["Communication with Insects", 
                             "Sound Amplification"],
           "Weaknesses" : ["Lacks Ability Control"]}
}

Main_Character = "Spiderman"   #default character
Inventory = []

# Functions ------------------------------------------------------------------
def Choose_Character():
  global Main_Character
  thinking = True
  while thinking:  
    print(f"Choose one of the following character: ")
    for characters in Marvel_Superheros:
      print(f"-{characters}")
    hero = input("Hero Choice: " )
    if hero in Marvel_Superheros.keys():
      Main_Character = hero
      thinking = False
    else: 
      print(f"Invalid Character Choice")


def Get_Weapons():
  global Inventory
  print(f"You will have access to the following Weapons: ")
  for weapon in Marvel_Superheros[Main_Character]["Weapons"]:
    print(f"-{weapon}")
    Inventory.append(weapon)

  
# Main -----------------------------------------------------------------------
print(f"Welcome to my Game!")
# Have user pick a charater to play the game with
Choose_Character()
print('\n')
# Print out main character's information
print(f"Your character is {Main_Character}.")
print(f"Your character's real name is {Marvel_Superheros[Main_Character]['Name']}.")

# Stock the main characters inventory
Get_Weapons()
print('\n')
# Print characters current inventory
print(f"Current Inventory: ")
for item in Inventory:
  print(f"-{item}")


