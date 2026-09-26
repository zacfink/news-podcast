import json
from newsGetter.googleNews.googleNews import googleNews
from newsGetter.mediastack.mediastack import mediastack
from newsGetter.newsAPI.newsAPI import newsAPI
from newsGetter.newsData.newsData import newsData
from newsFiles.newsFormatting.newsFormatting import newsFormatting
from newsFiles.newsFormatting.aiSummarize import formatPoints
from newsFiles.script.scriptFormatting.scriptFormatting import scriptSummarize
from readScript.readScript import readScript


def combineAllPoints(dir="newsFiles/files/data.json"):
    file = open(dir, "w")

    pointsList = []

    newsFormatting(googleNews())
    googleNewsFormatted = formatPoints()
    pointsList.append(googleNewsFormatted)
    newsFormatting(mediastack())
    mediastackFormatted = formatPoints()
    pointsList.append(mediastackFormatted)
    newsFormatting(newsAPI())
    newsAPIFormatted = formatPoints()
    pointsList.append(newsAPIFormatted)
    newsFormatting(newsData())
    newsDataFormatted = formatPoints()
    pointsList.append(newsDataFormatted)

    file.write(json.dumps(pointsList))


def main():
    combineAllPoints()
    scriptSummarize()
    readScript()


main()
