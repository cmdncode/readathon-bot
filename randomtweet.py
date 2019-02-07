from random import randint
import random

# generate 3 random numbers
part1 = ''
part2 = ''
part3 = ''

# 1
ran_number1 = (randint(1, 50))
print (ran_number1)
# ran_number1 = 1
# 2
ran_number2 = (randint(1, 50))
print (ran_number2)
# 3
ran_number3 = (randint(1, 50))
print (ran_number3)

#define length 
length = (random.choice([15, 30, 45, 60])) 

# Length portion of tweet

if length == 15:
  generic = 'This has been a 15 min sprint'
elif length == 30:
  generic = 'This has been a 30 min sprint'
elif length == 45:
  generic = 'This has been a 45 min sprint'
elif length == 60:
  generic = 'This has been a 60 min sprint'
else:
  generic = 'This has been a sprint!'

# part 1 generator
if ran_number1 == 1:
  part1 = 'Stop Reading!' 
elif ran_number1 == 2:
  part1 = 'Thats it!' 
elif ran_number1== 3:
  part1 = 'Alright guys!' 
elif ran_number1 == 4:
  part1 = 'Times up!' 
elif ran_number1 == 5:
  part1 = 'OK STOP!' 
elif ran_number1 == 6:
  part1 = 'Time to stop reading!' 
elif ran_number1 == 7:
  part1 = 'Reading times up!' 
elif ran_number1 == 8:
  part1 = 'STOP!' 
elif ran_number1 == 9:
  part1 = 'K stop!!' 
elif ran_number1 == 10:
  part1 = 'Sprints over!' 
elif ran_number1 == 11:
  part1 = 'Sprint has finished!' 
elif ran_number1 == 12:
  part1 = 'Stop sprinting!' 
elif ran_number1 == 13:
  part1 = 'Sprint has ended!' 
elif ran_number1 == 14:
  part1 = 'Read no more!' 
elif ran_number1 == 15:
  part1 = 'No more reading!' 
elif ran_number1 == 16:
  part1 = 'End of sprint!' 
elif ran_number1 == 17:
  part1 = 'Time is up!' 
elif ran_number1 == 18:
  part1 = 'Time to end this sprint!' 
elif ran_number1 == 19:
  part1 = 'Break time!' 
elif ran_number1 == 20:
  part1 = 'Time for a break!' 
elif ran_number1 == 21:
  part1 = 'Even the best sprinters need to stop sprinting!' 
elif ran_number1 == 22:
  part1 = 'Youve crossed the finish line!' 
elif ran_number1 == 23:
  part1 = 'Youve reached the end of the sprint!' 
elif ran_number1 == 24:
  part1 = 'Set down your book!' 
elif ran_number1 == 25:
  part1 = 'Stop turning pages!' 
elif ran_number1 == 26:
  part1 = 'No more page turning!' 
elif ran_number1 == 27:
  part1 = 'No more reading pages!' 
elif ran_number1== 28:
  part1 = 'Stop reading pages!' 
elif ran_number1 == 29:
  part1 = 'Stop for now!' 
elif ran_number1 == 30:
  part1 = 'Thats all folks!' 
elif ran_number1 == 31:
  part1 = 'STAAHHHHPP!' 
elif ran_number1 == 32:
  part1 = 'You shall read no longer!' 
elif ran_number1 == 33:
  part1 = 'Set your book down!' 
elif ran_number1 == 34:
  part1 = 'HALT! Stop readin!' 
elif ran_number1 == 35:
  part1 = 'No more! Stop reading!' 
elif ran_number1 == 36:
  part1 = 'YOU! Stop reading!' 
elif ran_number1 == 37:
  part1 = 'You there! No more reading!' 
elif ran_number1 == 38:
  part1 = 'Stoppp!!!' 
elif ran_number1 == 39:
  part1 = 'NO MORE READING!' 
elif ran_number1 == 40:
  part1 = 'Thats it for this sprint!' 
elif ran_number1 == 41:
  part1 = 'Thats all for this sprint!' 
elif ran_number1 == 42:
  part1 = 'Congrats! You survived the sprint!' 
elif ran_number1 == 43:
  part1 = 'PAUSE!' 
elif ran_number1 == 44:
  part1 = ' Reading on hold!' 
elif ran_number1 == 45:
  part1 = ' Pause your reading! Sprint over!' 
elif ran_number1 == 46:
  part1 = ' FREEZE!' 
elif ran_number1 == 47:
  part1 = ' Dont read any more!' 
elif ran_number1 == 48:
  part1 = ' Dont stop reading forever, but stop for now!' 
