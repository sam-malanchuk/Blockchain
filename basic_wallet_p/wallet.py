import hashlib
import json
import requests
import sys

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request, render_template

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# get the current route
if len(sys.argv) > 1:
    node = sys.argv[1]
else:
    node = "http://localhost:8000"

# Welcome message to the client portal
# @app.route('/', methods=['GET'])
# def welcome_message():
#     return 'Welcome to the Wallet!', 200

# Form to enter user-id to check
# @app.route('/')
# def my_form():
#     return render_template("form_input.html")

# Form to accept input from user form
@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

    print(f'I got the response, it is: {text}')

@app.route('/')
def get_chain():
    data = {}
    r = requests.get(url=node + "/chain")
    # Handle non-json response
    try:
        data = r.json()
    except ValueError:
        print("Error:  Non-json response")
        print("Response returned:")
        print(r)

    if data == {}:
        return "No data found."
    else:
        user = 'sam-malanchuk'
        wallet_total = 0
        user_transactions = []
        chain = data['chain']
        chain_length = data['len']
        for block in chain:
            for record in block['transactions']:
                if record['recipient'] == user or record['sender'] == user:
                    user_transactions.append(record)
                    if record['recipient'] == user:
                        wallet_total += int(record['amount'])
                    else:
                        wallet_total -= int(record['amount'])
        if len(user_transactions) == 0:
            return f'nothing found for user {user}'
        else:
            return jsonify({
                'user': user,
                'wallet_total': wallet_total,
                'user_transactions': user_transactions,
            }), 200

# Run the program on port 8000
if __name__ == '__main__':
    app.run(host='localhost', port=8080)