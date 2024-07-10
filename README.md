## Prerequisites
- Docker
- git

## Clone Repository
- git clone https://github.com/yourusername/primecapital.git
- cd primecapital

## Setup
- cd docker
- docker-compose build
- docker-compose up -d
## Run Unit Tests
- docker exec -it primecapital-app bash
- python -m unittest discover -s tests

## Access the application in browser
 - http://localhost:5000/






