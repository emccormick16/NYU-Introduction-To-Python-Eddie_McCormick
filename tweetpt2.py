tweet = input("What is your tweet?\n")
print("Your tweet is",len(tweet),"characters long.")
if len(tweet) < 280:
    print("You have",280 - len(tweet),"characters remaining.")
elif len(tweet) > 280:
    print ("You have exceeded the limit by",len(tweet) - 280,"characters.")
else:
    print ("You are at the limit, you have no characters remaining.")
