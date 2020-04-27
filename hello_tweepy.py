import credentials as cr
import tweepy

auth = tweepy.OAuthHandler(cr.CONSUMER_KEY, cr.CONSUMER_SECRET)
auth.set_access_token(cr.ACCESS_TOKEN, cr.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
print(len(public_tweets))
for tweet in public_tweets:
    print(tweet.text)

user = api.get_user('twitter')

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

# Iterate through the first 200 statuses in the home timeline
for status in tweepy.Cursor(api.home_timeline).items(200):
    # Process the status here
    print(status)
