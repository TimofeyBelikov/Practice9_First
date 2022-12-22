# Preparation
## PG container
docker run --name db-service
           -p 5432:5432
           --restart always
           --net-alias db-service
           -e POSTGRES_DB=postgres
           -e POSTGRES_USER=postgres
           -e POSTGRES_PASSWORD=postgres
           --network=microarch -d postgres 
## Service container
docker run -p 8000:80
           -d --restart always
           --net-alias first-service
           --network=microarch
           -e POSTGRES_NAME=postgres
           -e POSTGRES_USER=postgres
           -e POSTGRES_PASSWORD=postgres
           --name first-service
           timofeybelikov/ma-status-service:latest
