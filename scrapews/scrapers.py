from .base_scraper import BaseScraper


class NewYorkTimes(BaseScraper):
	base_url = 'https://www.nytimes.com'
	url = 'https://www.nytimes.com/section/technology'
	num_of_articles = 10
	xpaths = {
		'title': '//*[@id="stream-panel"]/div[1]/ol/li[{}]/div/div[1]/a/h2/text()',
		'link': '//*[@id="stream-panel"]/div[1]/ol/li[{}]/div/div[1]/a/@href',
		'description': '//*[@id="stream-panel"]/div[1]/ol/li[{}]/div/div[1]/a/p/text()',
	}


class BBCNews(BaseScraper):
	base_url = 'https://www.bbc.com'
	url = 'https://www.bbc.com/news/science_and_environment'
	num_of_articles = 10
	xpaths = {
		'title': '//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[{}]/div/div[2]/div[1]/a/h3/text()',
		'link': '//*[@id="topos-component"]/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div[{}]/div/div[2]/div[1]/a/@href',
	}


class ESPN(BaseScraper):
	base_url = 'https://www.espn.com.br'
	url = 'https://www.espn.com.br/futebol/'
	num_of_articles = 10
	xpaths = {
		'link': '//*[@id="news-feed"]/article[{}]/section/a/@href',
		'title': '//*[@id="news-feed"]/article[{}]/section/a/div/div[1]/h1/text()',
	}