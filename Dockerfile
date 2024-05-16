FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /app/imdbscraper
CMD ["scrapy", "crawl", "imdb_spider", "-o", "output.json"]