elif ran_number1 == 49:
  part1 = ' We have stopped the sprint!' 
elif ran_number1 == 50:
  part1 = ' Theres no more reading! Sprint complete!' 

# part 2 generator
if ran_number2 == 1:
  part2 = ' Hope you got a lot read!' 
elif ran_number2 == 2:
  part2 = ' I hope you had fun!' 
elif ran_number2== 3:
  part2 = ' I hope your plot is speeding!' 
elif ran_number2 == 4:
  part2 = ' I hope you enjoyed!' 
elif ran_number2 == 5:
  part2 = ' I hope to host another soon!' 
elif ran_number2 == 6:
  part2 = ' Dont forget anyone can start a sprint!' 
elif ran_number2 == 7:
  part2 = ' Dont forget you can start a sprint anytime!' 
elif ran_number2 == 8:
  part2 = ' Glad to have hosted this sprint!' 
elif ran_number2 == 9:
  part2 = ' I hope you all did well!' 
elif ran_number2 == 10:
  part2 = ' Join us for another sprint soon!' 
elif ran_number2 == 11:
  part2 = ' Join us again soon for more sprints!' 
elif ran_number2 == 12:
  part2 = ' Dont wait for someone else to start one, start a sprint yourself!' 
elif ran_number2 == 13:
  part2 = ' Thanks for participating in tbhis sprint!' 
elif ran_number2 == 14:
  part2 = ' Remember to spead the word about these sprints!' 
elif ran_number2 == 15:
  part2 = ' Sprints are no fun without friends! Spread the word!' 
elif ran_number2 == 16:
  part2 = ' Remember to RT to get more involved with these reading sprints' 
elif ran_number2 == 17:
  part2 = ' Tell your friends about these sprints!' 
elif ran_number2 == 18:
  part2 = ' Hope to see you again soon!' 
elif ran_number2 == 19:
  part2 = ' Be responsible and take breaks!' 
elif ran_number2 == 20:
  part2 = ' Time for a snack!' 
elif ran_number2 == 21:
  part2 = ' You deserve a break!' 
elif ran_number2 == 22:
  part2 = ' Hope you are flying through your book!' 
elif ran_number2 == 23:
  part2 = ' Sprinting is much more fun without sweating huh?' 
elif ran_number2 == 24:
  part2 = ' Im glad our sprints dont include actual physical activity!' 
elif ran_number2 == 25:
  part2 = ' Join us for another soon, or just start one yourself!' 
if ran_number2 == 26:
  part2 = ' Get your friends on board! SHARE!' 
elif ran_number2 == 27:
  part2 = ' Thanks for showing up!' 
elif ran_number2== 28:
  part2 = ' Thanks for sprinting with us!' 
elif ran_number2 == 29:
  part2 = ' We always enjoy sprinting with you guys!' 
elif ran_number2 == 30:
  part2 = ' Sprinting can be tiring, remember to take breaks!' 
elif ran_number2 == 31:
  part2 = ' Phew!' 
elif ran_number2 == 32:
  part2 = ' You shall read no longer!' 
elif ran_number2 == 33:
  part2 = ' Set your book down!' 
elif ran_number2 == 34:
  part2 = ' HALT! Stop readin!' 
elif ran_number2 == 35:
  part2 = ' No more! Stop reading!' 
elif ran_number2 == 36:
  part2 = ' YOU! Stop reading!' 
elif ran_number2 == 37:
  part2 = ' You there! No more reading!' 
elif ran_number2 == 38:
  part2 = ' Stoppp!!!' 
elif ran_number2 == 39:
  part2 = ' NO MORE READING!' 
elif ran_number2 == 40:
  part2 = ' Thats it for this sprint!' 
elif ran_number2 == 41:
  part2 = ' Thats all for this sprint!' 
elif ran_number2 == 42:
  part2 = ' Congrats! You survived the sprint!' 
elif ran_number2 == 43:
  part2 = ' PAUSE!' 
elif ran_number2 == 44:
  part2 = ' Reading on hold!' 
elif ran_number2 == 45:
  part2= ' Pause your reading! Sprint over!' 
elif ran_number2 == 46:
  part2 = ' FREEZE!' 
elif ran_number2 == 47:
  part2 = ' Dont read any more!' 
elif ran_number2 == 48:
  part2 = ' Dont stop reading forever, but stop for now!' 
elif ran_number2 == 49:
  part2 = ' We have stopped the sprint!' 
elif ran_number2 == 50:
  part2 = ' Theres no more reading! Sprint complete!' 

