# News Podcast

Turns today's headlines into a short spoken news briefing.

1. Pulls top stories from Google News, NewsAPI, NewsData and mediastack, and extracts each article's text.
2. GPT-4o mini boils each source down to its key points, then writes a script of up to 500 words.
3. OpenAI text-to-speech reads the script out to `readScript/speech.mp3`.

`newsFiles/script/script.txt` is an example script from a real run.

## Run it

```bash
pip install openai python-dotenv pygooglenews newspaper3k nltk newsapi-python newsdataapi
cp .env.example .env   # add your OpenAI, NewsAPI, NewsData and mediastack keys
python main.py
```
