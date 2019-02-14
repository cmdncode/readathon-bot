import tweepy
import time
import random
from random import randint
print('this is my sprint bot', flush=True)
length = 0


CONSUMER_KEY = 'mgn6uqjurbv4vYbbyQIINgWAj'
CONSUMER_SECRET = 'AEPlDPknQKSCEpsZQgY8rq0Kga0Gf7AEGZDke28yFbIszkOj72'
ACCESS_KEY = '1092448941763907593-j1STBqsVZzMWwCCmrWxoLvwpsQkGqF'
ACCESS_SECRET = 'mMflae7Tj70Y2X6BbRLSoXmyGTqNqtILyCMdSfBFl9EUN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id2.txt'

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
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if 'sprint' in mention.full_text.lower():
            print('found sprint command!', flush=True)
            print('responding back...', flush=True)
            print('randomizing...')
            ran_number1 = (randint(1, 50))
            ran_number2 = (randint(1, 50))
            ran_number3 = (randint(1, 10))
            length = 0
            sprint_tweet_master = ''

            # creating sprint tweet parts
            sprint_tweet1 = ''
            sprint_tweet2 = ''
            sprint_tweet3 = ''

            # creating general sprint time tweet for each time slot-- part 3 generator 
            if '15' in mention.full_text.lower():
                length = 15
                if ran_number3 == 1:
                    sprint_tweet3 = '15 mins!'
                elif ran_number3 == 2:
                    sprint_tweet3 = '15 min sprint!'
                elif ran_number3 == 3:
                    sprint_tweet3 = '15 min sprint starting!'
                elif ran_number3 == 4:
                    sprint_tweet3 = '15 min sprint starting now!'
                elif ran_number3 == 5:
                    sprint_tweet3 = '15 min sprint, as requested!'
                elif ran_number3 == 6:
                    sprint_tweet3 = '15 min sprint is starting!'
                elif ran_number3 == 7:
                    sprint_tweet3 = '15 min sprint, get reading!'
                elif ran_number3 == 8:
                    sprint_tweet3 = 'Starting a 15 min sprint!'
                elif ran_number3 == 9:
                    sprint_tweet3 = 'We are starting 15 min sprint now!'
                elif ran_number3 == 10:
                    sprint_tweet3 = '15 min sprint, come join!'

            if '30' in mention.full_text.lower():
                length = 30
                if ran_number3 == 1:
                    sprint_tweet3 = '30 mins!'
                elif ran_number3 == 2:
                    sprint_tweet3 = '30 min sprint!'
                elif ran_number3 == 3:
                    sprint_tweet3 = '30 min sprint starting!'
                elif ran_number3 == 4:
                    sprint_tweet3 = '30 min sprint starting now!'
                elif ran_number3 == 5:
                    sprint_tweet3 = '30 min sprint, as requested!'
                elif ran_number3 == 6:
                    sprint_tweet3 = '30 min sprint is starting!'
                elif ran_number3 == 7:
                    sprint_tweet3 = '30 min sprint, get reading!'
                elif ran_number3 == 8:
                    sprint_tweet3 = 'Starting a 30 min sprint!'
                elif ran_number3 == 9:
                    sprint_tweet3 = 'We are starting 30 min sprint now!'
                elif ran_number3 == 10:
                    sprint_tweet3 = '30 min sprint, come join!'

            if '45' in mention.full_text.lower():
                length = 45
                if ran_number3 == 1:
                    sprint_tweet3 = '45 mins!'
                elif ran_number3 == 2:
                    sprint_tweet3 = '45 min sprint!'
                elif ran_number3 == 3:
                    sprint_tweet3 = '45 min sprint starting!'
                elif ran_number3 == 4:
                    sprint_tweet3 = '45 min sprint starting now!'
                elif ran_number3 == 5:
                    sprint_tweet3 = '45 min sprint, as requested!'
                elif ran_number3 == 6:
                    sprint_tweet3 = '45 min sprint is starting!'
                elif ran_number3 == 7:
                    sprint_tweet3 = '45 min sprint, get reading!'
                elif ran_number3 == 8:
                    sprint_tweet3 = 'Starting a 45 min sprint!'
                elif ran_number3 == 9:
                    sprint_tweet3 = 'We are starting 45 min sprint now!'
                elif ran_number3 == 10:
                    sprint_tweet3 = '45 min sprint, come join!'

            if '60' in mention.full_text.lower():
                length = 60
                if ran_number3 == 1:
                    sprint_tweet3 = '60 mins!'
                elif ran_number3 == 2:
                    sprint_tweet3 = '60 min sprint!'
                elif ran_number3 == 3:
                    sprint_tweet3 = '60 min sprint starting!'
                elif ran_number3 == 4:
                    sprint_tweet3 = '60 min sprint starting now!'
                elif ran_number3 == 5:
                    sprint_tweet3 = '60 min sprint, as requested!'
                elif ran_number3 == 6:
                    sprint_tweet3 = '60 min sprint is starting!'
                elif ran_number3 == 7:
                    sprint_tweet3 = '60 min sprint, get reading!'
                elif ran_number3 == 8:
                    sprint_tweet3 = 'Starting a 60 min sprint!'
                elif ran_number3 == 9:
                    sprint_tweet3 = 'We are starting 60 min sprint now!'
                elif ran_number3 == 10:
                    sprint_tweet3 = '60 min sprint, come join!'

            # replying to user

            ran_msg1 = (randint(1, 20))
            ran_msg2 = (randint(1, 50))
            reply1 = ''
            reply2 = ''

            # msg 1 generator
            if ran_msg1 == 1:
                reply1 = ' Make sure you check in via the main tweet!'
            elif ran_msg1 == 2:
                reply1 = ' Make sure you let everyone know youre participating!'
            elif ran_msg1 == 3:
                reply1 = ' Make sure you let everyone know youre participating via the main tweet!'
            elif ran_msg1 == 4:
                reply1 = ' Make sure you check in with everyone!'
            elif ran_msg1 == 5:
                reply1 = ' Make sure to say hi to everyone!'
            elif ran_msg1 == 6:
                reply1 = ' Make sure to say hi to everyone via the main tweet!'
            elif ran_msg1 == 7:
                reply1 = ' Its a party! Make sure you check in via the main tweet!'
            elif ran_msg1 == 8:
                reply1 = ' Its a party! Make sure you let everyone know youre participating!'
            elif ran_msg1 == 9:
                reply1 = ' Its a party! Make sure you let everyone know youre participating via the main tweet!'
            elif ran_msg1 == 10:
                reply1 = ' Its a party! Make sure you check in with everyone!'
            elif ran_msg1 == 11:
                reply1 = ' Its a party! Make sure to say hi to everyone!'
            elif ran_msg1 == 12:
                reply1 = ' Its a party! Make sure to say hi to everyone via the main tweet!'
            elif ran_msg1 == 13:
                reply1 = ' Make sure you tag your friends!'
            elif ran_msg1 == 14:
                reply1 = ' Make sure to tag your friends in the main tweet!'
            elif ran_msg1 == 15:
                reply1 = ' Make sure to get all your friends involved!'
            elif ran_msg1 == 16:
                reply1 = ' Make sure to get all your friends involved via the main tweet!'
            elif ran_msg1 == 17:
                reply1 = ' Now shame your friends into participating!'
            elif ran_msg1 == 18:
                reply1 = ' Now tag all your friends! SHAME THEM INTO PARTICIPATING!'
            elif ran_msg1 == 19:
                reply1 = ' Invite all your friends to participate!'
            elif ran_msg1 == 20:
                reply1 = ' Make sure to invite all your friends to participate!'
            else:
                reply1 = 'error creating tweet_pt1'
        
            # msg 1 generator
            if ran_msg2 == 1:
                reply2 = ' You know what to do!'
            elif ran_msg2 == 2:
                reply2 = ' Get to reading!'
            elif ran_msg2 == 3:
                reply2 = ' Read away friend!'
            elif ran_msg2 == 4:
                reply2 = ' READ READ READ!'
            elif ran_msg2 == 5:
                reply2 = ' Get to reading!'
            elif ran_msg2 == 6:
                reply2 = ' READDD!'
            elif ran_msg2 == 7:
                reply2 = ' Its a sprint, get reading!'
            elif ran_msg2 == 8:
                reply2 = ' Sprint away!'
            elif ran_msg2 == 9:
                reply2 = ' READ!'
            elif ran_msg2 == 10:
                reply2 = ' GO!'
            elif ran_msg2 == 11:
                reply2 = ' GO! Get to reading!'
            elif ran_msg2 == 12:
                reply2 = ' READ THE BOOOOKKK!'
            elif ran_msg2 == 13:
                reply2 = ' Get some reading done!'
            elif ran_msg2 == 14:
                reply2 = ' Speed read mode - engaged!'
            elif ran_msg2 == 15:
                reply2 = ' SPRINT SPRINT SPRINT!'
            elif ran_msg2 == 16:
                reply2 = ' I believe in you!'
            elif ran_msg2 == 17:
                reply2 = ' Now kick some butt and READ!'
            elif ran_msg2 == 18:
                reply2 = ' Get that book read!'
            elif ran_msg2 == 19:
                reply2 = ' Now, READDD!'
            elif ran_msg2 == 20:
                reply2 = ' Now SPRINT!'
            elif ran_msg2 == 21:
                reply2 = ' Sprint away my friends!'
            elif ran_msg2 == 22:
                reply2 = ' Sprint, Sprint, Sprint!'
            elif ran_msg2 == 23:
                reply2 = ' GO GO GO!'
            elif ran_msg2 == 24:
                reply2 = ' NOW GO!'
            elif ran_msg2 == 25:
                reply2 = ' NOW GET READING!'
            elif ran_msg2 == 26:
                reply2 = ' Get going and READ!'
            elif ran_msg2 == 27:
                reply2 = ' READ! READ NOW!'
            elif ran_msg2 == 28:
                reply2 = ' Now get a chunk of reading done!'
            elif ran_msg2 == 29:
                reply2 = ' Reading sprints are just sprints of the mind. GO!'
            elif ran_msg2 == 30:
                reply2 = ' GO! READ! RIGHT NOW!'
            elif ran_msg2 == 31:
                reply2 = ' Make your house proud!'
            elif ran_msg2 == 32:
                reply2 = ' Focus! Read!'
            elif ran_msg2 == 33:
                reply2 = ' Get focusing! Get reading!'
            elif ran_msg2 == 34:
                reply2 = ' Now focus, and READ!'
            elif ran_msg2 == 35:
                reply2 = ' Focus all your energy on READING!'
            elif ran_msg2 == 36:
                reply2 = ' Lets see who can read the MOST!'
            elif ran_msg2 == 37:
                reply2 = ' DO you think you can read the most?!'
            elif ran_msg2 == 38:
                reply2 = ' READ! You know you wanna!'
            elif ran_msg2 == 39:
                reply2 = ' Focus on your book and READ!'
            elif ran_msg2 == 40:
                reply2 = ' Focus on reading. GO!'
            elif ran_msg2 == 41:
                reply2 = ' Think you can read more than me?!'
            elif ran_msg2 == 42:
                reply2 = ' Have fun! Read!'
            elif ran_msg2 == 43:
                reply2 = ' READ, and remember to have fun!'
            elif ran_msg2 == 45:
                reply2 = ' Sprinting is my favorite!'
            elif ran_msg2 == 46:
                reply2 = ' I love sprinting!'
            elif ran_msg2 == 47:
                reply2 = ' I always love sprinting with you all!'
            elif ran_msg2 == 48:
                reply2 = ' Im so glad you started this sprint!'
            elif ran_msg2 == 49:
                reply2 = ' SPRINT! GO! READ!'
            elif ran_msg2 == 50:
                reply2 = ' READ DAT!'



            api.update_status('@{} You have started a {} min sprint via housecupathon! {}'.format(mention.user.screen_name), mention.id, length, randommsg1, randommsg2)

            print ('randomizing pt 2...')
            # part 1 generator
            if ran_number1 == 1:
                sprint_tweet1 = ' You know what to do!'
            elif ran_number1 == 2:
                sprint_tweet1 = ' Get to reading!'
            elif ran_number1 == 3:
                sprint_tweet1 = ' Read away friends!'
            elif ran_number1 == 4:
                sprint_tweet1 = ' READ READ READ!'
            elif ran_number1 == 5:
                sprint_tweet1 = ' Get to reading!'
            elif ran_number1 == 6:
                sprint_tweet1 = ' READDD!'
            elif ran_number1 == 7:
                sprint_tweet1 = ' Its a sprint, get reading!'
            elif ran_number1 == 8:
                sprint_tweet1 = ' Sprint away!'
            elif ran_number1 == 9:
                sprint_tweet1 = ' READ!'
            elif ran_number1 == 10:
                sprint_tweet1 = ' GO!'
            elif ran_number1 == 11:
                sprint_tweet1 = ' GO! Get to reading!'
            elif ran_number1 == 12:
                sprint_tweet1 = ' READ THE BOOOOKKK!'
            elif ran_number1 == 13:
                sprint_tweet1 = ' Get some reading done!'
            elif ran_number1 == 14:
                sprint_tweet1 = ' Speed read mode - engaged!'
            elif ran_number1 == 15:
                sprint_tweet1 = ' SPRINT SPRINT SPRINT!'
            elif ran_number1 == 16:
                sprint_tweet1 = ' I believe in you!'
            elif ran_number1 == 17:
                sprint_tweet1 = ' Now kick some butt and READ!'
            elif ran_number1 == 18:
                sprint_tweet1 = ' Get that book read!'
            elif ran_number1 == 19:
                sprint_tweet1 = ' Now, READDD!'
            elif ran_number1 == 20:
                sprint_tweet1 = ' Now SPRINT!'
            elif ran_number1 == 21:
                sprint_tweet1 = ' Sprint away my friends!'
            elif ran_number1 == 22:
                sprint_tweet1 = ' Sprint, Sprint, Sprint!'
            elif ran_number1 == 23:
                sprint_tweet1 = ' GO GO GO!'
            elif ran_number1 == 24:
                sprint_tweet1 = ' NOW GO!'
            elif ran_number1 == 25:
                sprint_tweet1 = ' NOW GET READING!'
            elif ran_number1 == 26:
                sprint_tweet1 = ' Get going and READ!'
            elif ran_number1 == 27:
                sprint_tweet1 = ' READ! READ NOW!'
            elif ran_number1 == 28:
                sprint_tweet1 = ' Now get a chunk of reading done!'
            elif ran_number1 == 29:
                sprint_tweet1 = ' Reading sprints are just sprints of the mind. GO!'
            elif ran_number1 == 30:
                sprint_tweet1 = ' GO! READ! RIGHT NOW!'
            elif ran_number1 == 31:
                sprint_tweet1 = ' Make your house proud!'
            elif ran_number1 == 32:
                sprint_tweet1 = ' Focus! Read!'
            elif ran_number1 == 33:
                sprint_tweet1 = ' Get focusing! Get reading!'
            elif ran_number1 == 34:
                sprint_tweet1 = ' Now focus, and READ!'
            elif ran_number1 == 35:
                sprint_tweet1 = ' Focus all your energy on READING!'
            elif ran_number1 == 36:
                sprint_tweet1 = ' Lets see who can read the MOST!'
            elif ran_number1 == 37:
                sprint_tweet1 = ' DO you think you can read the most?!'
            elif ran_number1 == 38:
                sprint_tweet1 = ' READ! You know you wanna!'
            elif ran_number1 == 39:
                sprint_tweet1 = ' Focus on your book and READ!'
            elif ran_number1 == 40:
                sprint_tweet1 = ' Focus on reading. GO!'
            elif ran_number1 == 41:
                sprint_tweet1 = ' Think you can read more than me?!'
            elif ran_number1 == 42:
                sprint_tweet1 = ' Have fun! Read!'
            elif ran_number1 == 43:
                sprint_tweet1 = ' READ, and remember to have fun!'
            elif ran_number1 == 45:
                sprint_tweet1 = ' Sprinting is my favorite!'
            elif ran_number1 == 46:
                sprint_tweet1 = ' I love sprinting!'
            elif ran_number1 == 47:
                sprint_tweet1 = ' I always love sprinting with you all!'
            elif ran_number1 == 48:
                sprint_tweet1 = ' Id be so happy if youd join us!'
            elif ran_number1 == 49:
                sprint_tweet1 = ' SPRINT! GO! READ!'
            elif ran_number1 == 50:
                sprint_tweet1 = ' READ DAT!'
        
        
            # part 2 generator
            if ran_number2 == 1:
                sprint_tweet2 = ' Let everyone know you are here!'
            elif ran_number2 == 2:
                sprint_tweet2 = ' Let everyone know you are participating!'
            elif ran_number2 == 3:
                sprint_tweet2 = ' Please RT!'
            elif ran_number2 == 4:
                sprint_tweet2 = ' Please share!'
            elif ran_number2 == 5:
                sprint_tweet2 = ' Please share with your friends!'
            elif ran_number2 == 6:
                sprint_tweet2 = ' Remember to share with your friends!'
            elif ran_number2 == 7:
                sprint_tweet2 = ' Share! The more the merrier'
            elif ran_number2 == 8:
                sprint_tweet2 = ' Start this sprint off right!'
            elif ran_number2 == 9:
                sprint_tweet2 = ' Do you have a page goal in m!ind'
            elif ran_number2 == 10:
                sprint_tweet2 = ' How many pages do you think you can read?'
            elif ran_number2 == 11:
                sprint_tweet2 = ' Let us know you are sprinting with us!'
            elif ran_number2 == 12:
                sprint_tweet2 = ' Remember to make your presence known!'
            elif ran_number2 == 13:
                sprint_tweet2 = ' DO you have a goal in mind this sprint?!'
            elif ran_number2 == 14:
                sprint_tweet2 = ' RT to get more people on board!'
            elif ran_number2 == 15:
                sprint_tweet2 = ' Let us know your page goal!'
            elif ran_number2 == 16:
                sprint_tweet2 = ' How much do you think you can read in this time frame?'
            elif ran_number2 == 17:
                sprint_tweet2 = ' Tag a friend who loves sprints!'
            elif ran_number2 == 18:
                sprint_tweet2 = ' Tag a friend who loves reading sprints!!'
            elif ran_number2 == 19:
                sprint_tweet2 = ' Help grow our community and tag a friend who likes reading sprints!'
            elif ran_number2 == 20:
                sprint_tweet2 = ' Help grow our community and RT!'
            elif ran_number2 == 21:
                sprint_tweet2 = ' Help grow our community and share!'
            elif ran_number2 == 22:
                sprint_tweet2 = ' Help grow our community and get your friends involved!'
            elif ran_number2 == 23:
                sprint_tweet2 = ' Help grow pur community and share this tweet!'
            elif ran_number2 == 24:
                sprint_tweet2 = ' Let everyone know youre sprinting by replying to this tweet!'
            elif ran_number2 == 25:
                sprint_tweet2 = ' Let everyone know you are sprinting by replying to this tweet!'
            elif ran_number2 == 26:
                sprint_tweet2 = ' Let your friends know! The more participants, the more fun we will have!'            
            elif ran_number2 == 27:
                sprint_tweet2 = ' This is gonna be so much fun!'
            elif ran_number2 == 28:
                sprint_tweet2 = ' This is gonna be fun!'
            elif ran_number2 == 29:
                sprint_tweet2 = ' This is going to be a blast!'
            elif ran_number2 == 30:
                sprint_tweet2 = ' This is gonna be a blast!'
            elif ran_number2 == 31:
                sprint_tweet2 = ' Have fun!'
            elif ran_number2 == 32:
                sprint_tweet2 = ' Have fun all!'
            elif ran_number2 == 33:
                sprint_tweet2 = ' Remember to have fun!'
            elif ran_number2 == 34:
                sprint_tweet2 = ' I love a good sprint!'
            elif ran_number2 == 35:
                sprint_tweet2 = ' Make sure to RT or tag your friends!'
            elif ran_number2 == 36:
                sprint_tweet2 = ' Let everyone know you are sprinting and reply to this tweet'
            elif ran_number2 == 37:
                sprint_tweet2 = ' Get off twitter and get going!'
            elif ran_number2 == 38:
                sprint_tweet2 = ' No more twitter! Get sprinting'
            elif ran_number2 == 39:
                sprint_tweet2 = ' Invite your friends!'
            elif ran_number2 == 40:
                sprint_tweet2 = ' Remember to invite your friends!'
            elif ran_number2 == 41:
                sprint_tweet2 = ' RT to support this account!'
            elif ran_number2 == 42:
                sprint_tweet2 = ' Remember to share to support this account!'
            elif ran_number2 == 43:
                sprint_tweet2 = ' Remember to share and support our growing community!'
            elif ran_number2 == 45:
                sprint_tweet2 = ' Remember to support us by sharing!'
            elif ran_number2 == 46:
                sprint_tweet2 = ' Remember to support our growing community and share!'
            elif ran_number2 == 47:
                sprint_tweet2 = ' Remember to RT and share with your bookish friends!'
            elif ran_number2 == 48:
                sprint_tweet2 = ' Id be so greatful if you would share this sprint with your friends!'
            elif ran_number2 == 49:
                sprint_tweet2 = ' REMEMBER TO RT OUR SPRINTS!'
            elif ran_number2 == 50:
                sprint_tweet1 = ' Lets GOOOOOOOOOOO!!!!'
            




            sprint_tweet_master = (sprint_tweet3 + sprint_tweet1 + sprint_tweet2)
            print (sprint_tweet_master)
            api.update_status(sprint_tweet_master)
            # create sleep timer until sprint ends 

            if length == 15:
                time.sleep(900)
            # time.sleep(15)
            elif length == 30:
                time.sleep(1800)
            elif length == 45:
                time.sleep(2700)
            elif length == 60:
                time.sleep(3600)
            else:
                api.update_status('@{} You have attempted to start a sprint via housecupathon, but there was an error'.format(mention.user.screen_name), mention.id)
   
            print('found sprint end command!', flush=True)
            print('responding back...', flush=True)
            ran_number4 = (randint(1, 10))
            ran_number5 = (randint(1, 50))
            ran_number6 = (randint(1, 50))
            sprint_tweet_master_end = ''

            # creating sprint tweet parts
            sprint_tweet4 = ''
            sprint_tweet5 = ''
            sprint_tweet6 = ''

            # creating general sprint time tweet for each time slot-- part 3 generator 
            if '15' in mention.full_text.lower():
                length = 15
                if ran_number4 == 1:
                    sprint_tweet4 = '15 min sprint is over!'
                elif ran_number4 == 2:
                    sprint_tweet4 = '15 min sprint ends now!'
                elif ran_number4 == 3:
                    sprint_tweet4 = '15 min sprint ending!'
                elif ran_number4 == 4:
                    sprint_tweet4 = '15 min sprint ending now!'
                elif ran_number4 == 5:
                    sprint_tweet4 = 'Requested 15 min sprint, over!'
                elif ran_number4 == 6:
                    sprint_tweet4 = '15 min sprint is ending!'
                elif ran_number4 == 7:
                    sprint_tweet4 = '15 min sprint over, stop reading!'
                elif ran_number4 == 8:
                    sprint_tweet4 = 'Ending the 15 min sprint!'
                elif ran_number4 == 9:
                    sprint_tweet4 = 'We are ending 15 min sprint now!'
                elif ran_number4 == 10:
                    sprint_tweet4 = '15 min sprint, ITS OVER!'

            if '30' in mention.full_text.lower():
                length = 30
                if ran_number4 == 1:
                    sprint_tweet4 = '30 min sprint is over!'
                elif ran_number4 == 2:
                    sprint_tweet4 = '30 min sprint ends now!'
                elif ran_number4 == 3:
                    sprint_tweet4 = '30 min sprint ending!'
                elif ran_number4 == 4:
                    sprint_tweet4 = '30 min sprint ending now!'
                elif ran_number4 == 5:
                    sprint_tweet4 = 'Requested 30 min sprint, over!'
                elif ran_number4 == 6:
                    sprint_tweet4 = '30 min sprint is ending!'
                elif ran_number4 == 7:
                    sprint_tweet4 = '30 min sprint over, stop reading!'
                elif ran_number4 == 8:
                    sprint_tweet4 = 'Ending the 30 min sprint!'
                elif ran_number4 == 9:
                    sprint_tweet4 = 'We are ending 30 min sprint now!'
                elif ran_number4 == 10:
                    sprint_tweet4 = '30 min sprint, ITS OVER!'

            if '45' in mention.full_text.lower():
                length = 45
                if ran_number4 == 1:
                    sprint_tweet4 = '45 min sprint is over!'
                elif ran_number4 == 2:
                    sprint_tweet4 = '45 min sprint ends now!'
                elif ran_number4 == 3:
                    sprint_tweet4 = '45 min sprint ending!'
                elif ran_number4 == 4:
                    sprint_tweet4 = '45 min sprint ending now!'
                elif ran_number4 == 5:
                    sprint_tweet4 = 'Requested 45 min sprint, over!'
                elif ran_number4 == 6:
                    sprint_tweet4 = '45 min sprint is ending!'
                elif ran_number4 == 7:
                    sprint_tweet4 = '45 min sprint over, stop reading!'
                elif ran_number4 == 8:
                    sprint_tweet4 = 'Ending the 45 min sprint!'
                elif ran_number4 == 9:
                    sprint_tweet4 = 'We are ending the 45 min sprint now!'
                elif ran_number4 == 10:
                    sprint_tweet4 = '45 min sprint, ITS OVER!'

            if '60' in mention.full_text.lower():
                length = 60
                if ran_number4 == 1:
                    sprint_tweet4 = '60 min sprint is over!'
                elif ran_number4 == 2:
                    sprint_tweet4 = '60 min sprint ends now!'
                elif ran_number4 == 3:
                    sprint_tweet4 = '60 min sprint ending!'
                elif ran_number4 == 4:
                    sprint_tweet4 = '60 min sprint ending now!'
                elif ran_number4 == 5:
                    sprint_tweet4 = 'Requested 60 min sprint, over!'
                elif ran_number4 == 6:
                    sprint_tweet4 = '60 min sprint is ending!'
                elif ran_number4 == 7:
                    sprint_tweet4 = '60 min sprint over, stop reading!'
                elif ran_number4 == 8:
                    sprint_tweet4 = 'Ending the 60 min sprint!'
                elif ran_number4 == 9:
                    sprint_tweet4 = 'We are ending 60 min sprint now!'
                elif ran_number4 == 10:
                    sprint_tweet4 = '60 min sprint, ITS OVER!'

            # replying to user
            api.update_status('@{} Your sprint via housecupathon has ended! Remember to check in via the main tweet!'.format(mention.user.screen_name), mention.id)

            print ('randomizing pt 2 sprint ending...')
            # part 1 generator
            if ran_number5 == 1:
                sprint_tweet5 = ' Thanks for joining us!'
            elif ran_number5 == 2:
                sprint_tweet5 = ' Thanks for sprinting with us!'
            elif ran_number5 == 3:
                sprint_tweet5 = ' Thanks for participating!'
            elif ran_number5 == 4:
                sprint_tweet5 = ' Thanks for participating in this sprint!'
            elif ran_number5 == 5:
                sprint_tweet5 = ' Thanks for joining this sprint!'
            elif ran_number5 == 6:
                sprint_tweet5 = ' Hope you enjoyed this sprint!'
            elif ran_number5 == 7:
                sprint_tweet5 = ' Hope you had fun sprinting with us!'
            elif ran_number5 == 8:
                sprint_tweet5 = ' Hope you had fun durring this sprint!'
            elif ran_number5 == 9:
                sprint_tweet5 = ' Hope you had fun!'
            elif ran_number5 == 10:
                sprint_tweet5 = ' Hope you enjoyed reading with us!'
            elif ran_number5 == 11:
                sprint_tweet5 = ' Hope you are enjoying your book!'
            elif ran_number5 == 12:
                sprint_tweet5 = ' Hope you are loving your book!'
            elif ran_number5 == 13:
                sprint_tweet5 = ' Hope your book is amazing!'
            elif ran_number5 == 14:
                sprint_tweet5 = ' Hopefully you got a lot read!'
            elif ran_number5 == 15:
                sprint_tweet5 = ' Hope you got a chunk of reading done!'
            elif ran_number5 == 16:
                sprint_tweet5 = ' Hope you are speeding through your book!'
            elif ran_number5 == 17:
                sprint_tweet5 = ' Hope your book is enjoyable!'
            elif ran_number5 == 18:
                sprint_tweet5 = ' Hope youre getting that book read!'
            elif ran_number5 == 19:
                sprint_tweet5 = ' We love a good sprint!'
            elif ran_number5 == 20:
                sprint_tweet5 = ' We always love sprinting with you guys!'
            elif ran_number5 == 21:
                sprint_tweet5 = ' Hope you kicked butt durring this sprint!'
            elif ran_number5 == 22:
                sprint_tweet5 = ' Remember to take breaks!'
            elif ran_number5 == 23:
                sprint_tweet5 = ' Remember to eat!'
            elif ran_number5 == 24:
                sprint_tweet5 = ' Remember to stay hydrated!'
            elif ran_number5 == 25:
                sprint_tweet5 = ' Remember, your basic need are way more important than reading!'
            elif ran_number5 == 26:
                sprint_tweet5 = ' We love a good reading sprint!'
            elif ran_number5 == 27:
                sprint_tweet5 = ' Hope you are focused and read for more sprints!'
            elif ran_number5 == 28:
                sprint_tweet5 = ' Hope your sprint went well!'
            elif ran_number5 == 29:
                sprint_tweet5 = ' Hope you are ready for more reading sprints!'
            elif ran_number5 == 30:
                sprint_tweet5 = ' Remember you can start your own sprints anytime!'
            elif ran_number5 == 31:
                sprint_tweet5 = ' Check out the commands to start your own sprints!'
            elif ran_number5 == 32:
                sprint_tweet5 = ' Feel like sprinting more? Start one yourself using the bot commands!'
            elif ran_number5 == 33:
                sprint_tweet5 = ' Remember anyone can start a sprint here!'
            elif ran_number5 == 34:
                sprint_tweet5 = ' Sprints are always so uch fun!'
            elif ran_number5 == 35:
                sprint_tweet5 = ' Im ready for another!'
            elif ran_number5 == 36:
                sprint_tweet5 = ' Hope you stayed focus durring this sprint!'
            elif ran_number5 == 37:
                sprint_tweet5 = ' Hope you stayed focused durring this reading sprint!'
            elif ran_number5 == 38:
                sprint_tweet5 = ' I just love reading!'
            elif ran_number5 == 39:
                sprint_tweet5 = ' I love sharing my reading with you all!'
            elif ran_number5 == 40:
                sprint_tweet5 = ' This is so much fun!!'
            elif ran_number5 == 41:
                sprint_tweet5 = ' Im having a blast!'
            elif ran_number5 == 42:
                sprint_tweet5 = ' Im having so much fun!'
            elif ran_number5 == 43:
                sprint_tweet5 = ' Remember that you read for fun!!'
            elif ran_number5 == 45:
                sprint_tweet5 = ' Remember... reading is FUN!'
            elif ran_number5 == 46:
                sprint_tweet5 = ' Reading with you guys always makes my day!'
            elif ran_number5 == 47:
                sprint_tweet5 = ' Remember to get food and drink!'
            elif ran_number5 == 48:
                sprint_tweet5 = ' Remember- you have to eat and drink to live!'
            elif ran_number5 == 49:
                sprint_tweet5 = ' THIS SPRINT WAS AWESOME!'
            elif ran_number5 == 50:
                sprint_tweet5 = ' SO happy to be here with you all!'
        
        
            # part 2 generator
            if ran_number6 == 1:
                sprint_tweet6 = ' How many pages did you read?'
            elif ran_number6 == 2:
                sprint_tweet6 = ' How many pages did you end up reading?'
            elif ran_number6 == 3:
                sprint_tweet6 = ' How much did you get read?'
            elif ran_number6 == 4:
                sprint_tweet6 = ' How many chapters did you read?'
            elif ran_number6 == 5:
                sprint_tweet6 = ' Did you finish more than one chapter?'
            elif ran_number6 == 6:
                sprint_tweet6 = ' How much did you read?'
            elif ran_number6 == 7:
                sprint_tweet6 = ' Whats the title of your current read?'
            elif ran_number6 == 8:
                sprint_tweet6 = ' Whats your current read?'
            elif ran_number6 == 9:
                sprint_tweet6 = ' What book are you currently reading?'
            elif ran_number6 == 10:
                sprint_tweet6 = ' What book are you reading?'
            elif ran_number6 == 11:
                sprint_tweet6 = ' Have you finished a book recently?'
            elif ran_number6 == 12:
                sprint_tweet6 = ' What is the most recent book you finished?'
            elif ran_number6 == 13:
                sprint_tweet6 = ' Did you finish a book recently?'
            elif ran_number6 == 14:
                sprint_tweet6 = ' Whats the best book youve read this month?'
            elif ran_number6 == 15:
                sprint_tweet6 = ' Have you read any 5 star books this month?'
            elif ran_number6 == 16:
                sprint_tweet2 = ' Whats the most recent 5 star book youve read?'
            elif ran_number6 == 17:
                sprint_tweet6 = ' What book are you planning to read next?'
            elif ran_number6 == 18:
                sprint_tweet6 = ' Do you have plans for your next read?'
            elif ran_number6 == 19:
                sprint_tweet6 = ' If you have a next book planned, what is it?'
            elif ran_number6 == 20:
                sprint_tweet6 = ' Whats your favorite spot to read?'
            elif ran_number6 == 21:
                sprint_tweet6 = ' Do you have a favorite reading spot?'
            elif ran_number6 == 22:
                sprint_tweet6 = ' Where is your favorite reading spot?'
            elif ran_number6 == 23:
                sprint_tweet6 = ' Where is your favorite place to read?'
            elif ran_number6 == 24:
                sprint_tweet6 = ' Is your current read part of a series?'
            elif ran_number6 == 25:
                sprint_tweet6 = ' Is your book part of a series?'
            elif ran_number6 == 26:
                sprint_tweet6 = ' Whos your favorite character in your book?'
            elif ran_number6 == 27:
                sprint_tweet6 = ' Do you have a favorite character in your book?'
            elif ran_number6 == 28:
                sprint_tweet6 = ' Could you deal if you had to be best friends with the mc of your book?'
            elif ran_number6 == 29:
                sprint_tweet6 = ' Whats your reading beverage of choice?'
            elif ran_number6 == 30:
                sprint_tweet6 = ' Do you have a reading beverage of choice?'
            elif ran_number6 == 31:
                sprint_tweet6 = ' Tea or Coffee?'
            elif ran_number6 == 32:
                sprint_tweet6 = ' Whats your favorite candle scent?'
            elif ran_number6 == 33:
                sprint_tweet6 = ' Whats your favorite scent of candle?'
            elif ran_number6 == 34:
                sprint_tweet6 = ' Would you reccomend your book to others?'
            elif ran_number6 == 35:
                sprint_tweet6 = ' Would you reccomend your current read?'
            elif ran_number6 == 36:
                sprint_tweet6 = ' Describe your book with a gif.'
            elif ran_number6 == 37:
                sprint_tweet6 = ' Describe your book in 1 sentence.'
            elif ran_number6 == 38:
                sprint_tweet6 = ' Describe your book in 1 word'
            elif ran_number6 == 39:
                sprint_tweet6 = ' Describe your MC in 1 word.'
            elif ran_number6 == 40:
                sprint_tweet6 = ' Describe your MC with a gif.'
            elif ran_number6 == 41:
                sprint_tweet6 = ' What genre are you reading?'
            elif ran_number6 == 42:
                sprint_tweet6 = ' What is the genre of your book?'
            elif ran_number6 == 43:
                sprint_tweet6 = ' Is your book YA, middle-grade, or adult?'
            elif ran_number6 == 44:
                sprint_tweet6 = ' Do you prefer series or standalones?'
            elif ran_number6 == 45:
                sprint_tweet6 = ' Is your current read a standalone?'
            elif ran_number6 == 46:
                sprint_tweet6 = ' Do you prefer physical, ebook, or audiobook?'
            elif ran_number6 == 47:
                sprint_tweet6 = ' Do you generally read physical, ebooks, or audiobooks?'
            elif ran_number6 == 48:
                sprint_tweet6 = ' Do you usually take part in readathons?!'
            elif ran_number6 == 49:
                sprint_tweet6 = ' What is the last readathon you participated in?'
            elif ran_number6 == 50:
                sprint_tweet6 = ' Any big ideas for future readathons?'
            




            sprint_tweet_master_end = (sprint_tweet4 + sprint_tweet5 + sprint_tweet6)
            print (sprint_tweet_master_end)
            api.update_status(sprint_tweet_master_end)

while True:
    reply_to_tweets()
    time.sleep(15)

# mentions = api.mentions_timeline()

# for mention in mentions:
#   print(str(mention.id) + ' - ' + mention.text)
#   if '#housecupathon' in mention.text.lower():
#     print ('found #housecupathon')

