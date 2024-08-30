import random

# Constants
NUM_ROUNDS = 5  # You can adjust this value based on your requirement

def play_high_low_game():
    # Introduction
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    
    for round_number in range(1, NUM_ROUNDS + 1):
        # Generate random numbers
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        
        # Print the round information
        print(f"Round {round_number}")
        print(f"Your number is {your_number}")
        
        # Get user input
        user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Validate user input
        while user_guess not in ['higher', 'lower']:
            print("Please enter either 'higher' or 'lower'.")
            user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        
        # Determine if the guess is correct
        if (user_guess == 'higher' and your_number > computer_number) or \
           (user_guess == 'lower' and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        # Print score
        print(f"Your score is now {score}\n")
    
    # End of game messages
    print("Thanks for playing!")
    print(f"Your final score is {score}")

    # Conditional ending messages
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
play_high_low_game()
