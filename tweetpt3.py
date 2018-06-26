tweet_limit = int(input("What is the character limit?\n"))
tweet = input("What is your tweet?\n")
print("Your tweet is",len(tweet),"characters long.")
if len(tweet) < tweet_limit:
    print("You have",tweet_limit - len(tweet),"characters remaining.")
elif len(tweet) > tweet_limit:
    print ("You have exceeded the limit by",len(tweet) - tweet_limit,"characters.")
else:
    print ("You are at the limit, you have no characters remaining.")
