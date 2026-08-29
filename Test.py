import random

secret_number = random.randint(1, 50)
attempts = 5

print("I'm thinking of a number between 1 and 20. You have 5 attempts!")

for i in range(attempts):
    guess = int(input(f"Attempt {i+1}/5 - Enter your guess: "))
    
    if guess == secret_number:
        print("🎉 Correct! You won the game!")
        break
    elif guess < secret_number:
        print("💡 Hint: Too low!")
    else:
        print("💡 Hint: Too high!")
else:
    print(f"❌ Game over! The correct number was {secret_number}.")