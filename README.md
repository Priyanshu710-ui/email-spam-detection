<div align="center">

# 🛡️ SPAM SENTINEL

### 🧠 Production-style NLP Email Spam Detection

**Detect spam. Understand why. Deploy it.**

<p>
  <a href="https://github.com/Priyanshu710-ui/email-spam-detection"><img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://email-spam-detection-hthq9z.streamlit.app"><img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo"></a>
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NLP-TF--IDF-8B5CF6?style=for-the-badge" alt="NLP">
  <img src="https://img.shields.io/badge/ML-Linear%20SVM-FF6B35?style=for-the-badge" alt="Machine Learning">
  <img src="https://img.shields.io/badge/App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
</p>

<p>
  <strong>4,273 real emails</strong> &nbsp;•&nbsp;
  <strong>3 ML models</strong> &nbsp;•&nbsp;
  <strong>98.60% accuracy</strong> &nbsp;•&nbsp;
  <strong>0.980 spam F1</strong>
</p>

</div>

---

## 🚀 Try It Now

<p align="center">
  <a href="https://email-spam-detection-hthq9z.streamlit.app"><strong>🛡️ OPEN SPAM SENTINEL →</strong></a>
</p>

Paste an email, classify it, and inspect the model signals behind the prediction.

> **Demo:** https://email-spam-detection-hthq9z.streamlit.app

---

## ⚡ What This Project Does

Spam Sentinel is an end-to-end **Natural Language Processing + Machine Learning** system for classifying emails as **Spam** or **Legitimate (Ham)**.

It is built as a complete ML workflow rather than a notebook-only experiment:

```text
📨 Raw Email Corpus
        ↓
🧹 Cleaning & Deduplication
        ↓
🧠 NLP Preprocessing
        ↓
🔤 TF-IDF + Unigrams / Bigrams
        ↓
🤖 Model Training & Benchmarking
        ↓
🏆 Linear SVM
        ↓
💾 Saved Model + Vectorizer
        ↓
🖥️ Streamlit Application
        ↓
🚨 SPAM / ✅ LEGITIMATE
        ↓
🔍 Influential Feature Explanation
```

### The core idea

**Turn messy email text into useful numerical features, train strong classical classifiers, select the best model, then wrap the result in a usable web app.**

---

## 🏆 Results That Matter

Three models were trained and evaluated on the held-out test split:

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayes | 97.89% | 97.31% | 96.66% | 96.98% |
| Logistic Regression | 98.13% | 96.70% | 97.99% | 97.34% |
| **Linear SVM 🏆** | **98.60%** | **97.67%** | **98.33%** | **98.00%** |

### 🥇 Best model: Linear SVM

**98.60% accuracy** and **0.980 spam F1** on the held-out test set.

> ⚠️ These are dataset-specific evaluation results. They are not a guarantee of performance on arbitrary real-world email traffic.

---

## 🎯 Why Spam Sentinel Is More Than a Classifier

| Capability | What it shows |
|---|---|
| 📚 Real-world data | Apache SpamAssassin public corpus |
| 🧹 Data cleaning | Parsing, normalization and exact duplicate removal |
| 🧠 NLP | Text normalization, tokenization, stopword handling |
| 🔤 Feature engineering | TF-IDF with unigrams + bigrams |
| 🤖 Benchmarking | Naive Bayes vs Logistic Regression vs Linear SVM |
| 🏆 Model selection | Best held-out performance drives model choice |
| 🔍 Explainability | Influential text features for each prediction |
| 🖥️ Deployment | Interactive Streamlit application |
| 📊 EDA | Dataset exploration and performance analysis |
| 💾 Reusability | Trained classifier and vectorizer persisted to disk |

---

## 🧠 NLP Pipeline

```text
📩 EMAIL
  │
  ├── HTML cleanup
  ├── URL normalization
  ├── Whitespace normalization
  ├── Tokenization
  ├── Stopword removal
  └── Stemming / normalization
  │
  ▼
🔤 TF-IDF VECTORIZATION
  │
  ├── Unigrams
  └── Bigrams
  │
  ▼
🤖 LINEAR CLASSIFIER
  │
  ▼
┌─────────────────────────────┐
│ 🚨 SPAM   │   ✅ LEGITIMATE │
└─────────────────────────────┘
  │
  ▼
🔍 FEATURE-LEVEL EXPLANATION
```

### Why TF-IDF?

TF-IDF converts text into numerical features based on how informative terms are within the dataset. Combining **unigrams and bigrams** lets the model learn both individual words and short phrases.

---

## 🔍 Explainable Predictions

Spam detection should not be a total black box.

Spam Sentinel uses the trained **Linear SVM coefficients** together with the email's TF-IDF representation to surface features that strongly influence the prediction.

