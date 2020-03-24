import json

from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

from scraper import Scraper
from algorithms import Algorithms

flask_app = Flask(__name__)
app = Api(app=flask_app)
CORS(flask_app)


@app.route('/api/scrape/imdb/top')
class Movies(Resource):
    def get(self):
        scraper = Scraper()
        return scraper.scrape_imdbtop100()


@app.route('/api/scrape/billboard/top')
class Songs(Resource):
    def get(self):
        scraper = Scraper()
        return scraper.scrape_billboardtop100()


@app.route('/api/algorithm/fizzbuzz/<numbers>')
class FizzBuzz(Resource):
    def get(self, numbers):
        algorithm = Algorithms()
        result = []

        for num in range(1, int(numbers)+1):
            result.append(algorithm.fizzbuzz(num))

        return result


if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    http_server = WSGIServer(('', 8000), flask_app)
    http_server.serve_forever()
