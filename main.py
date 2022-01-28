from scrapews.scrapers import NewYorkTimes, BBCNews, ESPN


def main():
	targets = [NewYorkTimes(), BBCNews(), ESPN()]

	for target in targets:
		print(f'Scraping {target.base_url}')

		target.scrape()

		results = target.data['articles']
		print(f'{len(results)} articles scraped from {target.url}.\n')


if __name__ == '__main__':
	main()
	