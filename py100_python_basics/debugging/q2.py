import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
# the choices for sunshine are both strings which are truthy when not empty, need change to boolean values
# also predict_weather is not being envoked