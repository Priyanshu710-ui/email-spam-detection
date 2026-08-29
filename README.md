# 📧 Spam Sentinel

<p align="center">
  <strong>Real-world NLP powered email spam detection</strong><br/>
  Classify emails as <strong>Spam</strong> or <strong>Legitimate</strong> with TF-IDF + Linear SVM.
</p>

<p align="center">
  <a href="https://github.com/Priyanshu710-ui/email-spam-detection"><img src="https://img.shields.io/github/stars/Priyanshu710-ui/email-spam-detection?style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/Priyanshu710-ui/email-spam-detection"><img src="https://img.shields.io/github/license/Priyanshu710-ui/email-spam-detection?style=for-the-badge" alt="License"></a>
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/NLP-TF--IDF-purple?style=for-the-badge" alt="NLP">
</p>

---

## 🚀 What is Spam Sentinel?

**Spam Sentinel** is an end-to-end machine learning project that detects whether an email is **spam** or **legitimate (ham)**.

Instead of using a tiny synthetic dataset, the project processes **real email messages from the SpamAssassin public corpus**, performs NLP preprocessing, converts text into TF-IDF features, compares multiple machine-learning algorithms, and serves the winning model through a Streamlit application.

### ✨ Why this project is worth checking out

- 🧠 Real NLP pipeline from raw email text to prediction
- 📚 **4,273 unique emails** after cleaning and duplicate removal
- 🔤 TF-IDF with **unigrams + bigrams**
- 🤖 Compares **Naive Bayes, Logistic Regression, and Linear SVM**
- 🏆 **Linear SVM** selected as the best model
- 📈 **98.60% held-out test accuracy**
- 🎯 **0.980 spam F1-score**
- 🔍 Shows influential text features behind predictions
- 🖥️ Interactive Streamlit interface
- 📊 Includes an EDA notebook for data analysis

---

## 🏆 Model Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Multinomial Naive Bayes | 97.89% | 97.31% | 96.66% | 96.98% |
| Logistic Regression | 98.13% | 96.70% | 97.99% | 97.34% |
| **Linear SVM 🏆** | **98.60%** | **97.67%** | **98.33%** | **98.00%** |

> **Evaluation note:** results are reported on the held-out test split used during training. They should not be interpreted as production accuracy on arbitrary future email traffic.

---

## 🧩 How It Works

```text
                    📩 Raw Email
                         │
                         ▼
                🧹 Text Preprocessing
                         │
                         ▼
              🔤 TF-IDF Feature Extraction
                 (Unigrams + Bigrams)
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
       Naive Bayes   Logistic Reg.  Linear SVM
            │            │            │
            └────────────┼────────────┘
                         ▼
                 📊 Model Evaluation
                         │
                         ▼
                  🏆 Best Model
                         │
                         ▼
                  🖥️ Streamlit App
                         │
                         ▼
                 🚨 Spam / ✅ Ham
```

---

## 📊 Dataset

The project uses email messages collected from the **Apache SpamAssassin public corpus**.

After extraction, text cleaning, and exact duplicate removal:

| Class | Emails |
|---|---:|
| ✅ Ham | 2,776 |
| 🚨 Spam | 1,497 |
| **Total** | **4,273** |

The raw corpus is intentionally **not committed to this repository**. The `data/raw/` directory is ignored by Git.

---

## 🧠 NLP Pipeline

Each email passes through a preprocessing pipeline that includes:

1. HTML cleanup
2. URL normalization
3. Whitespace normalization
4. Tokenization
5. Stopword removal
6. Stemming/normalization
7. TF-IDF vectorization
8. Unigram + bigram feature extraction

This turns unstructured email text into numerical features that classical machine-learning algorithms can learn from.

---

## 🤖 Models Compared

### Multinomial Naive Bayes
A strong baseline for sparse text classification.

### Logistic Regression
A linear classifier that performs well with high-dimensional TF-IDF features.

### Linear SVM 🏆
The best-performing model in this project, achieving a **0.980 spam F1-score** on the held-out test set.

The best model and TF-IDF vectorizer are saved under `model/` for use by the Streamlit application.

---

## 🖥️ Streamlit App

The app lets users paste an email and receive a prediction in real time.

### What it provides

- 🚨 Spam / ✅ Legitimate prediction
- 📊 Prediction score display
- 🔍 Influential TF-IDF features contributing to the prediction
- 🧹 View of the processed text
- 🤖 Model information

### Example

```text
Input:
"Congratulations! You have won a FREE prize. Click here to claim your reward!"

Output:
🚨 SPAM DETECTED
```

---

## 📂 Project Structure

```text
email-spam-detection/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── prepare_dataset.py
│   ├── generate_dataset.py
│   └── spam.csv
│
├── model/
│   ├── model_results.csv
│   ├── spam_classifier.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── 01_EDA.ipynb
│
└── src/
    ├── preprocess.py
    └── train.py
```

---

## ⚙️ Run Locally

### 1. Clone the repository

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

The repository expects `data/spam.csv` with `label` and `text` columns.

To rebuild it from the raw SpamAssassin corpus, place the corpus folders inside `data/raw/` and run:

```bash
python data/prepare_dataset.py
```

### 5. Train the models

```bash
python src/train.py
```

This creates:

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

## 🧪 EDA

The `notebooks/01_EDA.ipynb` notebook explores:

- Dataset shape and integrity
- Missing values and duplicates
- Ham vs spam distribution
- Email-length distribution
- Common words in spam emails
- Common words in legitimate emails
- Model performance comparison

---

## 🔍 Explainability

The application uses the trained **Linear SVM coefficients** together with the email's TF-IDF representation to identify the words/phrases that contribute most strongly to the classification.

For example, a spam prediction may surface terms such as:

```text
free
claim
prize
click
winner
```

These are presented as **influential model features**, not as a guarantee that a message is malicious.

---

## 🎯 Skills Demonstrated

- Natural Language Processing
- Text preprocessing
- Tokenization
- Stopword removal
- Stemming
- TF-IDF
- N-gram feature engineering
- Supervised machine learning
- Model comparison
- Precision / Recall / F1 evaluation
- Class-imbalance awareness
- Model persistence with pickle
- Streamlit application development
- Exploratory data analysis

---

## 🔮 Future Improvements

- Calibrated probability estimates for the SVM
- Precision-recall and ROC analysis
- Cross-validation and stronger leakage checks
- Automated model retraining
- Containerized deployment
- Larger and more diverse email corpora
- Improved feature explanations and monitoring

---

## 👨‍💻 Author

### Priyanshu Sharma

Built as a practical NLP + machine-learning portfolio project focused on turning an end-to-end classification workflow into a usable application.

⭐ **Star the repository if you found it useful!**

---

## 📄 License

MIT License — feel free to use, modify, and learn from this project.
