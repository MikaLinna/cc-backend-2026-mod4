from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World again !</p>"
    # json test for return
    return {"message": "hello!"}

@app.route("/api", methods=["POST"])
def sentiment():
    body_data = request.get_json()
    print("Body data:")
    print(body_data["data"])
    return {"message": "hello from API!"}

