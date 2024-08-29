import requests

isFollowed = {}

urllist = []

URL = "https://www.kali.org/"

#page = requests.get(URL)

def isFollowedCheck(URL):
    for key in isFollowed.keys():
        if key != URL:
            return False
        else:
            if isFollowed[URL] == "yes":
                return True
            else:
                return False

def checkURL(URL):
    if URL in urllist:
        return True
    else:
        return False
    
urllist.append(URL)

for URL in urllist:
    if isFollowedCheck(URL) != True:
        page = requests.get(URL)
        isFollowed[URL] = "yes"

        start = "https"

        for line in page.text.split("\n"):
            if "https" in line:
                if "kali" in line:
                    if ">" in line:
                        end = ">"
                    else:
                        end = "/ "
                    sliced = (line[line.index(start):line.index(end)])
                    if " " in sliced:
                        end = " "
                        parsed = (sliced[sliced.index(start):sliced.index(end)])
                    else:
                        parsed = (sliced)

                    if checkURL(parsed) == False:
                        urllist.append(parsed)
                        isFollowed[parsed] = "no"

for URL in urllist:
    print(URL)