destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(str, list):
  for city in list:
    if city == str:
      return True
  
  return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False