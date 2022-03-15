# twitter-bot
A simple Twitter Bot which will like and retweet the tweets of other programmers and developers

Install tweepy Python module
pip install tweepy

Sign up for a Twitter Developer Account
Create a separate Twitter account for your bot.
Sign up for Twitter Developer Account from this site - https://developer.twitter.com/en/apply-for-access
Enter the necessary fields and await for email confirmation.
Click on Create an app
Enter the details and keep safe the access tokens generated.

you can create new variable and then assign them the generated keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

here like this 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret) 
auth.set_access_token(acess_token,acess_token_secret)

Don't forget to set these credentials
