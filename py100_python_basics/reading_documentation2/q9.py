# following code raises a TypeError

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5 # 5 should be outside of brackets len(tweet) + 5

# can't concatenate a str and an int