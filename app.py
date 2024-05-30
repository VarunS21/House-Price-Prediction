from flask import Flask, render_template, jsonify
from flask_cors import CORS
from model.predict import prediction

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict")
def predict():
    return render_template('prediction.html');

app.route("/prediction", methods=['POST'])(prediction)

if __name__ == '__main__':
    app.run()