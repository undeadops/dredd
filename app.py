## Dredd - API for determinting Sentiment
from datetime import datetime

from flask import Flask, request
from flask_restful import Resource, Api

from textblob import TextBlob

app = Flask(__name__)
api = Api(app)

# Need to Fetch Mongo URL from etcd


class JudgeDredd(Resource):
    def get(self):
        queryText = request.form['text']
        result = TextBlob(queryText)
        return '{ "sentinment": { "polarity": %s, "subjectivity": %s } }' % (result.sentiment.polarity, result.sentiment.subjectivity)

api.add_resource(JudgeDredd, '/api/v1/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, debug=True)
