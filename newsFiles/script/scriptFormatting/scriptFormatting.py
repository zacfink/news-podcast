from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()


def scriptSummarize(
    dir="newsFiles/files/data.json", newDir="newsFiles/script/script.txt"
):
    with open(dir, "r") as file:
        content = file.read()

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": f"You will create an entertaining, non-bias, informative, and formal script to be read. You will keep it at a max of 500 words. Your infomation to be used is:\n\n{json.dumps(content)} ONLY INCLUDE THE TEXT TO BE READ - NO SPEAKER NOTES OR ANYTHING THAT ISNT THE READY TO READ SCRIPT.",
            }
        ],
    )

    with open(newDir, "w") as file:
        file.write(str(response.output_text))
