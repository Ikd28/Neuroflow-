from flask import Flask
from flask_restful import Resource, Api, reqparse
import random

app = Flask(__name__)
api = Api(app)
moods = [{
          "sad": "sad",
          "happy":'happy'
      }]

@app.route('/getmood',methods=['get'])
def get():
    return random.choice(moods), 200
@app.route('/postmood',methods=['get','post'])
def post():
    parser = reqparse.RequestParser()
    parser.add_argument("mood")
    parser.add_argument("date")
    params = parser.parse_args()

    for mood in moods:
        if id == mood:
              return f"Mood with id {id} already exists", 400
        mood = {
            "id": int(),
            "mood": params["mood"],
            "date": params["date"]
            }

        return mood, 201
 


if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)
