import scrapy


class IMDBSpider(scrapy.Spider):
  name = 'imdb_spider'
  start_urls = ['https://www.imdb.com/chart/top/']

  def parse(self, response):
    top_50_movie_details = response.xpath('//li[contains(@class, "ipc-metadata-list-summary-item")]')[:50]
    print(f'Number of movie items: {len(top_50_movie_details)}')
    for movie_item in top_50_movie_details:
      movie_details_url = movie_item.css('.ipc-title-link-wrapper::attr(href)').get()
      yield scrapy.Request(url=response.urljoin(movie_details_url), callback=self.parse_movie_details)

  def parse_movie_details(self, response):
    movie_name = response.css('span.hero__primary-text::text').get()
    release_date = response.css('a.ipc-link[href*="releaseinfo"]::text').get()
    director_name = response.css(
      'span.ipc-metadata-list-item__label[aria-label="See full cast and crew"] + div ul a::text') \
      .extract_first()
    casts = response.css(
      'a.ipc-metadata-list-item__label[aria-label="See full cast and crew"] + div ul a::text') \
      .extract()
    casts = list(set([actor.strip() for actor in casts]))
    yield {
      'Movie name': movie_name,
      'Release date': release_date,
      'Director': director_name,
      'casts': casts
    }
