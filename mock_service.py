from flask import Flask

from utils import Utils

app = Flask(__name__)


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
app.run(host=ipaddress)