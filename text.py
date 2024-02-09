# Authenticate with Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

# Post a tweet
tweet_text = "Hello, Twitter! This is my first tweet using Python and Tweepy. #Python #Tweepy #TwitterAPI"
api.update_status(status=tweet_text)

print("Tweet posted successfully!")