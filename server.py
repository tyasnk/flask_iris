import logging
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, abort, current_app
from load_model import LoadModel
from config import config
from loggers import setup_logging

setup_logging(level=config.log_level,
              directory=config.log_dir,
              filename="flask_iris.log")

logger = logging.getLogger("server")

app = Flask(__name__)

logger.debug("Loading the classifier")
with app.app_context():
    current_app.classifier = LoadModel(config.model_dir, config.model_filename)


@app.route('/')
def index():
    return "hi"


@app.route('/predict', methods=['POST'])
def ApiCall():
    if not request.json:
        abort(400)

    y_train_json = np.array(request.json)
    y_train_json = y_train_json.reshape(1, -1)
    y_train = pd.DataFrame(y_train_json, index=[0])

    y_pred = current_app.classifier.model.predict(y_train)
    return jsonify({'Species': y_pred.item()})


if __name__ == '__main__':
    app.run(debug=True)
