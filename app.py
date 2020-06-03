import os
from pathlib import Path
from settings import *
from flask import Flask, jsonify
#from flask_cors import CORS

port = os.getenv("PORT")
domain = os.getenv("DOMAIN")

app  = Flask(__name__)



from src.routes.route import *

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)