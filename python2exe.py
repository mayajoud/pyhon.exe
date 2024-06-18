import random

def get_user_choice():
    choice = input("Choose: Rock, Paper, or Scissors: ")
    return choice.lower()

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice = random.choice(choices)
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You won!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer's choice:", computer_choice)
    print(determine_winner(user_choice, computer_choice))

# Main code
while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
