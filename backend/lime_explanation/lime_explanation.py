import lime
import lime.lime_tabular

class LimeExplanation:

    def __init__(self):
        pass

    def explainer(self, train, feature_names, class_names):
        self.explainer = lime.lime_tabular.LimeTabularExplainer(train, feature_names=feature_names, class_names=class_names, discretize_continuous=True)

    def explainInstance(self, test, predict_proba ,num_features):
        self.exp = self.explainer.explain_instance(test, predict_proba, num_features=num_features)
        return self.exp

    def save(self, domain):
        #self.exp.save_to_file("static/lime_explanation_html/" + domain + "explain.html")
        #print("file saved to " + "static/lime_explanation_html/" + domain + "explain.html")
        fig = self.exp.as_pyplot_figure()
        print(fig.get_dpi())
        fig.savefig("static/lime_explanation_images/" + domain + "_explanation.png")
        fig.savefig("static/lime_explanation_images/" + domain + "_explanation.pdf")
        print("figure saved")