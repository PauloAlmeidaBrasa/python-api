from flask import Flask, jsonify
import json


app = Flask(__name__)

# Helper function to load data from a JSON file
def load_resource_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "File not found"}, 404
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON"}, 400

@app.route('/')
def get_resource():
    file_path = 'data/data.json'  # The path to the file
    data = load_resource_from_file(file_path)
    return jsonify(data)

if __name__ == '__main__':
    app.run()
