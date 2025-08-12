import random

def prompt(message):
    print(f'==> {message}')

def change_hand_to_full_name(hand):
    mapping = {
        'r': 'rock',
        'p': 'paper',
        'sc': 'scissors',
        'sp': 'spock',
        'l': 'lizard',
    }
    return mapping.get(hand, hand)

# Rules: each key beats the set of values
WINNING_COMBOS = {
    'rock': {'scissors', 'lizard'},
    'scissors': {'paper', 'lizard'},
    'paper': {'rock', 'spock'},
    'spock': {'rock', 'scissors'},
    'lizard': {'spock', 'paper'},
}

def display_winner(
        user_hand, computer_hand, user_wins, computer_wins, total_games_played
    ):
    user_hand = change_hand_to_full_name(user_hand)
    computer_hand = change_hand_to_full_name(computer_hand)

    if user_hand == computer_hand:
        prompt(f'Draw: {user_hand} is the same as {computer_hand}')
    elif computer_hand in WINNING_COMBOS.get(user_hand, set()):
        prompt(f'User wins: {user_hand} beats {computer_hand}')
        user_wins += 1
    else:
        prompt(f'Computer wins: {computer_hand} beats {user_hand}')
        computer_wins += 1

    total_games_played += 1

    return user_wins, computer_wins, total_games_played

def main():
    hand_list = [
        'rock', 
        'paper', 
        'scissors', 
        'spock', 
        'lizard', 
        'r', 
        'p', 
        'sc', 
        'sp', 
        'l'
    ]

    prompt('Welcome to RPS')

    while True:
        total_games_played = 0
        user_wins = 0
        computer_wins = 0

        while user_wins < 3 and computer_wins < 3:
            prompt(f'Game {total_games_played + 1}')
            user_hand = input(f"Choose {', '.join(hand_list)}: ")

            while user_hand not in hand_list:
                user_hand = input(f"Invalid: choose {', '.join(hand_list)}: ")

            computer_hand = random.choice(hand_list)

            prompt(f'User chose: {change_hand_to_full_name(user_hand)}')
            prompt(
                f'Computer chose: {change_hand_to_full_name(computer_hand)}'
            )

            user_wins, computer_wins, total_games_played = display_winner(
                user_hand,
                computer_hand,
                user_wins,
                computer_wins,
                total_games_played
            )

            prompt(f'Games played: {total_games_played}')
            prompt(
                f'Current score: User {user_wins} vs Computer {computer_wins}'
            )
            if user_wins >= 3:
                prompt("🎉 User wins the game!")
            elif computer_wins >= 3:
                prompt("💻 Computer wins the game!")
            print()

        while True:
            ans = input('Play again? y/n ').lower()
            if ans.startswith(('n', 'y')):
                break
            prompt('Please enter "y" or "n".')

        if ans.startswith('n'):
            prompt('Thanks for playing')
            break

if __name__ == '__main__':
    main()
