import tweepy as tw
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TWITTER_KEY = os.getenv('TWITTER_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')

def handle_response(message : str) -> str:
    p_message = message.lower()

    if p_message.split(' ', 1)[0] == 'update':
        # your Twitter API key and API secret
        my_api_key = TWITTER_KEY
        my_api_secret = TWITTER_SECRET

        # authenticate
        auth = tw.OAuthHandler(my_api_key, my_api_secret)
        api = tw.API(auth, wait_on_rate_limit=True)

        client = tw.Client(CLIENT_ID)

        # get tweets from the API
        if p_message == 'update':
            resp = client.get_user(username = "JOMAN164")
            user_id = resp.data.id
            tweet = client.get_users_tweets(id = user_id, max_results = 5,  exclude = ['retweets'])
            return "https://twitter.com/twitter/statuses/" + str(tweet[0][0].id) + "\n" + str(tweet[0][0])
        else:
            resp = client.get_user(username = p_message.split(' ', 1)[1])
            user_id = resp.data.id
            tweet = client.get_users_tweets(id = user_id, max_results = 5,  exclude = ['retweets'])
            return "https://twitter.com/twitter/statuses/" + str(tweet[0][0].id) + "\n" + str(tweet[0][0])
