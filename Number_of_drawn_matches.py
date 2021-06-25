#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'getNumDraws' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
import requests         
import json

def getNumDraws(year):
    urlA = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year)  #int to string conversion
    resA = requests.get(urlA)           #request for team1
    resultA = json.loads(resA.content)   #data fetching for team1
    #print(resultA)
    current = 1   #current value taken as 1
    total = 0     # total value defined zero initially
    url_pages = resultA['total_pages']   #getting total pages value for further looping
    #print(url_pages)
    for i in range(0,12):
        urlA = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={2}".format(year,i,i)
        resA = requests.get(urlA)
        resultA = json.loads(resA.content)         #Getting year goal value from the data 
        print(resultA['total'])                   
        total += resultA['total']
    return total    #returning the total value
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
