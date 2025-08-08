import json
from pathlib import Path

file_path = Path(__file__).parent / "file.json"
with file_path.open() as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(MESSAGES['welcome'])

while True:
    prompt(MESSAGES['first_num'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['second_num'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES['choice'])
        operation = input()

    match operation:
        case "1":
            output = int(number1) + int(number2)
        case "2":
            output = int(number1) - int(number2)
        case "3":
            output = int(number1) * int(number2)
        case "4":
            output = int(number1) / int(number2)

    prompt(f"The result is {output}")

    prompt(MESSAGES['another'])
    answer = input()

    if answer and answer[0].lower() != 'y':
        prompt(MESSAGES['goodbye'])
        break