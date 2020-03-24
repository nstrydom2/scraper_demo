import json

from flask import Flask
from flask_restx import Api, Resource

from scraper import Scraper
from algorithms import Algorithms

flask_app = Flask(__name__)
app = Api(app=flask_app)


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
    flask_app.run(debug=True)
