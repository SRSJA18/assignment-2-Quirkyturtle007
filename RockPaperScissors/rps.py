# Please reference the included PDF for complete instructions.
#
# You can create your table (from the instructions) using a doc or spreadsheet.
#
# Advanced students should attempt to implement
# Rock, Paper, Scissors, Lizard, Spock using 3 or 4 players instead (This is much harder.)
# 1. Ask player 1 for their move.
player1=input("player1? ")

# 2. Check if player 1's move is valid.

# 3. Ask player 2 for their move.
player2=input("player2? ")
# 4. Check if player 1's move is valid.

# 5. Print out the winner or 'tie'
if player1==player2:
    print("Tie...")
elif player1=="rock":
    if player2=="scissors":
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
elif player1=="paper":
     if player2=="rock":
        print("Player 1 Wins!")
     else:
        print("Player 2 Wins!")
elif player1=="scissors":
    if player2=="rock":
        print("Player 2 Wins")
    else:
        print("Player 1 Wins!")
else:
    print("Not Real Move")