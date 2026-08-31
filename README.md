<div align="center">

# 🛡️ SPAM SENTINEL

### 📧 An NLP-powered email threat detector built for the real world.

**Detect. Explain. Classify.**

<p>
  <a href="https://github.com/Priyanshu710-ui/email-spam-detection"><img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://email-spam-detection-hthq9z.streamlit.app"><img src="https://img.shields.io/badge/🚀%20Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo"></a>
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NLP-TF--IDF-8B5CF6?style=for-the-badge" alt="NLP">
  <img src="https://img.shields.io/badge/ML-Linear%20SVM-FF6B35?style=for-the-badge" alt="Machine Learning">
</p>

<p><strong>4,273 real emails</strong> · <strong>3 ML models compared</strong> · <strong>98.60% test accuracy</strong> · <strong>0.980 spam F1</strong></p>

</div>

---

## 🚀 Live Demo

### Try it in your browser

**[🛡️ Launch Spam Sentinel](https://email-spam-detection-hthq9z.streamlit.app)**

Paste an email → run the classifier → see **SPAM** or **LEGITIMATE** with model insights.

> The app is a portfolio/demo deployment. Reported model metrics come from the held-out test split used during training.

---

## 🧠 What Is Spam Sentinel?

**Spam Sentinel** is an end-to-end **Natural Language Processing + Machine Learning** system that classifies emails as **Spam** or **Legitimate (Ham)**.

Instead of stopping at a notebook, the project takes the full journey:

```text
Real Email Corpus
       ↓
Data Cleaning & Deduplication
       ↓
NLP Preprocessing
       ↓
TF-IDF + Unigrams/Bigrams
       ↓
Model Training & Comparison
       ↓
Linear SVM 🏆
       ↓
Streamlit Web App
       ↓
Spam / Legitimate + Explanations
```

The result is a practical ML application rather than a model sitting unused inside a notebook.

---

## 💥 Why This Project Stands Out

| 🔥 | Capability | What it demonstrates |
|---|---|---|
| 📚 | **Real-world dataset** | Apache SpamAssassin public corpus |
| 🧹 | **Data engineering** | Cleaning, parsing and exact duplicate removal |
| 🧠 | **NLP pipeline** | Text normalization, tokenization and stopword handling |
| 🔤 | **Feature engineering** | TF-IDF with unigrams + bigrams |
| 🤖 | **Model benchmarking** | Naive Bayes vs Logistic Regression vs Linear SVM |
| 🏆 | **Best model selection** | Linear SVM achieved the strongest held-out performance |
| 🔍 | **Explainability** | Surfaces influential text features behind predictions |
| 🖥️ | **Deployment** | Interactive Streamlit application |
| 📊 | **EDA** | Dedicated notebook for dataset exploration |

---

## 🏆 Model Performance

Three classical text-classification approaches were trained and compared on the held-out test split.

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayes | 97.89% | 97.31% | 96.66% | 96.98% |
| Logistic Regression | 98.13% | 96.70% | 97.99% | 97.34% |
| **Linear SVM 🏆** | **98.60%** | **97.67%** | **98.33%** | **98.00%** |

### 🥇 Winner: Linear SVM

**98.60% accuracy** with a **0.980 spam F1-score** on the held-out test set.

> ⚠️ These numbers are evaluation results for this dataset and split. They should not be treated as guaranteed production accuracy on arbitrary future email traffic.

---

## 🗂️ Dataset

The project uses email messages from the **Apache SpamAssassin public corpus**.

After cleaning and removing exact duplicates:

| Class | Count |
|---|---:|
| ✅ Legitimate / Ham | 2,776 |
| 🚨 Spam | 1,497 |
| **Total** | **4,273** |

### Why real data matters

Spam detection depends on vocabulary, formatting, and patterns found in genuine messages. A real public corpus makes the workflow more meaningful than a tiny synthetic dataset.

The raw corpus is **not committed to this repository**; `data/raw/` is ignored by Git.

---

## ⚙️ NLP Pipeline

Every message moves through a reproducible text-processing workflow:

```text
📩 Raw Email
   │
   ├── HTML cleanup
   ├── URL normalization
   ├── Whitespace normalization
   ├── Tokenization
   ├── Stopword removal
   └── Stemming / normalization
   │
   ▼
🔤 TF-IDF Vectorization
   │
   ├── Unigrams
   └── Bigrams
   │
   ▼
🤖 ML Classifier
   │
   ▼
🚨 Spam / ✅ Legitimate
```

This converts messy natural-language email content into sparse numerical features that classical machine-learning models can learn from effectively.

---

## 🤖 Models Compared

### 1. Multinomial Naive Bayes
A strong baseline for sparse text classification.

### 2. Logistic Regression
A linear classifier that works well with high-dimensional TF-IDF representations.

### 3. Linear SVM 🏆
The best-performing model in this project, selected using the held-out evaluation results.

The trained classifier and TF-IDF vectorizer are persisted in `model/` so the Streamlit app can load them directly.

---

## 🔍 Explainable Predictions

Spam detection should not feel like a black box.

Spam Sentinel uses the trained **Linear SVM coefficients** together with the email's TF-IDF representation to identify influential terms contributing to a classification.

A spam prediction could surface signals such as:

```text
free
claim
winner
prize
click
```

These are **model features that influenced the prediction**, not proof that any individual word is inherently malicious.

---

## 🖥️ Streamlit App

The web app provides an interactive interface for testing emails in real time.

### 🎯 Features

- 🚨 Spam / ✅ Legitimate classification
- 📊 Prediction score display
- 🔍 Influential TF-IDF feature visualization
- 🧹 Processed-text view
- 🤖 Model information
- ⚡ Instant predictions in the browser

### Example

```text
Input:
"Congratulations! You have won a FREE prize. Click here to claim your reward!"

Prediction:
🚨 SPAM DETECTED
```

---

## 📊 Project Architecture

```text
                         ┌──────────────────────┐
                         │      User Email       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Text Preprocessing  │
                         │  HTML / URLs / Text  │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      TF-IDF          │
                         │  Uni + Bi-grams      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │        Linear SVM 🏆         │
                    └──────────────┬───────────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     ▼                           ▼
              🚨 SPAM DETECTED           ✅ LEGITIMATE
                     │                           │
                     └─────────────┬─────────────┘
                                   ▼
                         🔍 Feature Explanation
```

---

## 📁 Project Structure

```text
email-spam-detection/
│
├── app.py                         # Streamlit application
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── .gitignore
│
├── data/
│   ├── prepare_dataset.py         # Raw corpus → clean dataset
│   ├── generate_dataset.py
│   └── spam.csv
│
├── model/
│   ├── model_results.csv          # Benchmark results
│   ├── spam_classifier.pkl        # Trained classifier
│   └── vectorizer.pkl             # TF-IDF vectorizer
│
├── notebooks/
│   └── 01_EDA.ipynb              # Exploratory data analysis
│
└── src/
    ├── preprocess.py              # NLP preprocessing
    └── train.py                   # Model training + evaluation
```

---

## ⚡ Run It Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Priyanshu710-ui/email-spam-detection.git
cd email-spam-detection
```

### 2️⃣ Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare the dataset

The project expects `data/spam.csv` containing:

```text
label,text
```

To rebuild it from the raw SpamAssassin corpus, place the corpus folders in `data/raw/` and run:

```bash
python data/prepare_dataset.py
```

### 5️⃣ Train the models

```bash
python src/train.py
```

This generates:

```text
model/spam_classifier.pkl
model/vectorizer.pkl
model/model_results.csv
```

### 6️⃣ Launch the app

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

---

## 🔬 Exploratory Data Analysis

The `notebooks/01_EDA.ipynb` notebook investigates:

- Dataset shape and integrity
- Missing values and duplicates
- Ham vs spam distribution
- Email-length distribution
- Common words in spam
- Common words in legitimate messages
- Model performance comparison

---

## 🧪 Example Workflow

```text
Paste email
     ↓
Click classify
     ↓
Clean + transform text
     ↓
Generate TF-IDF representation
     ↓
Run Linear SVM
     ↓
Return class + score
     ↓
Show influential features
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | **Python 3.12+** |
| NLP | **TF-IDF, tokenization, stopwords, stemming** |
| ML | **scikit-learn** |
| Best Model | **Linear SVM** |
| App | **Streamlit** |
| Data Analysis | **Pandas + Jupyter** |
| Model Persistence | **Pickle** |
| Dataset | **SpamAssassin public corpus** |

---

## 🎓 Skills Demonstrated

This project covers a complete applied-ML workflow:

**Data → Cleaning → NLP → Feature Engineering → Training → Benchmarking → Explainability → Deployment**

Core skills demonstrated:

- Natural Language Processing
- Text preprocessing
- TF-IDF feature engineering
- Unigram / bigram modeling
- Supervised machine learning
- Model comparison
- Precision / Recall / F1 evaluation
- Class-imbalance awareness
- Model persistence
- Exploratory data analysis
- Streamlit deployment

---

## 🔮 Roadmap

- [x] Real-world email dataset
- [x] NLP preprocessing pipeline
- [x] TF-IDF unigrams + bigrams
- [x] Compare 3 ML algorithms
- [x] Select best-performing model
- [x] Persist trained model
- [x] Streamlit interface
- [x] Feature-level explanations
- [ ] Calibrated probability estimates
- [ ] Precision-recall / ROC visualizations
- [ ] Cross-validation and stronger leakage checks
- [ ] Automated model retraining
- [ ] Containerized deployment
- [ ] Larger and more diverse email corpora

---

## 📌 Project Takeaway

Spam detection is not just about training a classifier.

The interesting engineering challenge is building the **whole system** around the model: cleaning messy text, choosing useful representations, benchmarking multiple algorithms, explaining predictions, persisting the winning pipeline, and exposing it through a usable interface.

**That is what Spam Sentinel is built to demonstrate.**

---

## 👨‍💻 Author

### Priyanshu Sharma

Built as a practical **NLP + Machine Learning portfolio project** focused on turning an end-to-end text-classification workflow into a usable application.

**Repository:** https://github.com/Priyanshu710-ui/email-spam-detection  
**Live Demo:** https://email-spam-detection-hthq9z.streamlit.app

---

<div align="center">

## ⭐ Like the project?

**Star the repo • Try the demo • Explore the code • Build something cool** 🚀

</div>
