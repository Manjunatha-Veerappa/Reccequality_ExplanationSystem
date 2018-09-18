from sklearn.ensemble import RandomForestClassifier
import sklearn
import sklearn.datasets
import sklearn.ensemble
import sklearn.model_selection

class RandomForest:

    def __init__(self):
        self.classifier = None
        pass

    def split_dataset(self, data, labels, train_percentage):

        self.train, self.test, self.labels_train, self.labels_test = sklearn.model_selection.train_test_split(
            data, labels, train_size=train_percentage)

        return self.train, self.test, self.labels_train, self.labels_test

    def random_forest_classifier(self, features, target):
        self.classifier = RandomForestClassifier()
        self.classifier.fit(features, target)
        return self.classifier

    def predictProba(self, input):
        return self.classifier.predict_proba(input)

    def predict_proba(self, input):
        return self.predictProba(input)


