from typing import final


def main():
    print("Hello there")
    player_name = input("What's your name? ")
    print("Your name is {}. You are a {}" .format(player_name, "knight"))
    start_adventure()

def start_adventure():
    print("You entered a room and you see a red door to your left and blue door to your right.")
    door_picked= input("Please pick a door: ").lower()
    if door_picked.lower() == "red":
        red_door_room()
    elif door_picked.lower() == "blue":
        blue_door_room()
    else:
        print("Sorry, you have to pick one ")
        return 

def red_door_room():
    print("You see a great red dragon that breathes fire")
    print("It turns around and meets your eyes")
    print("Do you flee for your life or do you stay? ")

    next_move = input("Flee or stay? ")
    if next_move.lower() == "flee":
        start_adventure()
    else:
        you_died("It eats you. Well, that was tasty!")

def you_died(why):
    print("{}, Good job!".format(why))
    exit(0)
    
def blue_door_room():
    print("You enter the room and see a treasure chest to your left and a sleeping guard in front of a door to your right.")
    print("What would you like to do next? 1: Open the chest? or 2: Check out the door?")
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    action = input("1 or 2? ")
    if action == "1":
        print("Let's see what's in here...")
        print("The chest creaks open and the guard is still sleeping. Wow, that's one heavy sleeper!")
        print("you find some")
        for treasure in treasure_chest:
            print(treasure)
        print("Take all {} treasures, press 1" .format(len(treasure_chest)))
        print("Leave it, press 2")
        treasure_choice = input("1 or 2? ")

        if treasure_choice == "1":
            treasure_chest.remove("sword")
            print("You take the shinier sword from the treasure chest and drop your crappy sword in the empty treasure chest.")
            temp_treasure_list = treasure_chest[:]
            treasure_contents = ", ".join(treasure_chest)
            print("You also recieve {}" .format(treasure_contents))
            
            for treasure in temp_treasure_list:
                treasure_chest.remove(treasure)
            treasure_chest. append("crappy sword")
            print("Lets go past the guard and towards freedom")
        elif treasure_choice == "2":
            print("It will still be here (hopefully) after I get past this guard")
        
    elif action == "2": 
        print("The guard is more interesting, let's go that way!")
    else:
        print("Not sure what you picked there, let's poke the guard, seems fun!")
    guard()

def guard():
    actions_dict = {"check": "You see the guard still sleeping, you need to get to that door on the right of him. What are you waiting for?",
                    "sneak": "You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and slip out.",
                    "attack": "You run towards the guard and wack him with the hilt of your shiny sword, but it wasn't hard enough."}
    while True:
        action = input("What do you do? [attack | check | sneak] ").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You slipped through the door before the guard woke up")
                print("You are now outside and freed! Horray!")
                return
            elif action == "attack":
                you_died("Guard woke up with a grunt, reached for his dagger and before you know it, the world goes dark and you died")




        



main()
