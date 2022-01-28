import requests
from lxml import html
from datetime import datetime
import json


class BaseScraper:
	url = None
	xpaths = None
	base_url = ''
	num_of_articles = None
	
	def __init__(self):
		self.data = {
			'site': f'{self.get_class_name()}',
			'articles': [],
			'scraped_at': '',
		}
		assert self.url and isinstance(self.url, str)
		assert self.num_of_articles and isinstance(self.num_of_articles, int)
		assert self.xpaths and isinstance(self.xpaths, dict)

	@classmethod
	def get_class_name(cls):
		return cls.__name__

	def get_html(self):
		page = requests.get(self.url)
		assert page.ok
		return html.fromstring(page.text)

	def scrape(self):
		articles = []
		html_page = self.get_html()
		scraped_at = self.str_datetime_now()

		for n in range(1, self.num_of_articles+1):
			article = self.__get_article_by_id(id=n, html_page=html_page)

			if self.valid_article(article):
				article['scraped_at'] = scraped_at
				articles.append(article)

		self.data['scraped_at'] = scraped_at
		self.data['articles'] = articles

	def valid_article(self, article: dict):
		if article.get('title', None) is None or article.get('link', None) is None:
			return False
		return True

	def __get_article_by_id(self, id: int, html_page: html.HtmlElement):
		article = {}
		for field, xpath in self.xpaths.items():
			section = html_page.xpath(xpath.format(id))
			article[field] = section[0] if section else None
			if field == 'link' and article[field]:
				article[field] = self.base_url + article[field]
		return article

	def send_to_server(self):
		raise NotImplementedError()

	def str_datetime_now(self):
		now = datetime.now()
		return now.strftime('%d-%m-%Y %H:%M:%S')

	def print_json(self, json_response: dict):
		print(json.dumps(json_response, indent=4, sort_keys=True))
	