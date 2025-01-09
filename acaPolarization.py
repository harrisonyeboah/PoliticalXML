'''
A program that uses functions in `utilities.py` to compute whether the 
Affordable Care Act was a party line vote or not.

Authors: <your name>
Date Created: 
'''

# The following import state has been included for this file only.
# You may have to write similar import statements in your other files.
from utilities import countVotesByParty, isPartyLine

"""
Lookes through the aca file and determans if it is a party line

Input: non
Output: true or faluse
"""


def isACAPolarized():

    fileObject = open('aca.xml', "r", encoding='utf-8')
    rawfile = fileObject.read()
    rawfilebyline = rawfile.splitlines()
    fileObject.close

    votes = countVotesByParty(rawfilebyline)
    
    ACAIsPolorized = isPartyLine(votes[0],votes[1],votes[2],votes[3])

    return ACAIsPolorized
print(isACAPolarized())