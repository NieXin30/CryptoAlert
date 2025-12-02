#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def main():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CryptoAlert</title>
    </head>
    <body>
        <h1>CryptoAlert</h1>
        <form action="/alert" method="POST">
            <label>Email Address:</label><br>
            <input type="email" name="email" required><br><br>

            <label>Currency to Monitor:</label><br>
            <input type="text" name="currency" placeholder="e.g. BTC" required><br><br>

            <label>Price Threshold:</label><br>
            <input type="number" name="threshold" step="0.01" required><br><br>

            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    '''


@app.route("/alert", methods=["POST"])
def alert():
    email = request.form.get("email", "")
    currency = request.form.get("currency", "")
    threshold = request.form.get("threshold", "")

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Success</title>
    </head>
    <body>
        <h1>Setup Successful!</h1>
        <p>We will monitor <strong>{currency}</strong> price for <strong>{email}</strong> with a threshold of <strong>${threshold}</strong>.</p>
        <br>
        <a href="/">Back to Home</a>
    </body>
    </html>
    '''