# question generator
if ran_number3 == 1:
  part3 = ' How many pages did you read?' 
elif ran_number3 == 2:
  part3 = ' How many pages did you end up reading?' 
elif ran_number3== 3:
  part3 = ' How much did you get read?' 
elif ran_number3 == 4:
  part3 = ' How many chapters did you read?' 
elif ran_number3 == 5:
  part3 = ' Did you finish more than one chapter?' 
elif ran_number3 == 6:
  part3 = ' How much did you read?'
elif ran_number3 == 7:
  part3 = ' Whats the title of your current read?' 
elif ran_number3 == 8:
  part3 = ' Whats your current read?' 
elif ran_number3 == 9:
  part3 = ' What book are you currently reading?' 
elif ran_number3 == 10:
  part3 = ' What book are you reading?' 
elif ran_number3 == 11:
  part3 = ' Have you finished a book recently?' 
elif ran_number3 == 12:
  part3 = ' What is the most recent book you finished?' 
elif ran_number3 == 13:
  part3 = ' Did you finish a book recently?' 
elif ran_number3 == 14:
  part3 = ' Whats the best book youve read this month?' 
elif ran_number3 == 15:
  part3 = ' Have you read any 5 star books this month?' 
elif ran_number3 == 16:
  part3 = ' Whats the most recent 5 star book youve read?' 
elif ran_number3 == 17:
  part3 = ' What book are you planning to read next?' 
elif ran_number3 == 18:
  part3 = ' Do you have plans for your next read?' 
elif ran_number3 == 19:
  part3 = ' If you have a next book planned, what is it?' 
elif ran_number3 == 20:
  part3 = ' Whats your favorite spot to read?' 
elif ran_number3 == 21:
  part3 = ' Do you have a favorite reading spot?' 
elif ran_number3 == 22:
  part3 = ' Where is your favorite reading spot?' 
elif ran_number3 == 23:
  part3 = ' Where is your favorite place to read?' 
elif ran_number3 == 24:
  part3 = ' Is your current read part of a series?' 
elif ran_number3 == 25:
  part3 = ' Is your book part of a series?' 
if ran_number3 == 26:
  part3 = ' Whos your favorite character in your book?' 
elif ran_number3 == 27:
  part3 = ' Do you have a favorite character in your book?' 
elif ran_number3 == 28:
  part3 = ' Could you deal if you had to be best friends with the mc of your book?' 
elif ran_number3 == 29:
  part3 = ' Whats your reading beverage of choice?' 
elif ran_number3 == 30:
  part3 = ' Do you have a reading beverage of choice?' 
elif ran_number3 == 31:
  part3 = ' Tea or Coffee?' 
elif ran_number3 == 32:
  part3 = ' Whats your favorite candle scent?' 
elif ran_number3 == 33:
  part3 = ' Whats your favorite scent of candle?' 
elif ran_number3 == 34:
  part3 = ' Would you reccomend your book?' 
elif ran_number3 == 35:
  part3 = ' Would you reccomend your current read?' 
elif ran_number3 == 36:
  part3 = ' Describe your book in 1 sentence.' 
elif ran_number3 == 37:
  part3 = ' Describe your book with a gif.' 
elif ran_number3 == 38:
  part3 = ' Describe your book in 1 word.' 
elif ran_number3 == 39:
  part3 = ' Describe your MC in 1 word.' 
elif ran_number3 == 40:
  part3 = ' Describe your MC with a gif.' 
elif ran_number3 == 41:
  part3 = ' What genre are you reading?' 
elif ran_number3 == 42:
  part3 = ' What is the genre of your book?' 
elif ran_number3 == 43:
  part3 = ' Is your book YA, middle-grade, or adult?' 
elif ran_number3 == 44:
  part3 = ' Do you prefer series or standalones?' 
elif ran_number3 == 45:
  part3 = ' Is your current read a standalone?' 
elif ran_number3 == 46:
  part3 = ' Do you prefer physical, ebook, or audiobook?' 
elif ran_number3 == 47:
  part3 = ' Do you generally read physical, ebooks, or audiobooks?' 
elif ran_number3 == 48:
  part3 = ' Do you usually take part in readathons?' 
elif ran_number3 == 49:
  part3 = ' What is the last readathon you participated in?' 
elif ran_number3 == 50:
  part3 = ' Any big ideas for future readathons?'


# promo tags addition
promo_tags = '#reading #readingsprint'

sprint_tweet = (generic + part1 + part2 + part3 + promo_tags)
print (sprint_tweet)