For example, an email might contain influential signals such as:

```text
free
claim
winner
prize
click
```

These are **model features**, not proof that any individual word is malicious by itself.

---

## 📧 Example

### Input

```text
Congratulations! You have won a FREE prize.
Click here to claim your reward now!
```

### Output

```text
🚨 SPAM DETECTED

Why?
• Strong spam-associated vocabulary
• Suspicious call-to-action language
• Model confidence / score
• Influential TF-IDF features
```

---

## 🗂️ Dataset

The project uses email messages from the **Apache SpamAssassin public corpus**.

After cleaning and removing exact duplicates:

| Class | Emails |
|---|---:|
| ✅ Legitimate / Ham | 2,776 |
| 🚨 Spam | 1,497 |
| **Total** | **4,273** |

The raw corpus is **not committed to the repository**; `data/raw/` is ignored by Git.

---

## 🏗️ Architecture

```text
                         ┌────────────────────┐
                         │      USER EMAIL     │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ TEXT PREPROCESSING │
                         │ HTML / URLs / NLP  │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │       TF-IDF       │
                         │  Uni + Bi-grams    │
                         └─────────┬──────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │    LINEAR SVM 🏆   │
                         └─────────┬──────────┘
                                   │
                         ┌─────────┴─────────┐
                         ▼                   ▼
                  🚨 SPAM DETECTED   ✅ LEGITIMATE
                         │                   │
                         └─────────┬─────────┘
                                   ▼
                         🔍 FEATURE EXPLANATION
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

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🐍 Language | Python 3.12+ |
| 🧠 NLP | TF-IDF, tokenization, stopwords, stemming |
| 🤖 ML | scikit-learn |
| 🏆 Best Model | Linear SVM |
| 🖥️ App | Streamlit |
| 📊 Analysis | Pandas + Jupyter |
| 💾 Persistence | Pickle |
| 📚 Dataset | SpamAssassin public corpus |

---

## ⚙️ Run Locally

### 1. Clone

```bash
git clone https://github.com/Priyanshu710-ui/email-spam-detection.git
cd email-spam-detection
```

### 2. Create a virtual environment

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

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the dataset

The project expects:

```text
label,text
```

To rebuild `data/spam.csv` from the raw SpamAssassin corpus, place the corpus folders inside `data/raw/` and run:

```bash
python data/prepare_dataset.py
```

### 5. Train the models

```bash
python src/train.py
```

Generated artifacts:

```text
model/spam_classifier.pkl
model/vectorizer.pkl
model/model_results.csv
```

### 6. Launch the application

```bash
streamlit run app.py
```

---

## 📊 Exploratory Data Analysis

The EDA notebook covers:

- Dataset shape and integrity
- Missing values and duplicates
- Ham vs spam distribution
- Email-length distribution
- Common spam vocabulary
- Common legitimate vocabulary
- Model performance comparison

Notebook:

```text
notebooks/01_EDA.ipynb
```

---

## 🧪 End-to-End Workflow

```text
Paste email
     ↓
Click classify
     ↓
Clean + preprocess
     ↓
Transform with TF-IDF
     ↓
Run Linear SVM
     ↓
Return class + score
     ↓
Surface influential features
```

---

## 🎓 Skills Demonstrated

This project demonstrates a complete applied machine-learning workflow:

**Data → Cleaning → NLP → Feature Engineering → Training → Evaluation → Model Selection → Explainability → Deployment**

Key concepts:

- Natural Language Processing
- Text preprocessing
- TF-IDF feature engineering
- Unigram / bigram modeling
- Supervised machine learning
- Model benchmarking
- Precision, Recall and F1
- Exploratory data analysis
- Model persistence
- Streamlit deployment
- Feature-level interpretability

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

## 💡 Project Takeaway

A spam detector is more interesting when it works as a **system**.

Spam Sentinel connects the pieces that matter in a real ML workflow:

```text
REAL DATA
   +
CLEAN PIPELINE
   +
USEFUL FEATURES
   +
MODEL COMPARISON
   +
EXPLAINABILITY
   +
DEPLOYMENT
   =
A COMPLETE ML APPLICATION 🚀
```

The goal is not just to predict **spam vs legitimate** — it is to demonstrate how a text-classification model can be engineered into something people can actually use.

---

## 👨‍💻 Author

### Priyanshu Sharma

Built as a practical **NLP + Machine Learning portfolio project**.

<p>
  <a href="https://github.com/Priyanshu710-ui/email-spam-detection">📦 Repository</a> •
  <a href="https://email-spam-detection-hthq9z.streamlit.app">🚀 Live Demo</a>
</p>

---

<div align="center">

### ⭐ Like Spam Sentinel?

**Star the repo • Try the demo • Explore the pipeline • Build something cool** 🚀

</div>
