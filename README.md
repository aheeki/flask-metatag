# flask-metatag
flask-restful API to scrape meta tags

### install
pip install flask flask-restful newspaper3k

### use
POST to http://127.0.0.1:5000/tags with url data parameter

### example
`curl http://127.0.0.1:5000/tags -d "url=http://www.mtv.com/artists/rick-astley/" -X POST`

### docker
`docker-compose build`

`docker-compose up -d`

`curl http://[machine ip]/tags -d "url=http://www.mtv.com/artists/rick-astley/" -X POST`

### python
3.4