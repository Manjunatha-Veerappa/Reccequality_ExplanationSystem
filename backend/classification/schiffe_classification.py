import csv
import numpy
import sklearn
from backend.random_forest.random_forest_classifier import RandomForest
from backend.lime_explanation.lime_explanation import  LimeExplanation

class SchiffeClassification(object):

    def __init__(self):
        self.classifer = None
        self.schiffe_classifier_rules()

    def schiffe_classifier_rules(self):
        with open("static/dataset/Schiffedata.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(open("static/classification_files/SchiffeClassificationCategorical.csv", "w"))
            data = []
            count = 0
            for row in reader:
                if (count == 0):
                    headers_list = ["vectorName", "abmessungen_Breite", "uberwasserschiffe", "uberwasserschiffe_Rumpf_Rumpfart",
                               "uberwasserschiffe_Rumpf_Bugformen", "uberwasserschiffe_Rumpf_Heckformen", "uberwasserschiffe_Rumpf",
                               "uberwasserschiffe_Aufbauten", "unterwasserschiffe_Rumpform_Rohrenformig", "unterwasserschiffe_Bugformen_Abgerundet",
                               "unterwasserschiffe_Bewaffnung", "verwendungszweck_Organistaion_Kampfschiff", "uberwasserschiffe_Einzelrumpf",
                               "uberwasserschiffe_Aufbauten_Brucke", "uberwasserschiffe_Bewaffnung_Wasserbomben", "zusatzinformationen_Klasse",
                               "uberwasserschiffe_Rumpf_Deckformen_Glattdecker", "uberwasserschiffe_Aufbauten_AufbautenLange_Langer_als_1_3_der_Schiffslange_Gesamtanzahl",
                               "uberwasserschiffe_Schornsteine_Abgasoffnungen_Gesamtanzahl", "uberwasserschiffe_Masten_Mittelschiff", "result"]
                    writer.writerow(headers_list)
                    count += 1
                    continue
                else:
                    rule1, rule2, rule3, rule4, rule5, rule6, rule7 = 1, 1, 1, 1, 1, 1, 1

                    if (int(row[2309]) == 0):
                        if (int(row[1917]) == 0 and int(row[814]) == 0 and int(row[3158]) == 0):
                            rule1 = 0
                    else:
                        rule1 = 0

                    if (int(row[3265]) == 0):
                        if (int(row[3855]) == 0):
                            rule2 = 0
                    else:
                        rule2 = 0

                    if (int(row[315]) == 0):
                        if (int(row[697]) == 0):
                            rule3 = 0
                    else:
                        rule3 = 0

                    if (int(row[3262]) == 0):
                        if (int(row[498]) == 0):
                            rule4 = 0
                    else:
                        rule4 = 0

                    if (int(row[2589]) == 0):
                        if (int(row[3318]) == 0):
                            rule5 = 0
                    else:
                        rule5 = 0

                    if (int(row[2177]) == 0):
                        if (int(row[498]) == 0):
                            rule6 = 0
                    else:
                        rule6 = 0

                    if (float(row[618]) >= 2.0 and  float(row[618])<= 99.0):
                        rule7 = 0

                    if (rule1 == 0 and rule2 == 0 and rule3 == 0 and rule4 == 0 and rule5 == 0 and rule6 == 0 and rule7 == 0):
                        result = 1
                    else:
                        result = 0

                    #result1 = str(rule1) + str(rule2) + str(rule3) + str(rule4) + str(rule5) + str(rule6) + str(rule7) + str(result)
                    result1 = str(result)

                    list = [row[3921], row[618], row[2309], row[1917], row[814], row[3158], row[3265], row[3855], row[315], row[697], row[3262], \
                    row[498], row[2589], row[3318], row[2177], row[2878], row[2815], row[348], row[655], row[3893], result1]

                    writer.writerow(list)


    def random_forest(self):
        count = 0
        with open("static/classification_files/SchiffeClassificationCategorical.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            included_cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19]
            data = []
            result = []
            for row in reader:
                if(count == 0):
                    count = count + 1
                    continue
                else:
                    result.append(int(row[20]))
                    content = (list(float(row[i]) for i in included_cols))
                    data.append(content)

            data = numpy.array(data)
            result = numpy.array(result)

            self.classifier = RandomForest()
            self.train, self.test, self.labels_train, self.labels_test = self.classifier.split_dataset(data, result, 0.8)
            train = numpy.array(self.train)

            self.trained_model = self.classifier.random_forest_classifier(train, self.labels_train)

            predictions = self.trained_model.predict(self.test)

            for i in range(0, 10):
                print("Actual outcome :: {} and Predicted outcome :: {}".format(list(self.labels_test)[i], predictions[i]))

            print("Train Accuracy :: ", sklearn.metrics.accuracy_score(self.labels_train, self.trained_model.predict(train)))
            print("Test Accuracy  :: ", sklearn.metrics.accuracy_score(self.labels_test, predictions))


    def lime_explanation(self):

        headers = ["vectorName", "abmessungen_Breite", "uberwasserschiffe", "uberwasserschiffe_Rumpf_Rumpfart", "uberwasserschiffe_Rumpf_Bugformen", "uberwasserschiffe_Rumpf_Heckformen",
                   "uberwasserschiffe_Rumpf", "uberwasserschiffe_Aufbauten", "unterwasserschiffe_Rumpform_Rohrenformig", "unterwasserschiffe_Bugformen_Abgerundet", "unterwasserschiffe_Bewaffnung",
                   "verwendungszweck_Organistaion_Kampfschiff", "uberwasserschiffe_Einzelrumpf", "uberwasserschiffe_Aufbauten_Brucke", "uberwasserschiffe_Bewaffnung_Wasserbomben",
                   "uberwasserschiffe_Rumpf_Deckformen_Glattdecker", "uberwasserschiffe_Aufbauten_AufbautenLange_Langer_als_1_3_der_Schiffslange_Gesamtanzahl",
                   "uberwasserschiffe_Schornsteine_Abgasoffnungen_Gesamtanzahl", "uberwasserschiffe_Masten_Mittelschiff", "result"]


        limeExplainer = LimeExplanation()

        limeExplainer.explainer(self.train, feature_names=headers[1:-1], class_names=['Bad', 'Good'])

        predict_fn = lambda x: self.trained_model.predict_proba((x).astype(float))


        exp = limeExplainer.explainInstance(self.test[0], predict_fn, num_features=20)
        limeExplainer.save("Schiffe")




