import tweepy as tw
import os
from dotenv import load_dotenv
import datetime as DT
import re

# datetime  object for one week a
days = 7

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TWITTER_KEY = os.getenv('TWITTER_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

def handle_response(message : str) -> str:
    p_message = message.lower()

    # get tweets from the API
    client = get_client()
    args = p_message.split()
    if args[0] == 'update':
        resp = client.get_user(username = "JOMAN164" if len(args) == 1 else args[1])
        user_id = resp.data.id
        tweet = client.get_users_tweets(id = user_id, max_results = 5,  exclude = ['retweets'])
        return "https://twitter.com/twitter/statuses/" + str(tweet[0][0].id) + "\n" + str(tweet[0][0])
    
    elif args[0] == 'highscore':
        resp = client.get_user(username = "JOMAN164" if len(args) == 1 else args[1])
        user_id = resp.data.id
        if(len(args) > 2):
            days = args[2]
        else: days = 7
        tweet = client.get_users_tweets(id = user_id, start_time = DT.datetime.today()-DT.timedelta(days=int(days)), max_results = 100, tweet_fields='public_metrics', exclude = ['retweets'])
        
        most_liked = get_most_liked_tweets(tweet[0])
        print_str = resp.data.name + " has tweeted " + str(len(most_liked)) + " tweet(s) with " + str(most_liked[0].public_metrics['like_count']) + " likes in the past " + days + " days."
        for t in most_liked:
            print_str += "\n\n" + str(t)
            print_str += "\nhttps://twitter.com/twitter/statuses/" + str(t.id)
        print_str = re.sub('https:\/\/t.co\/\w+', '', print_str)
        return print_str
    
    elif args[0] == 'getlikes':
        resp = client.get_user(username = "JOMAN164" if len(args) == 1 else args[1])
        user_id = resp.data.id
        if(len(args) > 2):
            days = args[2]
        else: days = 7
        tweet = client.get_users_tweets(id = user_id, start_time = DT.datetime.today()-DT.timedelta(days=int(days)), max_results = 100, tweet_fields='public_metrics', exclude = ['retweets'])
        print_str = resp.data.name + " has tweeted " + str(len(tweet[0])) + " time(s) in " + str(days) + " days."
        for t in tweet[0]:
            print_str += "\n**(" + str(t.public_metrics['like_count']) + " likes)** " + str(t)
        print_str = re.sub('https:\/\/t.co\/\w+', '', print_str)
        return print_str
        

def get_client() -> str:
    # authenticate
    auth = tw.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
    api = tw.API(auth, wait_on_rate_limit=True)

    return tw.Client(BEARER_TOKEN)


def get_most_liked_tweets(tweet_list : list) -> list:
    most_liked = []
    # list of likes > get max likes> find all tweets with max amount of likes
    like_count_list = []
    for t in tweet_list:
        like_count_list.append(t.public_metrics['like_count'])
    highest_likes = max(like_count_list)

    count = 0
    for x in like_count_list:
        if(x == highest_likes):
            most_liked.append(tweet_list[count])
        count += 1
    
    return most_liked