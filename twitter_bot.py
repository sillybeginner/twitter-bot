import tweepy #pip install tweepy to use Twitter API with Python 
import logging
import time

#Authenticate to Twitter
#Logging to Twitter Developer portal
#create app and there u will get these keys consumer and access_token both secret and keys or token etc
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret") 
auth.set_access_token("acess_token","acess_token_secret") 
                                                        
#Create API Object
api = tweepy.API(auth)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#For Like and Retweet the tweet of other
class FavRetweet(tweepy.Stream):
    def __init__(self, api):
        self.api = api
        self.me = api.get_user()
    
    #Processes tweets from the stream.
    #This method receives a status obj and uses Favorite() for like and retweet() to mark the tweet as retweet
    #Use Try and Except in case of Error and to avoid crash
    #Using conditionals statements to avoid retweeting and liking tweets that are replies to other tweets
    def on_status(self, tweet):
        logger.info(f"Processing tweet id {tweet.id}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
                return
            
        if not tweet.favorited:
            try:
                tweet.favorited()
            
            except Exception as e:
                logger.error("Error on like " , exc_info=True)
        
        if not tweet.retweeted:
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error on like and retweet ", exc_info=True)
                
    def on_error(self, status):
        logger.error(status)

#This main function will use the API keys and access token to create a Tweepy API Obj
#A Tweepy Stream is created to to filter tweets that are in the English lang and include some of the keywords specified in
#in the main function argument    
def main(keywords):
    tweets_listner = FavRetweet(api)
    stream = tweepy.Stream(api, tweets_listner)
    stream.filter(track=keywords, languages=['en'])

#you can decrease it or increase it as you like.Please,use large delay if you are running bot all the time  so that your account does not get banned.
time.sleep(3600) #Equivalent to 1 hr
        
if __name__ == '__main__':
    main(["Python", "Java", "javascript", "developer", "coder", "code","programmer", "computer"])   
