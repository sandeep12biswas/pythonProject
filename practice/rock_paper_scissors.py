"""
Rock Paper Scissors
Exercise 8 (and Solution)
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

ext = ""

while not ext.upper() == "EXIT":

    player1 = input("First player please enter any of the (Rock, Paper, Scissor)) :")
    player2 = input("Second player please enter any of the (Rock, Paper, Scissor)) :")

    option_lst = ["ROCK", "PAPER", "SCISSOR"]

    while not option_lst.__contains__(player1.upper()):
        player1 = input("Please enter any value from (Rock, Paper, Scissor)) (Player 1):")

    while not option_lst.__contains__(player2.upper()):
        player2 = input("Please enter any value from  (Rock, Paper, Scissor)) (Player 2):")

    if player1.upper() == player2.upper() :
        print(f"It's a tie, try again !!")
    elif player1.upper() == "ROCK" and player2.upper() == "SCISSOR" :
        print(f"Player 1 wins !!")
    elif player1 == "SCISSOR" and player2.upper() == "PAPER":
        print(f"Player 1 wins !!")
    elif player1.upper() == "PAPER" and player2.upper() == "ROCK":
        print(f"Player 1 wins !!")
    else:
        print(f"Player 2 wins !!")

    ext = input("If you want to exit the game then type exit :")