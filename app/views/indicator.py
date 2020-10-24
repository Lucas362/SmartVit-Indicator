from flask import Blueprint
from flask_cors import CORS
import controllers.indicator_controller as controller

app = Blueprint('indicator', __name__)
CORS(app)


@app.route("/indicators/<string:winery_id>", methods=["GET"])
def pest(winery_id):
    return controller.retrieve_indicators_request(winery_id)
