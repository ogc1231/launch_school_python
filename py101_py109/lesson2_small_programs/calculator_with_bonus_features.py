import json
from pathlib import Path

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

file_path = Path(__file__).parent / "calculator_messages.json"
with file_path.open() as file:
    MESSAGES = json.load(file)

# Now ask for language AFTER defining prompt and messages
print("Select language / Seleccione idioma: (en) English, (es) Español")
lang = input().strip().lower()
if lang not in ['en', 'es']:
    lang = 'es'  # default

prompt(messages('welcome', lang))

while True:
    while True:
        prompt(messages('number_prompt_1', lang))
        number1 = input()

        if not invalid_number(number1):
            break

        prompt(messages('invalid_number', lang))

    while True:
        prompt(messages('number_prompt_2', lang))
        number2 = input()

        if not invalid_number(number2):
            break

        prompt(messages('invalid_number', lang))

    while True:
        prompt(messages('operation_prompt', lang))
        operation = input()

        if operation in ["1", "2", "3", "4"]:
            break

        prompt(messages('invalid_operation', lang))

    match operation:
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)  # Round the result to two decimals

    prompt(messages('result', lang).format(output=output))

    prompt(messages('another_operation', lang))
    answer = input()
    if (lang == 'es' and answer[0].lower() != 's') or (lang == 'en' and answer[0].lower() != 'y'):
        break
