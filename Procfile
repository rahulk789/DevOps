web: sh -c 'cd api && gunicorn api.wsgi'
release: python manage.py migrate
cmd: cd scraper/scraper/spiders
cmd: scrapy crawl mcx
