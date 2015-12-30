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

            return jsonify({"response":tags})
        except Exception as e:
            return jsonify({"response": "error"})

api = Api(app)
api.add_resource(MetaTagAPI, "/tags")

if __name__ == "__main__":
    app.run()