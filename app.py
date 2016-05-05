from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from flask.ext.cors import CORS
from newspaper import Article

app = Flask(__name__)
cors = CORS(app)
api = Api(app)

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
            return jsonify(tags)

        except Exception as e:
            print('\n', 'error type:', '\n', type(e))
            print('\n', 'error args:', '\n', e.args)
            print('\n', 'error:', '\n', e)
            jsonify({"response": "error"})

api.add_resource(MetaTagAPI, "/tags")

if __name__ == "__main__":
    app.run(host='0.0.0.0')