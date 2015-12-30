from flask import Flask, jsonify
from flask.ext.restful import Api, Resource
from newspaper import Article

app = Flask(__name__)

class metatagAPI(Resource):
    data = []
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass

api = Api(app)
api.add_resource(UserAPI, '/api/<string:url>')

if __name__ == "__main__":
    app.run(debug=True)