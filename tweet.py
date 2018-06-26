tweet = input("What is your tweet?\n")
print("Your tweet is",len(tweet),"characters long.")
if len(tweet) < 280:
    print("You still have space.")
elif len(tweet) > 280:
    print ("You have exceeded the limit, your tweet is too long.")
else:
    print ("You are at the limit.")
