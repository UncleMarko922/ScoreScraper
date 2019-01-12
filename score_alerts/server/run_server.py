from flask import Flask
from score_alerts.server.api.readings import readings
app = Flask(__name__)

app.register_blueprint(readings)
app.run(host='localhost', port=5000, debug=True)
