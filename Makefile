db:
	docker-compose up -d
app:
	python -m aiohttp.web -H localhost -P 8080 src.main:init_app
