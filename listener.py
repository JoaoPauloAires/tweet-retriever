import credentials as cr
import tweepy

# CONSTANTS
LANGS = ['pt', 'en']
OUTPUT_FILE = 'tweets.txt'

auth = tweepy.OAuthHandler(cr.CONSUMER_KEY, cr.CONSUMER_SECRET)
auth.set_access_token(cr.ACCESS_TOKEN, cr.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

output_file = open(OUTPUT_FILE, 'w')

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.lang in LANGS:
            output_file.write(status.text + "\n--\n")

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['covid'])