# 📧 Email Spam Detection

An NLP project that automatically classifies emails as **Spam** or
**Legitimate (Ham)** using classic text-processing and machine learning
techniques, with a Streamlit UI for live predictions.

## What is it?

Build an NLP model that automatically classifies emails as spam or
legitimate — end to end, from raw text to a deployable web interface.

## Tech Stack

- **Python**
- **Pandas** — data loading and handling
- **Scikit-learn** — TF-IDF vectorization, Naive Bayes classifier, evaluation
- **NLTK** — tokenization, stopword removal, stemming
- **Streamlit** — interactive prediction interface

## Core Features

- Text preprocessing (lowercasing, URL/HTML/punctuation/number stripping)
- Tokenization
- Feature extraction (TF-IDF, unigrams + bigrams)
- Spam classification (Multinomial Naive Bayes)
- Prediction interface (Streamlit web app)

## Skills You'll Learn

- Natural Language Processing
- TF-IDF
- Text classification
- Feature extraction
- Model evaluation

## Project Structure

```
email-spam-detection/
├── app.py                     # Streamlit prediction interface
├── requirements.txt
├── data/
│   ├── generate_dataset.py    # Generates the sample training dataset
│   └── spam.csv                # (created after running the generator)
├── model/                     # Saved vectorizer + trained model (.pkl)
├── src/
│   ├── preprocess.py          # Text cleaning / tokenization utilities
│   └── train.py                # Trains and saves the model
└── README.md
```

## Getting Started

### 1. Clone and set up a virtual environment

```bash
git clone https://github.com/<your-username>/email-spam-detection.git
cd email-spam-detection
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Generate the dataset

This repo ships with a script that generates a synthetic but realistic
labeled dataset (`data/spam.csv`), so you can run everything immediately
without hunting for external data.

```bash
python data/generate_dataset.py
```

> Want to use a real-world dataset instead (e.g. the SMS Spam Collection
> or Enron Spam dataset)? Just replace `data/spam.csv` with a CSV that has
> two columns: `label` (`spam`/`ham`) and `text`.

### 3. Train the model

```bash
python src/train.py
```

This will clean the text, extract TF-IDF features, train a Multinomial
Naive Bayes classifier, print accuracy/precision/recall, and save the
fitted vectorizer and model to `model/`.

### 4. Launch the app

```bash
streamlit run app.py
```

Paste in an email and click **Predict** to see whether it's classified as
spam or legitimate, along with the model's confidence.

## Why Recruiters Love It

It's a simple project that demonstrates practical NLP, while still being
understandable and deployable.

## Resume Impact

Shows experience working with unstructured text data and classification
models.

## License

MIT — feel free to use this project as a portfolio piece or starting point.
