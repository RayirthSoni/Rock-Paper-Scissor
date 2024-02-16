import random
from fuzzywuzzy import process

def start_game():
    possible_moves = ['rock', 'paper', 'scissors']
    num_rounds = int(input('Enter number of rounds you want to play: '))
    user_points = 0
    computer_points = 0

    for i in range(num_rounds):
        user_move = input('Enter your move (rock, paper, or scissors): ').lower()
        # Perform fuzzy matching to find the closest valid move
        user_move, _ = process.extractOne(user_move, possible_moves)
        
        computer_move = random.choice(possible_moves)

        print(f'Round {i + 1}: You chose {user_move}, Computer chose {computer_move}')

        if (
            (user_move == 'rock' and computer_move == 'scissors') or
            (user_move == 'paper' and computer_move == 'rock') or
            (user_move == 'scissors' and computer_move == 'paper')
        ):
            user_points += 1
            print('You win this round!')
        elif (
            (computer_move == 'rock' and user_move == 'scissors') or
            (computer_move == 'paper' and user_move == 'rock') or
            (computer_move == 'scissors' and user_move == 'paper')
        ):
            computer_points += 1
            print('Computer wins this round!')
        else:
            print("It's a draw!")

    print(f'All {num_rounds} rounds finished !')
    print(f'Your Points = {user_points}')
    print(f'Computer Points = {computer_points}')

    if user_points > computer_points:
        print('You win the game!!')
    elif user_points < computer_points:
        print('Computer wins the game!!')
    else:
        print("It's a draw!")

if __name__ == "__main__":
    start_game()
