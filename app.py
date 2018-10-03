## Dredd - API for determinting Sentiment
from datetime import datetime

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

from textblob import TextBlob
import unicodedata

app = Flask(__name__)
api = Api(app)

# Need to Fetch Mongo URL from etcd
class JudgeDredd(Resource):
    def post(self):
        queryText = request.form['text']
        blob = TextBlob(unicodedata.normalize('NFKD', queryText).encode('ascii','ignore').lower())
        noun_phrases = blob.noun_phrases
        status = '{ "sentinment": { "polarity": %s, "subjectivity": %s , "noun_phrases": %s } }' % (blob.sentiment.polarity, blob.sentiment.subjectivity, noun_phrases)
        return jsonify(status), 200
        
api.add_resource(JudgeDredd, '/v1/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4500, debug=True)
