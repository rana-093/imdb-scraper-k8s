import scrapy

class IMDBSpider(scrapy.Spider):
  name = 'imdb_spider'
  start_urls = ['https://www.imdb.com/chart/top/']

  custom_settings = {
    'CONCURRENT_REQUESTS': 5,  # Adjust the number of concurrent requests as needed
    'CONCURRENT_REQUESTS_PER_DOMAIN': 2  # Adjust the number of concurrent requests per domain
  }

  def parse(self, response):
    top_50_movie_details = response.xpath('//li[contains(@class, "ipc-metadata-list-summary-item")]')[:50]
    print(f'Number of movie items: {len(top_50_movie_details)}')
    for movie_item in top_50_movie_details:
      movie_name = movie_item.css('.ipc-title__text::text').get().strip()
      year = movie_item.css('.cli-title-metadata-item::text').get().strip()

      print("Movie Name:", movie_name)
      print("Year:", year)

  def parse_movie(self, response):
    pass
