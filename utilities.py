import urllib.request as web

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def countVotesByParty(lines):
    demYes = 0
    demNo = 0
    repYes = 0
    repNo = 0

    for line in lines:
        if "recorded-vote" in line:
            if ('party="D" ' in line) and (('>Yea<' in line) or ('>Aye<' in line)):
                demYes += 1
            elif ('party="D" ' in line) and (('>Nay<' in line) or ('>No<' in line)):
                demNo += 1
            elif ('party="R" ' in line) and (('>Yea<' in line) or ('>Aye<' in line)):
                repYes += 1
            elif ('party="R" ' in line) and (('>Nay<' in line) or ('>No<' in line)):
                repNo += 1

    listOfYeaAndNae = []
    listOfYeaAndNae.append(demYes)
    listOfYeaAndNae.append(demNo)
    listOfYeaAndNae.append(repYes)
    listOfYeaAndNae.append(repNo)


    return listOfYeaAndNae


def isPartyLine(demYes, demNo, repYes, repNo):

    try:
        1/(demNo+demYes+repNo+repYes)
    except ZeroDivisionError:
        return False

    if (demYes/(demYes+demNo) > .5 and repNo/(repYes+repNo) > .5) or (demNo/(demYes+demNo) > .5 and repYes/(repYes+repNo) > .5):
        return True
    else:
        return False
 

    
def getVoteFileFromWeb(url):
    '''
    This function downloads a temporary copy of a voting record file from the url
    and returns a list of lines representing each line in the file.
    
    Parameters: url: a string containing the address to download the voting data file from.

    Your url should be of the format: "https://clerk.house.gov/cgi-bin/vote.asp?year=<YEAR>&rollnumber=<NUMBER>"

    where <YEAR> and <NUMBER> are the year and roll-call number of the vote you want to obtain.

    Outputs: returns a list of the lines in the file obtained from the website
    '''
    webpage = web.urlopen(url)
    decodedLines = [line.decode('utf-8').rstrip() for line in webpage]
    webpage.close()
    return decodedLines
