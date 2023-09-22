import sys
from flask import Flask, jsonify, request
import yaml

from controller.todo_list import register_todo_list

try:
    with open(".local.yml", "r") as file:
        config = yaml.safe_load(file)
except:
    sys.exit("Local config not found")

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "helloyuesss!"})


register_todo_list(app)

if __name__ == "__main__":
    app.run(debug=config["DEBUG"])
