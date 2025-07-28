import random
class Number_guess:
  def guess_number(self):
    attempts = 0
    computer_guess = random.randint(1, 100)
    print("-------------Welcome to the Number Guessing Game!-------------")
    while True:
      number = int(input("Guess a number between 1 and 100: "))
      if number == computer_guess:
        print(f"Congratulations! You've guessed the number {computer_guess} correctly in {attempts + 1} attempts.")
        break
      elif number < computer_guess:
        print("Too low! Try again.")
        attempts += 1
      else:
        print("Too high! Try again.")
        attempts += 1
    print("Game Over! Thanks for playing.")
ng = Number_guess()
ng.guess_number()
      