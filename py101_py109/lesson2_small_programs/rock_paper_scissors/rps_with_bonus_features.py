import random

def prompt(message):
    print(f'==> {message}')

def display_winner(user_hand, computer_hand):
    if (
        (user_hand == 'rock' and (computer_hand == 'scissors' or computer_hand == 'lizard'))
        or (user_hand == 'scissors' and (computer_hand == 'paper' or computer_hand == 'lizard'))
        or  (user_hand == 'paper' and (computer_hand == 'rock' or computer_hand == 'spock'))
        or (user_hand == 'spock' and (computer_hand == 'rock' or computer_hand == 'scissors'))
        or (user_hand == 'lizard' and (computer_hand == 'spock' or computer_hand == 'paper'))
    ):
        prompt(f'User wins: {user_hand} beats {computer_hand}')
    elif user_hand == computer_hand:
        prompt(f'Draw: {user_hand} is the same as {computer_hand}')
    else:
        prompt(f'Computer wins: {computer_hand} beats {user_hand}')

hand_list = ['rock', 'paper', 'scissors', 'spock', 'lizard']

prompt('Welcome to RPS')
while True:
    user_hand = input(f'Choose {', '.join(hand_list)}: ')

    # validate user hand
    while True:
        if user_hand not in hand_list:
            user_hand = input(f'Invalid: choose {', '.join(hand_list)} ')
        else:
            break

    computer_hand = random.choice(hand_list)

    prompt(f'User chose: {user_hand}')
    prompt(f'Computer chose: {computer_hand}')

    display_winner(user_hand, computer_hand)


    while True:
        ans = input('Play again? y/n ').lower()

        if ans.startswith('n') or ans.startswith('y'):
            break
        else:
            prompt('Please enter "y" or "n".')
    
    if ans[0] == 'n':
        prompt('Thanks for playing')
        break