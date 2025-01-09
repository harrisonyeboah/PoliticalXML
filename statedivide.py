

import matplotlib.pyplot as pyplot
#import matplotlib.ticker as ticker
#from matplotlib.ticker import MultipleLocator
from utilities import getVoteFileFromWeb, STATES

def stateDivide(state):
    demRepEachYear = []
    repRepEachYear = []
    
    assert state in STATES
    
    for year in range(2004, 2024):
        numberOfDemRep = 0
        numberOfRepRep = 0
        lines = (getVoteFileFromWeb("https://clerk.house.gov/cgi-bin/vote.asp?year="+str(year)+"&rollnumber=001"))
        for line in lines:
            if ("<recorded-vote>" and str(state)) in line:
                if 'party="R"' in line:
                    numberOfRepRep += 1
                elif 'party="D"' in line:
                    numberOfDemRep += 1
        demRepEachYear.append(numberOfDemRep)
        repRepEachYear.append(numberOfRepRep)

    pyplot.title("Distribution for Congretional Repesentative for " + str(state) + ' from 2004-2023')
    pyplot.xlabel('Year')    
    pyplot.ylabel('Number of Representatives')
    pyplot.plot(range(2004, 2024), demRepEachYear, color='blue', label='Democrat')
    pyplot.plot(range(2004, 2024), repRepEachYear, color='red', label='Republican')
    #pyplot.xaxis.set_major_locator(ticker.MultipleLocator(2))
    #pyplot.yaxis.set_major_locator(ticker.MultipleLocator(2))

    pyplot.legend()
    pyplot.show()


    return

stateDivide('IL')