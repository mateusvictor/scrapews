# scrapews

A news scraper made in Python using the packages ```requests``` and ```lxml```.

Usage of the class <a href="https://github.com/mateusvictor/scrapews/blob/main/scrapews/base_scraper.py">```BaseScraper```</a>:

<!-- <img src="https://github.com/mateusvictor/scrapews/blob/main/screenshots/example.png"> -->

```python
from scrapews.scrapers import NewYorkTimes


ny_scraper = NewYorkTimes()

ny_scraper.scrape()
ny_scraper.send_to_server()

print(ny_scraper.data.get('articles'))
```

## Idea

The core ideia of the ```scrapews``` scraper is to request the HTML of a news site and extract from it, through XPath expressions, the primary information about an article, such as title, description and url.

Combining with a RESTful API service, the scraper can be used to feed a content agregator app, for example.

Check out the <a href="https://github.com/mateusvictor/scrapews/blob/main/scrapews/base_scraper.py">```base_scraper``` class</a> for more understanding of the code.

## Instalation
 