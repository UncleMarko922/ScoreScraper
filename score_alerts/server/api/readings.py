from flask import Blueprint, jsonify
from score_alerts.scrapers.score_scraper import get_scores

readings = Blueprint('readings', __name__, url_prefix='/api')


@readings.route("/v1/readings")
def readings_v1():
    # try:
    results = get_scores()

    # except Exception as e:
    #     print(e)
    # results = {'results': 'error getting scores'}

    return jsonify({'test': results})