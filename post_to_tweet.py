import tweepy

# Set up your credentials
BEARER = "AAAAAAAAAAAAAAAAAAAAAKk2sQEAAAAAaPy%2FfEbPh1kGmGkQGpSseg24qSo%3DJMGXx68HjKTS3wkjdn8fe41qleQdy5rbxYrVike6B1M4gaeXv4"
CONSUMER_KEY = "p4ePCXbUgiYqwHy1fWuEuhJZW"
CONSUMER_SECRET = "jFxrHhXorAcvtkZ6Ijins6HLAi1vv9d0R8SFA424eSRDnsxsTV"
ACCESS_TOKEN = "1755821570142920704-fnqkmgXWz78khLbxH3fIjY9h4Iipyn"
ACCESS_TOKEN_SECRET = "I9YbMYwdiaviOQqdwMdnbVViJjx9GRsF8xRj48K8IqDAQ"

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