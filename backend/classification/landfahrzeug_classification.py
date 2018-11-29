import csv
import numpy
import sklearn
from backend.model.random_forest_classifier import RandomForest
from backend.lime_explanation.lime_explanation import LimeExplanation

class LandfahrzeugClassification(object):

    def __init__(self):
        self.classifier = None
        self.header_list = ["vectorName", "abmessungen_Breite", "gezogenes_Gerat", "rader_Achsen", "kettenfahrzeug", \
                       "kettenlaufwerk", "kettendetails", "aufbau_Turm_Turmform", "aufbau_Turm_Turmposition",
                       "radfahrzeug", \
                       "wanne_Karossiere_Holme_Lafette_Wanne", "wanne_Karossiere_Holme_Lafette_Motor_Motorposition", \
                       "wanne_Karossiere_Holme_Lafette_Wanne_Form_Kastenformig",
                       "wanne_Karossiere_Holme_Lafette_Wanne_Form_Draufsicht_Bug", \
                       "wanne_Karossiere_Holme_Lafette_Wanne_Form_Draufsicht_Heck", "zusatzinformationen_Familie", \
                       "wanne_Karossiere_Holme_Lafette_Lucken",
                       "wanne_Karossiere_Holme_Lafette_Motor_Motorposition_Hinten_Mitte", "result"]

    def landfahrzueg_classifier_rules(self):
        with open("static/datasetCSV/Landfahrzeugdata.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(open("static/classification_csv_files/LandfahrzeugClassificationCategorical.csv", "w"))
            count = 0
            for row in reader:
                if (count == 0):
                    writer.writerow(self.header_list)
                    count += 1
                    continue
                else:
                    rule1, rule2, rule3, rule4, rule5, rule6, rule7 = 1, 1, 1, 1, 1, 1, 1

                    if (int(row[2114]) == 0):
                        if (int(row[1881]) == 0):
                            rule1 = 0
                    else:
                        rule1 = 0

                    if (int(row[2668]) == 0 and int(row[769]) == 0):
                        if (int(row[2917]) == 0):
                            rule2 = 0
                    else:
                        rule2 = 0

                    if (int(row[1722]) == 0):
                        if (int(row[4342]) == 0):
                            rule3 = 0
                    else:
                        rule3 = 0

                    if (int(row[2796]) == 0 and int(row[1169]) == 0):
                        if (int(row[4141]) == 0):
                            rule4 = 0
                    else:
                        rule4 = 0

                    if (int(row[2668]) == 0 and int(row[1169]) == 0):
                        if (int(row[4141]) == 0):
                            rule5 = 0
                    else:
                        rule5 = 0

                    if (int(row[1790]) == 0 and int(row[4571]) == 0):
                        if (int(row[911]) == 0):
                            rule6 = 0
                    else:
                        rule6 = 0

                    if (float(row[978]) > 0.5 and float(row[978]) < 10):
                        rule7 = 0

                    if (rule1 == 0 and rule2 == 0 and rule3 == 0 and rule4 == 0 and rule5 == 0 and rule6 == 0 and rule7 == 0):
                        result = 1
                    else:
                        result = 0

                    #result1 = str(rule1) + str(rule2) + str(rule3) + str(rule4) + str(rule5) + str(rule6) + str(result)
                    result1 = str(result)

                    list = [row[4771], row[978], row[2114], row[1881], row[2668], row[769], row[2917], row[1722], row[4342], row[2796], row[1169], \
                            row[4141], row[1790], row[4571], row[911], row[13], row[1522], row[4372], result1]

                    writer.writerow(list)

    def random_forest(self):
        count = 0
        with open("static/classification_csv_files/LandfahrzeugClassificationCategorical.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            included_cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17]
            data = []
            result = []
            for row in reader:
                if (count == 0):
                    count = count + 1
                    continue
                else:
                    result.append(int(row[18]))
                    content = (list(float(row[i]) for i in included_cols))
                    data.append(content)

        data = numpy.array(data)
        result = numpy.array(result)

        self.classifier = RandomForest()
        self.train, self.test, self.labels_train, self.labels_test = self.classifier.split_dataset(data, result, 0.8)
        train = numpy.array(self.train)

        self.trained_model = self.classifier.random_forest_classifier(train, self.labels_train)

        predictions = self.trained_model.predict(self.test)

        print("Train Accuracy :: ", sklearn.metrics.accuracy_score(self.labels_train, self.trained_model.predict(train)))
        print("Test Accuracy  :: ", sklearn.metrics.accuracy_score(self.labels_test, predictions))

    def lime_explanation4user_data(self, arr):

        limeExplainer = LimeExplanation()
        limeExplainer.explainer(self.train, feature_names=self.header_list[1:-1], class_names=['Bad', 'Good'])

        predict_fn = lambda x: self.trained_model.predict_proba((x).astype(float))
        data_to_be_explained = numpy.array(arr)
        exp = limeExplainer.explainInstance(data_to_be_explained, predict_fn, num_features=20)
        exp.save_to_file("static/lime_explanation_html/landfahrzeugexplain.html")
        attr_explain_list = exp.as_list()
        #fig = exp.as_pyplot_figure()

        #fig.savefig("static/lime_explanation_images/landfahrzeug_explanation.png")
        #print("figure saved! and returning")
        return attr_explain_list