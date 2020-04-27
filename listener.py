import credentials as cr
import tweepy

# CONSTANTS
LANGS = ['pt', 'en']
OUTPUT_PT = 'tweets_pt.txt'
OUTPUT_EN = 'tweets_en.txt'

auth = tweepy.OAuthHandler(cr.CONSUMER_KEY, cr.CONSUMER_SECRET)
auth.set_access_token(cr.ACCESS_TOKEN, cr.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

output_pt = open(OUTPUT_PT, 'w')
output_en = open(OUTPUT_EN, 'w')

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.lang in LANGS:
            if status.lang == 'pt':
                output_pt.write(status.full_text + "\n--\n")
            if status.lang == 'en':
                output_en.write(status.full_text + "\n--\n")	

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode='extended')

track_terms = ['covid', 'corona', 'pandemia', 'pandemic', 'quarentena', 'isolamento', 'quarentine', 'isolation', 'locked', 'coronavirus', 'coronavírus', 'hand washing', 'lavar as mãos', 'máscara', 'working from home', 'em casa', 'mask', 'social distancing', 'distanciamento social', 'cough', 'tosse']

myStream.filter(track=track_terms)#['covid', 'corona', 'pandemia', 'pandemic'])
