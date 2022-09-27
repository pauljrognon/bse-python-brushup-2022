#
# 1)
# Create a new file called 'tweet_data.py'
# and create a function called "load_tweets".
# The function should have one parameter:
# a string which is the relative path of a
# file in "json lines" format.
#
# The function should open that file and
# parse each line as JSON, returning a
# list of dictionaries.

from tweet_data import load_tweets

#
# 2)
# Twitter records the language of each tweet in
# a key called "lang". The language is represented
# by a 2-character code recorded as a string,
# i.e.: "en" or "ca" or "es"
#
# Create a function called "get_language_counts"
# which takes a list of "tweets" (dictionaries)
# and returns a dictionary where the keys are
# language codes ("es", "ca", "en") and the
# values are integers representing the number
# of tweets in that language.
#
# For example: { 'es': 5, 'ca': 3 }

def get_language_counts(tweets):
    if tweets:
        langs = [tweet['lang'] for tweet in tweets if 'lang' in tweet.keys()]
        lang_counts = count_occurances(langs)
        return lang_counts
    else:
        raise ValueError("The dictionary of tweets is empty.")

##################################
# BONUS QUESTIONS
##################################

#
# 3)
# Twitter records the hashtags of a tweet
# under a key called "entities".
#
# Explore the format of the tweet dictionary
# (HINT: use the interactive python interpreter)
# and find out how to get the hashtags, as a
# string, from the "entities" dictionary
# (which holds many other things besides just
# hashtags).
#
# Create a function, called "get_hashtag_counts"
# that returns a dictionary where the keys
# are the hashtags and the values are integers
# representing the number of times that hashtag
# occured.

def get_hashtag_counts(tweets):
    if tweets:
        hashtags = [hashtag['text'] for tweet in tweets for hashtag in tweet['entities']['hashtags'] if 'entities' in tweet.keys()]
        hashtag_counts = count_occurances(hashtags)
        return hashtag_counts
    else:
        raise ValueError("The dictionary of tweets is empty.")

#
# 4)
# You should notice that the last two functions
# do very similar things (count occurences of items).
#
# Remember the concept of DRY code? The two functions
# probably contain code that looks very similar. Indeed,
# you have probable "repeated yourself".
#
# This exercise consists in making your code more DRY.
#
# "Refactoring" is the act of rewriting the implementation
# of your code without changing the interface or the
# functionality.
#
# Refactor the last two functions to be DRYer.
#
# Create a helper function, called "count_occurences"
# that can be used by both functions to remove
# repeated code and make the functions simpler.
#
# NOTE: There are no tests for this exercise!

def count_occurances(li):
    counts = {}
    for elem in li:
            counts[elem] = 1 if elem not in counts.keys() else counts[elem] + 1
    return counts