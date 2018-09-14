import csv

class LandfahrzeugClassifierRules(object):

    def __init__(self):
        self.landfahrzueg_classifier_rules()

    def landfahrzueg_classifier_rules(self):
        with open("static/dataset/Landfahrzeugdata.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(open("static/classification_files/LandfahrzeugClassificationCategorical.csv", "w"))
            data = []
            count = 0
            for row in reader:
                if (count == 0):
                    header_list = ["vectorName", "abmessungen_Breite", "gezogenes_Gerat", "rader_Achsen", "kettenfahrzeug",\
                                  "kettenlaufwerk", "kettendetails", "aufbau_Turm_Turmform", "aufbau_Turm_Turmposition", "radfahrzeug",\
                                  "wanne_Karossiere_Holme_Lafette_Wanne", "wanne_Karossiere_Holme_Lafette_Motor_Motorposition",\
                                  "wanne_Karossiere_Holme_Lafette_Wanne_Form_Kastenformig", "wanne_Karossiere_Holme_Lafette_Wanne_Form_Draufsicht_Bug",\
                                  "wanne_Karossiere_Holme_Lafette_Wanne_Form_Draufsicht_Heck", "zusatzinformationen_Familie", \
                                  "wanne_Karossiere_Holme_Lafette_Lucken", "wanne_Karossiere_Holme_Lafette_Motor_Motorposition_Hinten_Mitte", "result"]
                    writer.writerow(header_list)
                    count += 1
                    continue
                else:
                    rule1, rule2, rule3, rule4, rule5, rule6 = 1, 1, 1, 1, 1, 1

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


                    if (rule1 == 0 and rule2 == 0 and rule3 == 0 and rule4 == 0 and rule5 == 0 and rule6 == 0):
                        result = 1
                    else:
                        result = 0

                    #result1 = str(rule1) + str(rule2) + str(rule3) + str(rule4) + str(rule5) + str(rule6) + str(result)
                    result1 = str(result)

                    list = [row[4771], row[978], row[2114], row[1881], row[2668], row[769], row[2917], row[1722], row[4342], row[2796], row[1169], \
                            row[4141], row[1790], row[4571], row[911], row[13], row[1522], row[4372], result1]

                    writer.writerow(list)