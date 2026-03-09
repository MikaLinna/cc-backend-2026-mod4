from flask import Flask, request

app = Flask(__name__)

# read pickle file here to python object; "rb" = read binary
with open("sentiment_model_v1.pkl", "rb"):
    loaded_tuple = pickle.load(file)


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

