from flask import Flask, render_template, request, url_for, redirect, flash
import time
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, validators, ValidationError, StringField, PasswordField
from backend.classification.schiffe_classification import SchiffeClassification
from backend.classification.landfahrzeug_classification import LandfahrzeugClassification
from backend.classification.luftfahrzeug_classification import LuftfahrzeugClassification

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
    classifier = SchiffeClassification()
    classifier.random_forest()
    return render_template("classification/schiffe_classification.html", title=title)

@app.route("/landfahrzeug/classification")
def landfahrzeug_classification():
    title = 'landfahrzeug-classification'
    classifier = LandfahrzeugClassification()
    classifier.random_forest()
    return render_template("classification/landfahrzeug_classification.html", title=title)

@app.route("/landfahrzeug/explanation")
def landfahrzeug_explanation():
    title = 'landfahrzeug-explanation'
    return render_template("explanation/landfahrzeug_explanation.html", title=title)

@app.route("/luftfahrzeug/classification")
def luftfahrzeug_classification():
    title = 'luftfahrzeug-classification'
    classifier = LuftfahrzeugClassification()
    classifier.random_forest()
    return render_template("classification/luftfahrzeug_classification.html", title=title)

@app.route("/luftfahrzeug/explanation", methods=['GET', 'POST'])
def luftfahrzeug_explanation():
    title = 'luftfahrzeug-explanation'
    try:
        if(request.method == "POST"):
            #import os
            #path = os.getcwd() + "/static/lime_explanation_html/luftfahrzeugexplain.html"
            #print(path)
            #if os.path.isfile(path):
                #os.remove(path)
                #print('file removed')
            #else:
                #print("The file does not exist")
            abmessungen_länge = int(request.form['abmessungen_länge'])
            starflügler = int(request.form['starflügler'])
            tragflächen = int(request.form['tragflächen'])
            triebwerke = int(request.form['triebwerke'])
            rumpf = int(request.form['rumpf'])
            leitwerk = int(request.form['leitwerk'])
            drehflügler = int(request.form['drehflügler'])
            drehflügler_rumpf_cockpit = int(request.form['drehflügler_rumpf_cockpit'])
            doppeldecker = int(request.form['doppeldecker'])
            tragflächen_stellung_gerade = int(request.form['tragflächen_stellung_gerade'])
            hochDecker = int(request.form['hochDecker'])
            triebwerke_triebwerksart = int(request.form['triebwerke_triebwerksart'])
            rumpf_rumpfformen = int(request.form['rumpf_rumpfformen'])
            drehflügler_rotor = int(request.form['drehflügler_rotor'])
            drehflügler_triebwerk = int(request.form['drehflügler_triebwerk'])
            drehflügler_rumpf = int(request.form['drehflügler_rumpf'])
            drehflügler_heckausleger = int(request.form['drehflügler_heckausleger'])
            drehflügler_triebwerk_lufteinlass = int(request.form['drehflügler_triebwerk_lufteinlass'])
            drehflügler_triebwerk_luftauslass = int(request.form['drehflügler_triebwerk_luftauslass'])
            drehflugler_rotor_einzelRotor_rotorblatter = int(request.form['drehflugler_rotor_einzelRotor_rotorblatter'])
            drehflugler_triebwerk_position_uberdemRumpf_anzahl = int(request.form['drehflugler_triebwerk_position_uberdemRumpf_anzahl'])
            data = [abmessungen_länge, starflügler, tragflächen, triebwerke, rumpf, leitwerk, drehflügler, drehflügler_rumpf_cockpit, doppeldecker, tragflächen_stellung_gerade, hochDecker,
                    triebwerke_triebwerksart, rumpf_rumpfformen, drehflügler_rotor, drehflügler_triebwerk, drehflügler_rumpf, drehflügler_heckausleger, drehflügler_triebwerk_lufteinlass,
                    drehflügler_triebwerk_luftauslass, drehflugler_rotor_einzelRotor_rotorblatter, drehflugler_triebwerk_position_uberdemRumpf_anzahl]
            print(data)
            classifier = LuftfahrzeugClassification()
            classifier.random_forest()
            #classifier.lime_explanation()
            classifier.lime_explanation4user_data(data)
            return render_template("explanation/luftfahrzeug_explanation.html", title=title, data=data)
    except Exception as e:
        flash(e)
        return render_template("explanation/luftfahrzeug_explanation.html", title=title)

    return render_template("explanation/luftfahrzeug_explanation.html", title=title)

@app.route("/schiffe/explanation", methods=['GET', 'POST'])
def schiffe_explanation():
    title = 'schiffe-explanation'
    #form = ExplanationForm()
    return render_template("explanation/schiffe_explanation.html", title=title)

if(__name__ == '__main__'):
    app.run(debug=True)
