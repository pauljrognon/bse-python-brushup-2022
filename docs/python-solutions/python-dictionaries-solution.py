#
# INSTRUCTIONS:
# For this exercise we will work with a
# "scoreboard" for an imaginary game.
# You will be required to write functions
# that operate on the "scoreboard" data
# structure and compute certain results.



######################################
# TUPLES
#
# For these functions, the "scoreboard"
# will be a list of tuples, where each
# tuple is of the form (str, int)
# representing (player_name, score)
#
# For example:
# [('kewld00d1', 100), ('pumpkin', 550)]
######################################


#
# 1)
# Create a function "get_scores"
# that has one parameter, the scoreboard,
# and returns a list of the same size
# with just the scores for each player
# (a list of ints)

def get_scores(scoreboard):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.')
    return [player[1] for player in scoreboard]

#
# 2)
# Create a function "top_score"
# that has one parameter, the scoreboard,
# and returns an int, the highest score
# on the scoreboard

def __max__(li: list):
    pointer = li[0]
    for x in li:
        if x > pointer:
            pointer = x
    return pointer

def top_score(scoreboard):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.')    
    scores = get_scores(scoreboard)
    return __max__(scores)

#
# 3)
# Create a function "top_player"
# that has one parameter, the scoreboard,
# and returns the player_name that has
# the highest score

def top_player(scoreboard):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.')
    player_name = None
    score_max = top_score(scoreboard)
    for player in scoreboard:
        if player[1] == score_max:
            player_name = player[0]
            break
    return player_name

######################################
# DICTIONARIES
#
# For these functions, the "scoreboard"
# will be a list of dictionaries, where each
# dictionary represents information
# about a single player.
#
# The keys of the dictionary are:
# "player", "score", "country", "levels"
#
# For example, one dictionary:
#
# {
#    'player': 'tr0llhuntah',
#    'score': 200,
#    'country': 'no',
#    'levels': ['Choco Mountain', 'Rainbow Road']
# }
#
######################################


#
# 4)
# Create a function "top_player_from_dict"
# that has one parameter, the scoreboard,
# and returns the player_name that has
# the highest score

def top_player_from_dict(scoreboard):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.') 
    scoreboard_tup= [(player['player'], player['score']) for player in scoreboard]
    return top_player(scoreboard_tup)

#
# 5)
# Create a function "get_good_players"
# that has two parameters:
# 1. scoreboard
# 2. an int (limit)
#
# "get_good_players" returns a list of
# strings, with the names of the players
# who have a score greater than or equal to
# limit.

def get_good_players(scoreboard, limit):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.') 
    return [player['player'] for player in scoreboard if player['score'] >= limit]

#
# 6)
# Create a function "top_player_by_country"
# that has two parameters:
# 1. scoreboard
# 2. a string (country)
#
# "top_player_by_country" returns a string
# with the name of the player with the highest
# score in the provided country.

def top_player_by_country(scoreboard, country):
    return top_player_from_dict([player for player in scoreboard if player['country'] == country])

#
# 7)
# Create a function "most_levels_played"
# that has one parameter: "scoreboard".
# and returns a tuple (str, int) with the name of
# the player that has played the most levels
# and the number of levels they played

def most_levels_played(scoreboard):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.') 
    #let's consider number of levels as scores
    players= [(player['player'], len(player['levels'])) for player in scoreboard]
    return top_player(players), top_score(players)

#
# 8)
# Create a function "played_levels"
# that has one parameter: "scoreboard".
# and returns a list of strings with the
# names of all the levels that have been
# played by any user.
#
# The list of levels can have duplicates.

def played_levels(scoreboard):
    if len(scoreboard) == 0:
        raise ValueError('The scoreboard is empty.')
    levels = []
    for player in scoreboard:
        levels += player['levels']
    return levels

######################################
# BONUS QUESTIONS
######################################

#
# 9)
# Create a function "distinct" that
# takes a list of elements and returns
# a list of only the unique elements.
#
# Example:
# [1,2,2,2,1,3] -> [1,2,3]
#
# NOTE: Use only the tools we have learned
# so far:
# dictionaries, lists, for loop, try/except

def distinct(li):
    if len(li) == 0:
        raise ValueError('The list is empty.')
    unique = []
    for elem in li:
        if elem in unique:
            pass
        else:
            unique.append(elem)
    return unique

#
# 10)
# Create a function "distinct_played_levels"
# That is just like "played_levels" except
# that it returns a list of the unique
# levels played (a list without duplicates)
#
# HINT: just use the two functions you've
# already written!

def distinct_played_levels(scoreboard):
    return distinct(played_levels(scoreboard)) 

#
# 11)
# Modify your function "top_player_by_country":
#
# Now, the second parameter ("country") should
# be either the country code OR None. If it
# is None, the function should return the top
# player across all countries

def top_player_by_country(scoreboard, country):
    if country is None:
        return top_player_from_dict(scoreboard)
    else:
        return top_player_from_dict([player for player in scoreboard if player['country'] == country])

# 12)
# Create a function called "country_leaderboard"
#
# This function will return a "leaderboard" that
# provides information about the top player
# per country.
#
# The "leaderboard" should be a dictionary.
# See the test_exercises.py file for the format.

def country_leaderboard(scoreboard):
    countries = distinct([player['country'] for player in scoreboard])
    top_players = [{'country': country, 'player': top_player_by_country(scoreboard, country)} for country in countries] 
    top_scores = [player['score'] for player in scoreboard if {'country': player['country'], 'player': player['player']} in top_players]
    leaderboard = {}
    for i in range(len(top_players)):
        leaderboard[top_players[i]['country']] = {'player': top_players[i]['player'], 'score': top_scores[i]}
    return leaderboard