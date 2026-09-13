import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou choso {user_action}, computer chose {computer_action}.\n")
    
    
    if user_action == computer_action:
        print(f"Both players selected {user_action}. Its a tie")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scissors! You win")
        else:
            print("paper covers rock! You lose")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! You win!")
        else:
            print("scissors cuts paper! yo lose")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win")
        else:
            print("Rock smashes scissors! you lose")
            
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
    
    

        
            
            