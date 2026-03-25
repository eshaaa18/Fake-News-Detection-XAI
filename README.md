# Fake News Detection with Explainable AI

## Overview

This project is an NLP-based system that detects whether a news article is **Fake or Real** and provides **interpretable explanations** for its predictions using Explainable AI techniques.

Unlike traditional classifiers, this system not only predicts outcomes but also explains *why* a piece of news is classified as fake or real.

---

## Features

* Fake vs Real news classification
* Confidence score for predictions
* Explainable AI using LIME (word importance)
* Chatbot-style reasoning for user-friendly explanations
* Interactive UI using Streamlit

---

## Tech Stack

* **Language:** Python
* **ML/NLP:** Scikit-learn (TF-IDF, Logistic Regression)
* **Explainability:** LIME
* **Frontend:** Streamlit

---

## Model Performance

* **Accuracy:** ~0.93
* **Precision:** ~0.92
* **Recall:** ~0.94
* **F1 Score:** ~0.93

> Note: Metrics may vary slightly due to random train-test split.

---

## Project Structure

```
MLproj/
├── data/                # Dataset (not included)
├── app.py               # Streamlit UI
├── train_model.py       # Model training + evaluation
├── preprocessing.py     # Data cleaning & loading
├── explain.py           # LIME explanations
├── chatbot.py           # Explanation generator
├── requirements.txt     # Dependencies
└── README.md
```

---

 How to Run

### 1. Clone the repository

```
git clone https://github.com/eshaaa18/Fake-News-Detection-XAI.git
cd Fake-News-Detection-XAI
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```

Dataset

Dataset not included due to size.

Download from Kaggle:
*Fake and Real News Dataset

Place files in:
```
data/
├── Fake.csv
├── True.csv
```


(Add screenshots of your app here — input, prediction, explanation)

 Limitations

* Model relies on textual patterns, not factual verification
* Does not fetch real-time news or external sources
* Performance depends on dataset quality

Future Improvements

* Add deep learning models (LSTM/BERT)
* Improve UI with advanced visualization
* Integrate real-time fact-checking APIs


If you found this useful
Give this repo a star and feel free to connect!
