import random

def number_guessing_game():
  """
  This function implements a number guessing game.
  """

  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)

  # Set the number of guesses allowed
  num_guesses = 7

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  # Start the guessing loop
  for guess_count in range(num_guesses):
    print(f"You have {num_guesses - guess_count} guesses left.")
    try:
      guess = int(input("Enter your guess: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    # Check if the guess is correct
    if guess == secret_number:
      print(f"Congratulations! You guessed the number {secret_number} in {guess_count + 1} tries.")
      return

    # Provide feedback on the guess
    elif guess < secret_number:
      print("Too low! Try again.")
    else:
      print("Too high! Try again.")

  # If the player runs out of guesses
  print(f"Sorry, you ran out of guesses. The number was {secret_number}.")

# Start the game
number_guessing_game()