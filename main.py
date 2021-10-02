import os
import random
import logging
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R', 'B']


@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    return moves[random.randrange(len(moves))]


def throw():
    request.get_data()
    logger.info(request.json)
    return moves[random.randrange(len(moves))]


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=(os.environ.get('PORT', 8080)))
