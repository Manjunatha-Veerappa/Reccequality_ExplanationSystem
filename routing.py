from flask import Flask, render_template, request, url_for, redirect, flash, jsonify, json
from random import sample
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, validators, ValidationError, StringField, PasswordField
from backend.classification.schiffe_classification import SchiffeClassification
from backend.classification.landfahrzeug_classification import LandfahrzeugClassification
from backend.classification.luftfahrzeug_classification import LuftfahrzeugClassification

app = Flask(__name__)
app.secret_key = 'development key'

luft_data = []
land_data = []
schiff_data = []
luft_attr_counter = []

@app.route("/")
@app.route("/home")
def home():
    title = 'Home'
    return render_template("home.html", title=title)

@app.route("/luftfahrzeug")
def luftfahrzeug():
    title = 'luftfahrzeug'
    classifier = LuftfahrzeugClassification()
    classifier.random_forest()
    luft_attr_counter.append(classifier.lime_explanation())
    print(luft_attr_counter)
    return render_template("luftfahrzeug.html", title=title)

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

            abmessungen_länge = float(request.form['abmessungen_länge'])

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

            user_data = [abmessungen_länge, starflügler, tragflächen, triebwerke, rumpf, leitwerk, drehflügler, drehflügler_rumpf_cockpit, doppeldecker, tragflächen_stellung_gerade, hochDecker,
                    triebwerke_triebwerksart, rumpf_rumpfformen, drehflügler_rotor, drehflügler_triebwerk, drehflügler_rumpf, drehflügler_heckausleger, drehflügler_triebwerk_lufteinlass,
                    drehflügler_triebwerk_luftauslass, drehflugler_rotor_einzelRotor_rotorblatter, drehflugler_triebwerk_position_uberdemRumpf_anzahl]

            classifier = LuftfahrzeugClassification()
            classifier.random_forest()
            exp_list = classifier.lime_explanation4user_data(user_data)
            labels_list = []
            data_list = []
            for i in range(len(exp_list)):
                for j in range(1):
                    labels_list.append(exp_list[i][j])
                    data_list.append(exp_list[i][j + 1])

            luft_data.append(labels_list)
            luft_data.append(data_list)

            return render_template("explanation/luftfahrzeug_explanation.html", title=title, data=luft_data)

    except Exception as e:
        flash(e)
        return render_template("explanation/luftfahrzeug_explanation.html", title=title)

    return render_template("explanation/luftfahrzeug_explanation.html", title=title)

@app.route("/luftfahrzeug_data")
def luftfahrzeug_data():
    return jsonify({'results' : luft_data})

@app.route("/luftfahrzeug/dashboard")
def luftfahrzeug_dashboard():
    title = 'luftfahrzeug-dashboard'
    return render_template("dashboard/luftfahrzeug/datasetPieChart.html", title=title, data=luft_attr_counter)

@app.route("/landfahrzeug")
def landfahrzeug():
    title = 'landfahrzeug'
    return render_template("landfahrzeug.html", title=title)

@app.route("/landfahrzeug/classification")
def landfahrzeug_classification():
    title = 'landfahrzeug-classification'
    classifier = LandfahrzeugClassification()
    classifier.random_forest()
    return render_template("classification/landfahrzeug_classification.html", title=title)

@app.route("/landfahrzeug/explanation", methods=['GET', 'POST'])
def landfahrzeug_explanation():
    title = 'landfahrzeug-explanation'
    try:
        if(request.method == "POST"):

            abmessungen_breite = float(request.form['abmessungen_breite'])

            gezogenes_gerät = int(request.form['gezogenes_gerät'])

            räder_achsen = int(request.form['räder_achsen'])

            kettenfahrzeug = int(request.form['kettenfahrzeug'])

            kettenlaufwerk = int(request.form['kettenlaufwerk'])

            kettendetails = int(request.form['kettendetails'])

            aufbau_turm_turmform = int(request.form['aufbau_turm_turmform'])

            aufbau_turm_turmposition = int(request.form['aufbau_turm_turmposition'])

            radfahrzeug = int(request.form['radfahrzeug'])

            wanne_karossiere_holme_lafette_wanne = int(request.form['wanne_karossiere_holme_lafette_wanne'])

            wanne_karossiere_holme_lafette_motor_motorposition = int(request.form['wanne_karossiere_holme_lafette_motor_motorposition'])

            wanne_karossiere_lafette_wanne_form_kastenförmig = int(request.form['wanne_karossiere_lafette_wanne_form_kastenförmig'])

            wanne_karossiere_lafette_wanne_form_draufsicht_bug = int(request.form['wanne_karossiere_lafette_wanne_form_draufsicht_bug'])

            wanne_karossiere_lafette_wanne_form_draufsicht_heck = int(request.form['wanne_karossiere_lafette_wanne_form_draufsicht_heck'])

            wanne_karossiere_holme_lafette_lucken = int(request.form['wanne_karossiere_holme_lafette_lucken'])

            wanne_karossiere_motor_motorposition_hinten_mitte = int(request.form['wanne_karossiere_motor_motorposition_hinten_mitte'])


            data = [abmessungen_breite, gezogenes_gerät, räder_achsen, kettenfahrzeug, kettenlaufwerk, kettendetails, aufbau_turm_turmform, aufbau_turm_turmposition, radfahrzeug,
                    wanne_karossiere_holme_lafette_wanne, wanne_karossiere_holme_lafette_motor_motorposition, wanne_karossiere_lafette_wanne_form_kastenförmig,
                    wanne_karossiere_lafette_wanne_form_draufsicht_bug, wanne_karossiere_lafette_wanne_form_draufsicht_heck, wanne_karossiere_holme_lafette_lucken,
                    wanne_karossiere_motor_motorposition_hinten_mitte]

            classifier = LandfahrzeugClassification()
            classifier.random_forest()
            exp_list = classifier.lime_explanation4user_data(data)
            labels_list = []
            data_list = []
            for i in range(len(exp_list)):
                for j in range(1):
                    labels_list.append(exp_list[i][j])
                    data_list.append(exp_list[i][j + 1])

            land_data.append(labels_list)
            land_data.append(data_list)

            return render_template("explanation/landfahrzeug_explanation.html", title=title, data=land_data)

    except Exception as e:
        flash(e)
        return render_template("explanation/landfahrzeug_explanation.html", title=title)

    return render_template("explanation/landfahrzeug_explanation.html", title=title)

