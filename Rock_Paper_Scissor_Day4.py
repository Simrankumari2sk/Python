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

image = [rock,paper,scissors]

user_choice = int(input("What do you choose to play with the computer ? Select 0 for Rock, 1 for Paper and 2 for scissors"))

if user_choice >=0 and user_choice <=2:
    print(image[user_choice])

computer_choice = random.randint(a= 0, b= 2)
print("Computer choose: ")
print(image[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("Invalid Input!")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You Win!")
else:
    print("It's a draw")