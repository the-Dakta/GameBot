#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import io
import tweepy
import time
import urllib2
from random import randint
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


list1file = open('genres_list.json')
#     "https://raw.githubusercontent.com/the-Dakta/GameBot/master/genres_list."
#     "json")

list1read = list1file.read()

list2file = open('games_list.json')
#     "https://raw.githubusercontent.com/the-Dakta/GameBot/master/games_list."
#     "json")

list2read = list2file.read()

# Create Python-readable lists of items in JSON files
list1 = json.loads(list1read)["genres"]
list2 = json.loads(list2read)["games_list"]


# Repeatable game idea generator
idealist = []
counter = 0

while counter < 200:  # Change 2 to however many games you want to produce

    # Pick random numbers
    list1num = randint(0, len(list1) - 1)
    list2num = randint(0, len(list2) - 1)
    list3num = randint(0, len(list2) - 1)

    # Choose random items from each list using random numbers
    first = list1[list1num]  # Syntax: list[number]
    second = list2[list2num]
    third = list2[list3num]

    # Fill in the blanks of the poem
    idea = 'It\'s %s game that\'s like %s + %s! #gameideas #gamedev'  \
           % (first, second, third)

    print idea
    idealist.append(idea)  # add to long list of game ideas
    counter = counter + 1


# Line up tweets for bot

for line in idealist:
    api.update_status(line)
    # print line
    time.sleep(1800)  # Sleep for 30 minutes


print '[All done!]'
