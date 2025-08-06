cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for i in range(len(cities)):
  if cities[i] == None:
    continue
  print(cities[i])