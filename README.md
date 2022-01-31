# scrapews

A news scraper made in Python using the packages ```requests``` and ```lxml```.

Usage of the class <a href="https://github.com/mateusvictor/scrapews/blob/main/scrapews/base_scraper.py">```BaseScraper```</a>:

<!-- <img src="https://github.com/mateusvictor/scrapews/blob/main/screenshots/example.png"> -->

```python
from scrapews.base_scraper import BaseScraper
from scrapews.scrapers import NewYorkTimes


ny_scraper = NewYorkTimes()

ny_scraper.scrape()
ny_scraper.send_to_server()

print(ny_scraper.data.get('articles'))
```

## Idea


## Instalation
 