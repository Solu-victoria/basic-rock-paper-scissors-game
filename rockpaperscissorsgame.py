import random
print('''

█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█

''')

rock = ''' 
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
    '''
paper = '''

           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'    
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
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
    imageMoves = [rock, paper, scissors] #ascii art of moves

    if userMove not in possibleMoves:
        print('Invalid move! Please enter "rock", "paper", "scissors", or "quit".')
        continue
    print(imageMoves[possibleMoves.index(userMove)]) #print the corresponding image of the move (find the index of the user's move and use it to locate the corresponding image in imageMoves)

    computerMove = random.choice(possibleMoves)
    print(f"My move: {computerMove}", flush=True)
    print(imageMoves[possibleMoves.index(computerMove)])

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
        print(f"You lose! {scoreBoard}", flush=True)
