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

import random
game_images = [rock, paper, scissors]

your_input = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n")
int_your_input = int(your_input)

if int_your_input >= 3 or int_your_input < 0:
  print('You choose invalid number, you lose!')
else:
  print(game_images[int_your_input])

computer_input = int(random.randint(0, 2))
print(f"Computer choose: {computer_input}")
if computer_input == 0:
  print(rock)
elif computer_input == 1:
  print(paper)
else:
  print(scissors)


if int_your_input == computer_input - 1 or int_your_input == computer_input + 2:
  print("You lose!")
elif int_your_input == computer_input - 2 or int_your_input == computer_input + 1:
  print("You win!")
else:
  print("It's a draw!")