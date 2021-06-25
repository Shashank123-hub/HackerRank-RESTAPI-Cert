#!/bin/python3

import math
import os
import random
import re
import sys
import requests    #requests and json are required for data fetching 
import json

def getTotalGoals(team, year):
    urla = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team1=" + team   #url for team1
    urlb = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year) + "&team2=" + team   #url for team2
    res1 = requests.get(urla)           #getting data from url(team1)
    result1 = json.loads(res1.content)      #gtting data into json format
    res2 = requests.get(urlb)           #getting data for team2
    result2 = json.loads(res2.content)
    # print(result1) 
    # print(result2)
    curr_1 = 1   #current value for goal specified 1
    total_url_1 = result1['total_pages']    #getting total pages value(urla)
    curr_2 = 1
    total_url_2 = result2['total_pages']    #getting total pages value(urlb)

    total = 0     #total value specified as 0(to be updated and returned later)
    while curr_1 <= total_url_1:      #Looping for value of team1
        urla = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1={1}&page={2}".format(year,team,curr_1)
        res1 = requests.get(urla)
        result1 = json.loads(res1.content)
        for i in result1['data']:
            if i['team1'].upper() == team.upper():   #Loop for validating team name
                total += int(i['team1goals'])    #updating total value
        curr_1 += 1        #updating current value
    # print(total)

    while curr_2 <= total_url_2:      #Looping for value of team2
        url2 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team2={1}&page={2}".format(year,team,curr_2)
        res2 = requests.get(url2)
        result2 = json.loads(res2.content)
        for i in result2['data']:
            if i['team2'].upper() == team.upper():
                total += int(i['team2goals'])
        curr_2 += 1
    return total
    

if __name__ == '__main__':
