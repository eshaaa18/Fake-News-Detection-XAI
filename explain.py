from lime.lime_text import LimeTextExplainer

class_names = ['Real', 'Fake']

def get_explanation(model, vectorizer, text):
    explainer = LimeTextExplainer(class_names=class_names)

    def predict_proba(texts):
        return model.predict_proba(vectorizer.transform(texts))

    exp = explainer.explain_instance(text, predict_proba, num_features=6)

    return exp.as_list()