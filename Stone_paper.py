import random
class Stone_paper:
  def stone_paper(self):
    options = ["stone", "paper", "scissor"]
    attempt = 0 
    print("-------------Welcome to the Stone, Paper, Scissor Game!-------------")
    while (True):
      user_choice = input("Enter your choice (stone, paper, scissor): ").lower()
      computer_choice = random.choice(options)
      if (computer_choice == user_choice):
        print(f"It's a tie! Both chose {user_choice}.")
        attempt += 1
      elif (
           computer_choice=="stone" and user_choice=="paper" 
            or computer_choice=="paper" and user_choice=="scissor"
            or computer_choice=="scissor" and user_choice=="stone"
            ):
        attempt += 1
        print(f"You win! {user_choice} beats {computer_choice} in {attempt} attempts.")
        break
      else:
        attempt += 1
        print(f"You lose! {computer_choice} beats {user_choice}. Try again.")
    print("Game Over! Thanks for playing.")
st = Stone_paper()
st.stone_paper()