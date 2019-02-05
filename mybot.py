import tweepy
import time
print('this is my twitter bot', flush=True)

CONSUMER_KEY = 'y8iiRCg3T0eJ9n98Gjw7ZQR3t'
CONSUMER_SECRET = '6pmo8WuXb08fPE6Qiaw3q5ASZo5KOI7FUHuxhM8w0l0NsUIW5a'
ACCESS_KEY = '1092448941763907593-IvcsNtQFPWbGG9rXx6miAmWDxmbg4j'
ACCESS_SECRET = 'rvZxDiN84cqNgIaFv1Xazq8hahP53P9h3KGxupEjSma5E'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

scores = {}

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        ravenclaw = 0
        hufflepuff = 0
        slytheryn = 0
        gryffindor = 0
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if 'info' in mention.full_text.lower():
            print('found info command!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@{} HouseCupAThon info is not avalible yet! ' +
                'Make sure you turn notifications on so you do not miss news updates!'.format(mention.user.screen_name), mention.id)
        elif 'scores' in mention.full_text.lower():
            print('found scores command!', flush=True)
            print('responding back...', flush=True)
            score_list = ['{}: {}'.format(house, score) for house, score in scores.items()]
            print (score_list)
            api.update_status('@{} Ravenclaw: {}'.format(mention.user.screen_name, str(scores.get('ravenclaw', 0))), mention.id)

        else: # houses
            house = None
            if 'ravenclaw' in mention.full_text.lower():
                house = 'ravenclaw'
            elif 'gryffindor' in mention.full_text.lower():
                house = 'gryffindor'
            elif 'hufflepuff' in mention.full_text.lower():
                house = 'hufflepuff'
            elif 'slytherin' in mention.full_text.lower():
                house = 'slytherin'

            if house: # there was indeed a valid house
                points = 0 # no points as of yet, need to analyze
                print('{} adding book!'.format(house.capitalize()), flush=True)

                # set point value
                if 'short' in mention.full_text.lower():
                    points = 10
                elif 'medium' in mention.full_text.lower():
                    points = 30
                elif 'long' in mention.full_text.lower():
                    points = 50
                elif 'giant' in mention.full_text.lower():
                    points = 70
                elif 'tome' in mention.full_text.lower():
                    points = 100

                scores[house] = scores.setdefault(house, 0) + points
                api.update_status('@{} {} points to {}!'.format(mention.user.screen_name, points, house.capitalize()), mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

# mentions = api.mentions_timeline()

# for mention in mentions:
#   print(str(mention.id) + ' - ' + mention.text)
#   if '#housecupathon' in mention.text.lower():
#     print ('found #housecupathon')