@app.route("/landfahrzeug_data")
def landfahrzeug_data():
    return jsonify({'results' : land_data})

@app.route("/landfahrzeug/dashboard")
def landfahrzeug_dashboard():
    title = 'landfahrzeug-dashboard'
    return render_template("dashboard/landfahrzeug/datasetPieChart.html", title=title)

@app.route("/schiffe")
def schiffe():
    title = 'Schiffe'
    return render_template("schiffe.html", title=title)

@app.route("/schiffe/classification")
def schiffe_classification():
    title = 'schiffe-classification'
    classifier = SchiffeClassification()
    classifier.random_forest()
    return render_template("classification/schiffe_classification.html", title=title)

@app.route("/schiffe/explanation", methods=['GET', 'POST'])
def schiffe_explanation():
    title = 'schiffe-explanation'
    try:
        if (request.method == "POST"):
            abmessungen_breite = float(request.form['abmessungen_breite'])

            uberwasserschiffe = int(request.form['uberwasserschiffe'])

            uberwasserschiffe_rumpf_rumpfart = int(request.form['uberwasserschiffe_rumpf_rumpfart'])

            uberwasserschiffe_rumpf_bugformen = int(request.form['uberwasserschiffe_rumpf_bugformen'])

            uberwasserschiffe_rumpf_heckformen = int(request.form['uberwasserschiffe_rumpf_heckformen'])

            uberwasserschiffe_rumpf = int(request.form['uberwasserschiffe_rumpf'])

            uberwasserschiffe_aufbauten = int(request.form['uberwasserschiffe_aufbauten'])

            unterwasserschiffe_rumpform_rohrenformig = int(request.form['unterwasserschiffe_rumpform_rohrenformig'])

            unterwasserschiffe_bugformen_abgerundet = int(request.form['unterwasserschiffe_bugformen_abgerundet'])

            unterwasserschiffe_bewaffnung = int(request.form['unterwasserschiffe_bewaffnung'])

            verwendungszweck_organistaion_kampfschiff = int(request.form['verwendungszweck_organistaion_kampfschiff'])

            uberwasserschiffe_einzelrumpf = int(request.form['uberwasserschiffe_einzelrumpf'])

            uberwasserschiffe_aufbauten_brucke = int(request.form['uberwasserschiffe_aufbauten_brucke'])

            uberwasserschiffe_bewaffnung_wasserbomben = int(request.form['uberwasserschiffe_bewaffnung_wasserbomben'])

            uberwasserschiffe_rumpf_deckformen_glattdecker = int(request.form['uberwasserschiffe_rumpf_deckformen_glattdecker'])

            überwasserschiffe_aufbautenLänge_schiffslänge_gesamtanzahl = int(request.form['überwasserschiffe_aufbautenLänge_schiffslänge_gesamtanzahl'])

            uberwasserschiffe_schornsteine_abgasoffnungen_gesamtanzahl = int(request.form['uberwasserschiffe_schornsteine_abgasoffnungen_gesamtanzahl'])

            uberwasserschiffe_masten_mittelschiff = int(request.form['uberwasserschiffe_masten_mittelschiff'])

            data = [abmessungen_breite, uberwasserschiffe, uberwasserschiffe_rumpf_rumpfart, uberwasserschiffe_rumpf_bugformen, uberwasserschiffe_rumpf_heckformen, uberwasserschiffe_rumpf,
                    uberwasserschiffe_aufbauten, unterwasserschiffe_rumpform_rohrenformig, unterwasserschiffe_bugformen_abgerundet, unterwasserschiffe_bewaffnung, verwendungszweck_organistaion_kampfschiff,
                    uberwasserschiffe_einzelrumpf, uberwasserschiffe_aufbauten_brucke, uberwasserschiffe_bewaffnung_wasserbomben, uberwasserschiffe_rumpf_deckformen_glattdecker,
                    überwasserschiffe_aufbautenLänge_schiffslänge_gesamtanzahl, uberwasserschiffe_schornsteine_abgasoffnungen_gesamtanzahl, uberwasserschiffe_masten_mittelschiff]

            classifier = SchiffeClassification()
            classifier.random_forest()
            exp_list = classifier.lime_explanation4user_data(data)
            labels_list = []
            data_list = []
            for i in range(len(exp_list)):
                for j in range(1):
                    labels_list.append(exp_list[i][j])
                    data_list.append(exp_list[i][j + 1])

            schiff_data.append(labels_list)
            schiff_data.append(data_list)

            return render_template("explanation/schiffe_explanation.html", title=title, data=schiff_data)

    except Exception as e:
        flash(e)
        return render_template("explanation/schiffe_explanation.html", title=title)

    return render_template("explanation/schiffe_explanation.html", title=title)

@app.route("/schiffe/dashboard")
def schiffe_dashboard():
    title = 'schiffe-dashboard'
    return render_template("dashboard/schiffe/datasetPieChart.html", title=title)

@app.route("/schiffe_data")
def schiffe_data():
    return jsonify({'results' : schiff_data})

if(__name__ == '__main__'):
    app.run(debug=True)
