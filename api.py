from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# read pickle file here to python object; "rb" = read binary
with open("model/sentiment_model_v1.pkl", "rb") as file:
    model = pickle.load(file)



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



# some testing to show model size data
@app.route("/model")
def show_model():

    info = {
        "pipeline": str(model),
        "steps": [name for name, _ in model.steps]
    }
    return jsonify(info)

# info for model
@app.route("/model/info")
def model_info():
    vocab_size = len(model.named_steps["tfidf"].vocabulary_)
    return jsonify({
        "model_type": "sentiment classifier",
        "vectorizer": "TFIDF",
        "classifier": "LinearSVC",
        "vocabulary_size": vocab_size
    })
    
# ten first words
@app.route("/model/words")
def model_words():

    vocab = model.named_steps["tfidf"].vocabulary_

    first_words = list(vocab.keys())[:10]

    return {
        "first_words": first_words
    }
    
# topWords    
@app.route("/model/topwords")
def top_words():

    tfidf = model.named_steps["tfidf"]

    words = list(tfidf.vocabulary_.keys())[:5]

    return {"example_words": words}



# most important words
# print(svc.classes_)     # luokat
# print(svc.coef_.shape)  # painomatriisi
@app.route("/model/important_words")
def important_words():

    import numpy as np

    tfidf = model.named_steps["tfidf"]
    svc = model.named_steps["clf"]

    words = tfidf.get_feature_names_out()

    # painorivit luokittain
    weights_negative = svc.coef_[0]
    weights_neutral = svc.coef_[1]
    weights_positive = svc.coef_[2]

    # top 10 sanat per luokka
    neg_idx = np.argsort(weights_negative)[-10:][::-1]
    neu_idx = np.argsort(weights_neutral)[-10:][::-1]
    pos_idx = np.argsort(weights_positive)[-10:][::-1]

    negative = [words[i] for i in neg_idx]
    neutral = [words[i] for i in neu_idx]
    positive = [words[i] for i in pos_idx]

    return {
        "classes": svc.classes_.tolist(),
        "top_negative_words": negative,
        "top_neutral_words": neutral,
        "top_positive_words": positive
    }