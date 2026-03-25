import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def load_data():
    fake = pd.read_csv("data/Fake.csv")
    true = pd.read_csv("data/True.csv")

    # Combine title + text
    fake['text'] = fake['title'] + " " + fake['text']
    true['text'] = true['title'] + " " + true['text']

    fake['label'] = 1
    true['label'] = 0

    df = pd.concat([fake, true])

    df = df[['text', 'label']]
    df['text'] = df['text'].apply(clean_text)

    return df