from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from newspaper import Article

app = Flask(__name__)

class MetaTagAPI(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('url', type=str, help='url to scrape')
            data = parser.parse_args()
            url = data['url']
            tags = {}

            art = Article(url)
            art.download()
            art.parse()

            if art.title:
                tags['title'] = art.title

            if art.top_image:
                tags['image'] = art.top_image

            # Throwing a "Not JSON Serializable"
            # if art.images:
            #     tags['images'] = art.images

            # if art.description:
            #     tags['description'] = art.description            
            response = jsonify(tags)
            print('resp in class')
            print(response)
            return response
        except Exception as e:
            print('\n', 'error type:', '\n', type(e))
            print('\n', 'error args:', '\n', e.args)
            print('\n', 'error:', '\n', e)
            response = jsonify({"response": "error"})
            return response

api = Api(app)
api.add_resource(MetaTagAPI, "/tags")

@app.after_request
def after_request(response):
  response.headers['Access-Control-Allow-Origin'] = '*'
  response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
  response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
  print('resp in after_request')
  print(response)  
  return response

if __name__ == "__main__":
    app.run(debug=True)