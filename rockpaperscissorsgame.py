import random

computerWins = 0
userWins = 0
ties = 0
winningMoves = {
    'rock' : 'scissors',
    'paper' : 'rock',
    'scissors' : 'paper'
}

scoreBoard = f"\nScoreboard:\nComputer: {computerWins}\t\t\tYou: {userWins}\t\t\tTies: {ties}"
while True:
    userMove = input('Please make your move: "rock", "paper", "scissors" or enter "quit" to exit the game>>>')
    if userMove.lower() == 'quit':
        while True:
            userQuit = input(f'Are you sure you want to quit? (Please enter "yes" or "no")>>>')
            if userQuit.lower() != 'yes' and userQuit.lower() != 'no':
                print('Invalid input! (Please enter "yes" or "no")')
                continue
            break
        if userQuit.lower() == 'yes':
            print(f"Thanks for playing! {scoreBoard}")
            break
        elif userQuit.lower() == 'no':
            continue  # Go back to the beginning of the main loop (asking for a new move)

    possibleMoves = ['rock', 'paper', 'scissors']
    if userMove not in possibleMoves:
        print('Invalid move! Please enter "rock", "paper", "scissors", or "quit".')
        continue

    computerMove = random.choice(possibleMoves)
    print(f"My move: {computerMove}", flush=True)

    if userMove.lower() == computerMove:
        ties += 1
        scoreBoard = f"\nScoreboard:\nComputer: {computerWins}\t\t\tYou: {userWins}\t\t\tTies: {ties}"
        print(f"I'ts a tie! {scoreBoard}", flush=True)
        
    elif winningMoves[userMove.lower()]  == computerMove:
        userWins += 1
        scoreBoard = f"\nScoreboard:\nComputer: {computerWins}\t\t\tYou: {userWins}\t\t\tTies: {ties}"
        print(f"You win! {scoreBoard}", flush=True)
        
    else:
        computerWins += 1
        scoreBoard = f"\nScoreboard:\nComputer: {computerWins}\t\t\tYou: {userWins}\t\t\tTies: {ties}"
        print(f"Computer wins! {scoreBoard}", flush=True)
