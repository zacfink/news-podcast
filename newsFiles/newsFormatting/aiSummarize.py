from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()


def aiSummarize(dir="newsFiles/files/tempData.json"):
    with open(dir, "r") as file:
        content = file.read()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": f"You will summarize the most important news information given into 12 points:\n\n{json.dumps(content)} \n\n DO NOT INCLUDE ANY NUMBERS AND RETURN IN A JSON LIST",
            }
        ],
    )
    print(response.output_text)
    return response.output_text


def formatPoints():
    lst = []
    topPoints = aiSummarize()
    topPoints.split()
    topPoints = topPoints.split("[")
    topPoints = topPoints[1]
    topPoints = topPoints.split("]")
    topPoints = topPoints[0]
    lst.append(topPoints)
    return json.dumps(lst)
