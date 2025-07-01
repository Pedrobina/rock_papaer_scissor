import random

# Print multiline instruction
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")


options = ["rock", "paper", "scissors"]
keep_playing = True
while keep_playing:

    print('Enter your choice \n'
          + "1 - Rock \n"
          + "2 - Paper \n"
          + "3 - Scissors \n")
    computer_option = random.choice(options)
    user_option = str.lower(input("Chose your hand \n"))
    print(f"User ({user_option}) vs Computer ( {computer_option} )")
    if user_option == computer_option:
        print("DRAW")
    elif user_option == "rock":
        if computer_option == "paper":
            print("<== Computer wins! ==>")
        else:
            print("<== User wins! ==>")

    elif user_option == "paper":
        if computer_option == "scissors":
            print("<== Computer wins! ==>")
        else:
            print("<== User wins! ==>")

    elif user_option == "scissors":
        if computer_option == "rock":
            print("<== Computer wins! ==>")
        else:
            print("<== User wins! ==>")

    user_play = str.lower(input("\nPlay again? Yes or No\n"))
    if user_play == "no":
        keep_playing = False