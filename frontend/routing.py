from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import IntegerField, SelectField, SubmitField, validators, ValidationError, StringField, PasswordField
from backend.classifier_rules.schiffe_classifier_rules import SchiffeClassifierRules
from backend.classifier_rules.landfahrzeug_classifier_rules import LandfahrzeugClassifierRules

app = Flask(__name__)
app.secret_key = 'development key'

@app.route("/")
@app.route("/home")
def home():
    title = 'Home'
    return render_template("home.html", title=title)

@app.route("/schiffe")
def schiffe():
    title = 'Schiffe'
    return render_template("schiffe.html", title=title)

@app.route("/landfahrzeug")
def landfahrzeug():
    title = 'landfahrzeug'
    return render_template("landfahrzeug.html", title=title)

@app.route("/luftfahrzeug")
def luftfahrzeug():
    title = 'luftfahrzeug'
    return render_template("luftfahrzeug.html", title=title)

@app.route("/schiffe/classification")
def schiffe_classification():
    title = 'schiffe-classification'
    classifier = SchiffeClassifierRules()
    classifier.schiffe_classifier_rules()
    return render_template("classification/schiffe_classification.html", title=title)

@app.route("/landfahrzeug/classification")
def landfahrzeug_classification():
    title = 'landfahrzeug-classification'
    classifier = LandfahrzeugClassifierRules()
    classifier.landfahrzueg_classifier_rules()
    return render_template("classification/landfahrzeug_classification.html", title=title)

@app.route("/landfahrzeug/explanation")
def landfahrzeug_explanation():
    title = 'landfahrzeug-explanation'
    return render_template("explanation/landfahrzeug_explanation.html", title=title)

@app.route("/luftfahrzeug/classification")
def luftfahrzeug_classification():
    title = 'luftfahrzeug-classification'
    return render_template("classification/luftfahrzeug_classification.html", title=title)

@app.route("/luftfahrzeug/explanation")
def luftfahrzeug_explanation():
    title = 'luftfahrzeug-explanation'
    return render_template("explanation/luftfahrzeug_explanation.html", title=title)

class SchiffeExplanationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route("/schiffe/explanation", methods=['GET', 'POST'])
def schiffe_explanation():
    form = SchiffeExplanationForm(request.form)
    if(request.method == 'POST' and form.validate()):
        return render_template("explanation/schiffe_explanation.html", form=form)
    return render_template("explanation/schiffe_explanation.html", form=form)

if(__name__ == '__main__'):
    app.run(debug=True)
