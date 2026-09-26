from pygooglenews import GoogleNews
from newspaper import Article

gn = GoogleNews()
top = gn.top_news()


def googleNews():
    formattedArticles = []

    for entry in top["entries"]:
        url = entry.get("link", "")
        articleData = {
            "source": entry.get("source", {}).get("title", "Unknown Source"),
            "author": entry.get("author", None),
            "url": url,
            "title": entry.get("title", ""),
            "description": entry.get("summary", ""),
            "content": None,
        }

        try:
            a = Article(url)
            a.download()
            a.parse()
            a.nlp()
            articleData["content"] = a.summary
        except Exception as e:
            print(f"Failed to get summary from: {url}\nError: {e}")

        if articleData["content"] != None:
            formattedArticles.append(articleData)

    return formattedArticles
