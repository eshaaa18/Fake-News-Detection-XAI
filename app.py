import streamlit as st
from train_model import train
from explain import get_explanation
from chatbot import generate_response

st.title("Fake News Detection with Explanation")

# Cache model (VERY IMPORTANT)
@st.cache_resource
def load_model():
    return train()

try:
    model, vectorizer, acc, precision, recall, f1 = load_model()
except Exception as e:
    st.error(f"Error in training: {e}")
    st.stop()

user_input = st.text_area("Enter News Article")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        vec = vectorizer.transform([user_input])

        pred = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0]
        confidence = max(proba)

        label = "Fake" if pred == 1 else "Real"

        st.success(f"Prediction: {label}")
        st.info(f"Confidence: {confidence:.2f}")

        # Metrics (Professional UI)
        st.subheader("Model Performance")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Accuracy", f"{acc:.2f}")
        col2.metric("Precision", f"{precision:.2f}")
        col3.metric("Recall", f"{recall:.2f}")
        col4.metric("F1 Score", f"{f1:.2f}")

        explanation = get_explanation(model, vectorizer, user_input)

        st.subheader("Key Influencing Words:")
        for word, weight in explanation:
            st.write(f"{word} ({weight:.3f})")

        response = generate_response(pred, explanation)

        st.subheader("Explanation:")
        st.write(response)