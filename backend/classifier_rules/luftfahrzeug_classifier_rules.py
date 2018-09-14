import csv

class LuftfahrzeugClassifierRules(object):

    def __init__(self):
        self.luftfahrzueg_classifier_rules()

    def luftfahrzueg_classifier_rules(self):
        with open("static/dataset/Luftfahrzeugdata.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            writer = csv.writer(open("static/classification_files/LuftfahrzeugClassificationCategorical.csv", "w"))
            data = []
            count = 0
            for row in reader:
                if (count == 0):
                    header_list = ["vectorName", "abmessungen_Lange", "starrflugler", "tragflachen", "triebwerke", "rumpf", "leitwerk",
                   "drehflugler", "drehflugler_Rumpf_Cockpit", "doppeldecker", "tragflachen_Stellung_Gerade", "hochDecker",
                   "triebwerke_triebwerksart", "rumpf_Rumpfformen", "drehflugler_Rotor", "drehflugler_Triebwerk", "drehflugler_Rumpf",
                   "drehflugler_Heckausleger", "drehflugler_Triebwerk_Lufteinlass", "drehflugler_Triebwerk_Luftauslass",
                   "zusatzinformationen_Familie", "drehflugler_Rotor_EinzelRotor_Rotorblatter",
                   "drehflugler_Triebwerk_Position_UberdemRumpf_Anzahl", "result"]
                    writer.writerow(header_list)
                    count += 1
                    continue
                else:
                    rule1, rule2, rule3, rule4, rule5, rule6, rule7 = 1, 1, 1, 1, 1, 1, 1

                    if (int(row[412]) == 0):
                        if (int(row[707]) == 0 and int(row[1088]) == 0 and int(row[791]) == 0 and int(row[33]) == 0):
                            rule1 = 0
                    else:
                        rule1 = 0

                    if (int(row[687]) == 0):
                        if (int(row[314]) == 0):
                            rule2 = 0
                    else:
                        rule2 = 0

                    if (int(row[970]) == 0):
                        if (int(row[1176]) == 0):
                            rule3 = 0
                    else:
                        rule3 = 0

                    if (int(row[930]) == 0):
                        if (int(row[707]) == 0 and int(row[126]) == 0 and int(row[740]) == 0):
                            rule4 = 0
                    else:
                        rule4 = 0

                    if (int(row[687]) == 0):
                        if (int(row[350]) == 0 and int(row[966]) == 0 and int(row[1067]) == 0 and int(row[279]) == 0):
                            rule5 = 0
                    else:
                        rule5 = 0

                    if (int(row[1068]) == 0):
                        if (int(row[282]) == 0):
                            rule6 = 0
                    else:
                        rule6 = 0

                    if (float(row[1003]) >= 2.0 and  float(row[1003])<= 89.0):
                        rule7 = 0

                    if (rule1 == 0 and rule2 == 0 and rule3 == 0 and rule4 == 0 and rule5 == 0 and rule6 == 0 and rule7 == 0):
                        result = 1
                    else:
                        result = 0

                    #result1 = str(rule1) + str(rule2) + str(rule3) + str(rule4) + str(rule5) + str(rule6) + str(rule7) + str(result)
                    result1 = str(result)

                    list = [row[1263], row[1003], row[412], row[707], row[1088], row[791], row[33], row[687], row[314], row[970], row[1176], \
                    row[930], row[126], row[740], row[350], row[966], row[1067], row[279], row[1068], row[282], row[607], row[874], row[911], result1]

                    writer.writerow(list)