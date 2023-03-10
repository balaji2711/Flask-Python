from flask import Flask
from utils import Utils
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "My Flask App"
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/server")
def index():
    return "Hello, This Server works!"


@app.route("/AddEmployee", methods=['POST'])
def add_employee():
    return "{\"Name\" : \"Balaji\" }", 201


@app.route("/UpdateEmployee", methods=['PUT'])
def update_employee():
    return "{\"Name\" : \"Balaji G\" }", 201


@app.route("/GetAllEmployee", methods=['GET'])
def get_all_employee():
    return "{\"User\" : \"Balaji G\"}", 200


ipaddress = Utils.get_current_ip_address()
app.run(host=ipaddress, debug=True)