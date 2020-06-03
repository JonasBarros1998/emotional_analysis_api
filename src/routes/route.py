from flask import request
from app import app
from src.analysis_emotional.analysis_emotional import EmotionalAnalisys
import json

@app.route('/api/v1/emotional_analysis', methods=["POST"])

def emotional_analysis():
    datas = request.json
    url = datas["url"]
    emotional_analisys = EmotionalAnalisys(url)
    js =json.dumps(emotional_analisys[:])
    return js