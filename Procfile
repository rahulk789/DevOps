web: sh -c 'cd api && gunicorn api.wsgi'
release: python api/manage.py migrate
cmd: cd api/scraper/scraper/spiders && scrapy crawl mcx
