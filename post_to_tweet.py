import tweepy

# Set up your cr

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to get account details
def get_account_details(username):
    try:
        user = api.get_user(screen_name=username)
        print("User Details:")
        print("Username:", user.screen_name)
        print("User ID:", user.id)
        print("Followers Count:", user.followers_count)
        print("Friends Count:", user.friends_count)
        print("Statuses Count:", user.statuses_count)
    except tweepy.errors.TweepError as e:
        print("Error getting account details:", e)

# Example usage
target_username = "Rikky36p"
get_account_details(target_username)
