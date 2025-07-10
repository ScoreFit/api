start:
	docker-compose build
	docker-compose up

start-detach:
	docker-compose build
	docker-compose up -d

stop:
	docker-compose down

clean:
	docker-compose down --volumes

delete:
	docker rm $(docker ps -aq)