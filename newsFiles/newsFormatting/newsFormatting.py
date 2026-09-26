import json


def newsFormatting(lst):
    newNewsList = []
    for article in lst:
        newNewsList.append(
            {
                "title": article["title"],
                "description": article["description"],
                "content": article["content"],
            }
        )
    file = open("newsFiles/files/tempData.json", "w")
    file.write(((str(newNewsList))))
