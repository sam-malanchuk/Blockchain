import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Welcome message to the client portal
@app.route('/', methods=['GET'])
def welcome_message():
    return 'Welcome to the Wallet!', 200

# Run the program on port 8000
if __name__ == '__main__':
    app.run(host='localhost', port=8080)