import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request, render_template

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Welcome message to the client portal
# @app.route('/', methods=['GET'])
# def welcome_message():
#     return 'Welcome to the Wallet!', 200

# Form to enter user-id to check
@app.route('/')
def my_form():
    return render_template("form_input.html")

# Form to accept input from user form
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

    print(f'I got the response, it is: {text}')

# Run the program on port 8000
if __name__ == '__main__':
    app.run(host='localhost', port=8080)