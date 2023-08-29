from getpass import getpass

print("Welcome to Rock, Paper, Scissors.")
print("Each player select their move. R, P, or S.\nR for Rock, P for Paper, S for Scissors.\n")

player1name = input("What is Player 1's name? ")
player2name = input("What is Player 2's name? ")

player_scores = {player1name: 0, player2name: 0}
moves = {"R": "Rock", "P": "Paper", "S": "Scissors"}

while True:
    player1move = getpass(f"{player1name}'s move: ").upper()
    player2move = getpass(f"{player2name}'s move: ").upper()

    if player1move in moves and player2move in moves:
        if player1move == player2move:
            print(f"You both picked {moves[player1move]}. This game is a draw.")
        elif (player1move == "R" and player2move == "S") or \
             (player1move == "S" and player2move == "P") or \
             (player1move == "P" and player2move == "R"):
            print(f"{player1name} wins! {moves[player1move]} defeats {moves[player2move]}.")
            player_scores[player1name] += 1
        else:
            print(f"{player2name} wins! {moves[player2move]} defeats {moves[player1move]}.")
            player_scores[player2name] += 1
    else:
        print("Invalid Move.")

    print()
    print(f"{player1name}: {player_scores[player1name]}   {player2name}: {player_scores[player2name]}\n")

    ready_play = input("Play again? Y or N ").upper()
    if ready_play != "Y":
        break

print("Thank you for playing. Come back again.")
