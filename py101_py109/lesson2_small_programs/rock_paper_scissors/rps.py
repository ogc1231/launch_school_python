import random

def prompt(message):
    print(f'==> {message}')

def display_winner(user_hand, computer_hand):
    if (
        (user_hand == 'rock' and computer_hand == 'scissors')
        or (user_hand == 'scissors' and computer_hand == 'paper')
        or  (user_hand == 'paper' and computer_hand == 'rock')
    ):
        prompt(f'User wins: {user_hand} beats {computer_hand}')
    elif user_hand == computer_hand:
        prompt(f'Draw: {user_hand} is the same as {computer_hand}')
    else:
        prompt(f'Computer wins: {computer_hand} beats {user_hand}')

hand_list = ['rock', 'paper', 'scissors']

prompt('Welcome to RPS')
while True:
    user_hand = input(f'Choose {', '.join(hand_list)}: ')

    # validate user hand
    while True:
        if user_hand not in hand_list:
            user_hand = input('Invalid: choose rock, paper or scissors: ')
        else:
            break

    computer_hand = random.choice(hand_list)

    prompt(f'User chose: {user_hand}')
    prompt(f'Computer chose: {computer_hand}')

    display_winner(user_hand, computer_hand)

    ans = input('Play again? y/n ').lower()

    while True:
        if ans.startswith('n') or ans.startswith('y'):
            break
        prompt('Please enter "y" or "n".')
        ans = input().lower()
    
    if ans == 'n':
        prompt('Thanks for playing')
        break