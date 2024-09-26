class Fighter:
    def __init__(self, name, health, strength, speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.speed = speed

    def __repr__(self):
        return f"{self.name} (Health: {self.health}, Strength: {self.strength}, Speed: {self.speed})"

    def attack(self, opponent):
        opponent.health -= self.strength
        return f"{self.name} attacks {opponent.name} and deals {self.strength} damage!"

# Creating fighter instances
fighter1 = Fighter("Warrior", health=100, strength=15, speed=50)
fighter2 = Fighter("Mage", health=80, strength=20, speed=40)
fighter3 = Fighter("Rogue", health=90, strength=10, speed=70)
fighter4 = Fighter("Knight", health=120, strength=12, speed=60)

fighter_list = [fighter1, fighter2, fighter3, fighter4]

# Defining function for player participation: players expected between 1 or 2
def players():
    while True:
        num_of_players = int(input("How many players are playing? (1 or 2): "))
        if num_of_players in [1, 2]:
            return num_of_players
        else:
            print("Please enter 1 or 2.")

def welcome_prompt():
    print("⚔️ Welcome to the Battle Arena! ⚔️")
    print("Fight solo or challenge a friend. Only the strongest will survive!")

def show_fighters(fighters):
    print("Choose your fighter:")
    for i, fighter in enumerate(fighters, start=1):
        print(f"{i}. {fighter}")

def pick_fighter(fighters):
    choice = int(input("Enter the number of your choice: ")) - 1
    if 0 <= choice < len(fighters):
        return fighters[choice]
    else:
        print("Invalid choice!")
        return pick_fighter(fighters)




while True:
    # Game introductions
    welcome_prompt()

    # Prompt user to provide number of users
    number_of_players = players()

    # Placeholder for players
    players = []

    # for loop to allow player/(s) to select a fighter
    for i in range(1,number_of_players + 1):
        # Notify the current player
        print(f"Player {i}")

        # Show fighters and allow the user to pick one
        show_fighters(fighter_list)

        # Prompt users to select a fighter from 1 and including 4
        user_fighter = pick_fighter(fighter_list)
        print(f"You selected: {user_fighter}")
