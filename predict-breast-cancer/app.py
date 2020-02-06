from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_cancer():
    form = request.form
    prediction = {
        'meanRadius': form.get('meanRadius'),
        'meanTexture': form.get('meanTexture')}
    print(prediction)
    return render_template('predict.html', prediction=prediction)

# python -m flask run
# https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework