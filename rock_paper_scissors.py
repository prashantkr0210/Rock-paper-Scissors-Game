import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

should_continue = True

def should_conti():
    user_input = input("Do you want to continue 'yes' or 'no': ").lower()
    if user_input == "no":
        should_continue = False

while should_continue:
    a = int(input(" Type 0 for Rock, 1 for Paper, 2 for Scissors  "))
    random_int = random.randint(0, 2)
    if a == 0:
        print(" \nYou Choose\n")
        print(rock)

        if random_int == 0:
            print(" \nComputer Choose\n")
            print(rock)
            print("\nIt's a Draw\n")
            should_conti()
        elif random_int == 1:
            print(" \nComputer Choose\n")
            print(paper)
            print(" \nSorry You lost\n")
            should_conti()
        else:
            print(" \nComputer Choose\n")
            print(scissors)
            print(" \nCongrats You Won\n")
            should_conti()

    elif a == 1:
        print(" \nYou Choose\n")
        print(paper)

        if random_int == 0:
            print(" \nComputer Choose\n")
            print(rock)
            print("\nCongrats You Won\n")
            should_conti()
        elif random_int == 1:
            print(" \nComputer Choose\n")
            print(paper)
            print(" \nIt's a Draw\n")
            should_conti()
        else:
            print(" \nComputer Choose\n")
            print(scissors)
            print(" \nSorry you lost\n")
            should_conti()
    elif a == 2:
        print(" \nYou Choose\n")
        print(scissors)

        if random_int == 0:
            print(" \nComputer Choose\n")
            print(rock)
            print("\nSorry You Lost\n")
            should_conti()
        elif random_int == 1:
            print(" \nComputer Choose\n")
            print(paper)
            print(" \nCongrats You Won\n")
            should_conti()
        else:
            print(" \nComputer Choose\n")
            print(scissors)
            print(" \nIt's a Draw\n")
            should_conti()
    else:
        print("\nInvalid input Run Again and put correct input\n")
        should_conti()



