import time


def start(name: str) -> bool:
    for i in range(1, 100):
        print()
    print("In a world, far, far away...")
    time.sleep(3)
    print("A hero emerged. His name, you ask?\nIt was", name, ".")
    time.sleep(3)
    print("In a world where people were being oppressed by governments, he was the hero people needed.")
    time.sleep(2)
    print("If you haven\'t noticed, YOU are that hero. Yes YOU,", name)
    time.sleep(2)
    print("You need to train for what is right!")
    time.sleep(2)
    print("You need to fight for freedom!")
    return True


def intro(name: str):
    willHelp = None
    print("Welcome to SlavVille!")
    time.sleep(2)
    print(f"Villager: We have heard many, great, great story\'s about you, {name}...")
    print("Villager: Will you support our village against the oppressors?")
    while type(willHelp) is not bool:
        willHelp = input("True or False? ")
    willHelp = bool(willHelp)
    if not willHelp:
        print("Tanks start rolling in.")
        print("You tried to defend yourself, buy the tanks and soldiers are way stronger than you.")
        print("Maybe try helping next time.")
        exit(3)
    elif willHelp:
        print("Villager: We are so grateful for your help! We will support you with weapons and armor.")
