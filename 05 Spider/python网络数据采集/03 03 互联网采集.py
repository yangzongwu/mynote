from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


def getInternalLink(bsObj):
    internalLink = []
    for link in bsObj.findAll('a', href=re.compile("^(/|.*" + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLink:
                internalLink.append(link.attrs['href'])
    return internalLink


def getExternalLink(bsObj, excludeUrl):
    externalLink = []
    for link in bsObj.findAll('a', href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLink:
                externalLink.append(link.attrs['href'])
    return externalLink


def splitAddress(address):
    addressParts = address.replace("http://", "").split('/')
    return addressParts


def getRandomExternalLine(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLink(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLink(bsObj)
        return getExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)], "")
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followingExternalOnly(startingSite, n):
    if n == 0:
        return
    externalLink = getRandomExternalLine(startingSite)
    print("random external link:" + externalLink)
    followingExternalOnly(externalLink, n - 1)


followingExternalOnly("https://www.taobao.com/", 3)
