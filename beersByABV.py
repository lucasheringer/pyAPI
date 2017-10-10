#!/usr/bin/env python2.7

################################################
## Script to read a json from a URL and print
## only beers with ABV greater than set as parameter
## print Beer Name and ABV sorted by ABV
## Created by Lucas Heringer 26/09/2017
################################################

import os, sys, json, urllib, argparse
from operator import itemgetter

# Json URL
url = "https://api.punkapi.com/v2/beers"
beer_list = []

parser = argparse.ArgumentParser(description='Beers, ABV\'s and other stuff')
parser.add_argument('--abv', type=float, help='abv help')
args = parser.parse_args()

#Checking if argument was provided and greater than 0
if args.abv > 0.0:
    minABV = args.abv
else:
    minABV = 0.0

#Reading Json from http
def getJson():
    tries = 5
    while tries >= 0:
        try:
            response = urllib.urlopen(url)
            data = json.loads(response.read())
            return data
        except ValueError:
            if tries == 0:
                print(ValueError)
            else:
                time.sleep(1)
                tries -= 1
                continue

data = getJson()

#reading json and selecting only the ones with abv greater than minABV
for item in data:
    if (item['abv'] >= minABV):
        #print item['name']+", " + (str(item['abv']))
        beer_list.append({'name': item['name'].encode('ascii', 'replace'), 'abv': item['abv']})

#Sorting beer list
beer_sorted = sorted(beer_list, key=lambda beer: beer['abv'])

for beer in beer_sorted:
    print beer['name'] + ", " + (str(beer['abv']))
