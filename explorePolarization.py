'''
A program that uses functions in `utilities.py` to compute whether a vote of 
the student's choosing was a party line vote.

Authors: <your name>
Date Created: 
'''
from utilities import getVoteFileFromWeb, countVotesByParty, isPartyLine

def isMyChoicePolarized(year, number):

    goodNumber = ""
    if number < 10:
        goodNumber = "00" + str(number)
    elif number < 100:
        goodNumber = "0" + str(number)
    else:
        goodNumber = str(number)

    lines = getVoteFileFromWeb("https://clerk.house.gov/evs/"+ str(year) +"/roll"+goodNumber+".xml")

    votes = countVotesByParty(lines)
    
    Polarized = isPartyLine(votes[0],votes[1],votes[2],votes[3])

    return Polarized

print(isMyChoicePolarized(2013, 200))