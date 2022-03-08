# scrapews

A news scraper made in Python using the packages ```requests``` and ```lxml```.


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

 - First Clone this repo

```bash
git clone https://github.com/mateusvictor/scrapews.git
```

- Change into the project directory

```bash
cd scrapews/
```

- Create a Virtualenv in the project directory

```bash
python -m venv venv
```

- Activate the virtualenv

```bash
venv\Scripts\activate.bat
```

- Install the project dependencies

```bash
pip install -r requirements.txt
```
