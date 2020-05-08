from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import API
import os

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


class MyListener(StreamListener):  # TODO: StreamListener argument isn't used.
    # TODO: change the function to add a write to file option
    def write_to_file(self, data):
        try:
            with open(os.getcwd(), 'a') as f:  # change location here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True


twitter_stream = Stream(auth, MyListener())

# change the keyword here
twitter_stream.filter(track=['#FridayFeeling'])  # TODO: set the hash tag track to take a user input
