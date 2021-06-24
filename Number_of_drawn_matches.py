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
    urlA = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year)
    resA = requests.get(urlA)
    resultA = json.loads(resA.content)
    #print(resultA)
    current = 1
    total = 0 
    url_pages = resultA['total_pages']
    #print(url_pages)
    for i in range(0,12):
        urlA = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={2}".format(year,i,i)
        resA = requests.get(urlA)
        resultA = json.loads(resA.content)
        print(resultA['total'])
        total += resultA['total']
    return total    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = getNumDraws(year)

    fptr.write(str(result) + '\n')

    fptr.close()
