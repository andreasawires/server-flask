from flask import Flask, render_template, redirect, request, url_for
import requests

app = Flask(__name__)

key = open("key.txt", "r").read()
password = open("password.txt", "r").read()

r = requests.get(f"https://{key}:{password}@test-impossible-brads.myshopify.com/admin/api/2021-01/checkouts.json")

@app.route("/checkouts")
def homepage():
    return r.content

@app.errorhandler(404)
def page_not_found(error):
    return "404"

@app.errorhandler(500)
def internal_error(error):
    return "500"

if __name__ == "__main__":
    app.run(debug=True)