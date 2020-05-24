from flask import request
from app import app
from src.analysis_emotional.analysis_emotional import EmotionalAnalisys
import json
from flask_cors import CORS, cross_origin

CORS(app, resources={r"/*":{"origins": "http://localhost:3000"}})

@app.route('/api/v1/emotional_analysis', methods=["POST"])
@cross_origin()
def emotional_analysis():
    datas = request.json
    url = datas["url"]
    emotional_analisys = EmotionalAnalisys(url)
    js =json.dumps(emotional_analisys[:])
    return js