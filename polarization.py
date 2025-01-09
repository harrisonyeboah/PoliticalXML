
from explorePolarization import isMyChoicePolarized
from urllib.error import HTTPError
import matplotlib.pyplot as pyplot

def countPartyLine(year, maxNumber):

    votePolarized = 0
    voteNotPolarized = 0
    persentagePolarized = 0.0

    for num in range(1,maxNumber):
        try:
            if(isMyChoicePolarized(year, num)):
                votePolarized += 1
            else:
                voteNotPolarized += 1
        except HTTPError:
            votePolarized = votePolarized

    percentagePolarized = votePolarized/(votePolarized+voteNotPolarized)

    return percentagePolarized

def plotPartyLine():
    xPlot = []
    yPlot = []
    for index in range (2004, 2023):
        result = countPartyLine(index, 10)
        print(result)
        print(index)
        xPlot.append(index)
        yPlot.append(result)
        pyplot.plot(xPlot, yPlot)
    pyplot.title("Proportion of Polarized from 2004 to 2023")
    pyplot.ylabel("Percentage")
    pyplot.xlabel("Year")
    pyplot.show()



    return

plotPartyLine()

