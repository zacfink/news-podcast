from newspaper import Article, Config
import nltk
import urllib.parse, http.client, json, os
from dotenv import load_dotenv

load_dotenv()

nltk.download("punkt_tab", quiet=True)

config = Config()
config.browser_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X)"

blocked_domains = ["investing.com", "seekingalpha.com"]


def is_blocked(url):
    return any(domain in url for domain in blocked_domains)


def mediastack():
    conn = http.client.HTTPConnection("api.mediastack.com")
    params = urllib.parse.urlencode(
        {
            "access_key": os.environ["MEDIASTACK_KEY"],
            "categories": "-general,-sports",
            "sort": "published_desc",
            "limit": 10,
        }
    )
    conn.request("GET", f"/v1/news?{params}")
    res = conn.getresponse()
    parsed = json.loads(res.read().decode("utf-8"))

    formattedArticles = []

    for article in parsed.get("data", []):
        url = article.get("url", "")
        data = {
            "source": article.get("source", "Unknown"),
            "author": article.get("author"),
            "url": url,
            "title": article.get("title"),
            "description": article.get("description"),
            "content": None,
        }

        # Try newspaper summary unless blocked
        if not is_blocked(url):
            try:
                a = Article(url, config=config)
                a.download()
                a.parse()
                a.nlp()
                data["content"] = a.summary
            except Exception as e:
                print(f"Could not summarize {url}:\n{e}")
                data["content"] = data["description"]
        else:
            print(f"Skipping blocked site: {url}")
            data["content"] = data["description"]

        formattedArticles.append(data)

    return formattedArticles
