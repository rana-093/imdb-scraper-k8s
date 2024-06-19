## imdb_spider crawls the top 50 movies from IMDB

First clone this repo: **https://github.com/rana-093/imdb-scraper-k8s**

To run in docker run:
- `docker build -f imdb-spider .`
- `docker run imdb-spider`

You can mount volume also like this:
- `docker run -v $(pwd)/imdbscraper/:/app/imdbscraper imdb-scraper`

This way you will find  output.json  file inside imdbscraper folder

Finally to run via k8s:
- Need to config kubectl first

Then apply the following commands:
- `kubectl apply -f deployment.yaml`
- `kubectl apply -f service.yaml`
- `kubectl apply -f hpa.yaml`

Now give the following command:
- `kubectl get all`

You will find the necessary resources here!

**But make sure first to configure aws, eksctl also!** 

