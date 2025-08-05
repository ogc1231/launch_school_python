pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog']) # Bark

print(pets.get('Lizard')) # None

print(pets.get("Lizard", '<silence>'))