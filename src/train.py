"""
train.py
--------
Trains and compares multiple NLP classification models using
TF-IDF features.

Models:
    1. Multinomial Naive Bayes
    2. Logistic Regression
    3. Linear SVM

The best model is selected using F1-score and saved along
with the TF-IDF vectorizer.
"""

import os
import pickle

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import LinearSVC


from preprocess import preprocess_series


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "spam.csv"
)

MODEL_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model"
)


# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

def load_data(path=DATA_PATH):

    df = pd.read_csv(path)

    # Remove missing values
    df = df.dropna(
        subset=["label", "text"]
    )

    # Normalize labels
    df["label"] = (
        df["label"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Keep only valid labels
    df = df[
        df["label"].isin(["spam", "ham"])
    ]

    # Remove duplicate emails
    df = df.drop_duplicates(
        subset=["text"]
    )

    return df


# ---------------------------------------------------------
# Main Training Pipeline
# ---------------------------------------------------------

def main():

    print("=" * 70)
    print("EMAIL SPAM DETECTION - MODEL TRAINING")
    print("=" * 70)

    # -----------------------------------------------------
    # Load data
    # -----------------------------------------------------

    print("\n[1/6] Loading dataset...")

    df = load_data()

    spam_count = (
        df["label"] == "spam"
    ).sum()

    ham_count = (
        df["label"] == "ham"
    ).sum()

    print(f"Total emails : {len(df)}")
    print(f"Spam emails  : {spam_count}")
    print(f"Ham emails   : {ham_count}")

    # -----------------------------------------------------
    # Preprocessing
    # -----------------------------------------------------

    print("\n[2/6] Preprocessing text...")

    df["clean_text"] = preprocess_series(
        df["text"]
    )

    # Remove emails that become empty
    df = df[
        df["clean_text"].str.strip() != ""
    ]

    # -----------------------------------------------------
    # Train / Test split
    # -----------------------------------------------------

    print("\n[3/6] Creating train/test split...")

    X_train, X_test, y_train, y_test = train_test_split(
        df["clean_text"],
        df["label"],
        test_size=0.20,
        random_state=42,
        stratify=df["label"]
    )

    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    # -----------------------------------------------------
    # TF-IDF
    # -----------------------------------------------------

    print("\n[4/6] Extracting TF-IDF features...")

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        min_df=2,
        sublinear_tf=True
    )

    X_train_vec = vectorizer.fit_transform(
        X_train
    )

    X_test_vec = vectorizer.transform(
        X_test
    )

    print(
        f"TF-IDF vocabulary size: "
        f"{len(vectorizer.vocabulary_)}"
    )

    # -----------------------------------------------------
    # Models
    # -----------------------------------------------------

    print("\n[5/6] Training models...")

    models = {

        "Naive Bayes": MultinomialNB(),

        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            random_state=42
        ),

        "Linear SVM": LinearSVC(
            class_weight="balanced",
            random_state=42
        )
    }

    results = {}

    best_model = None
    best_model_name = None
    best_f1 = -1

    # -----------------------------------------------------
    # Train + Evaluate
    # -----------------------------------------------------

    for name, model in models.items():

        print("\n" + "-" * 70)
        print(f"Training: {name}")
        print("-" * 70)

        model.fit(
            X_train_vec,
            y_train
        )

        predictions = model.predict(
            X_test_vec
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions,
            pos_label="spam",
            zero_division=0
        )

        recall = recall_score(
            y_test,
            predictions,
            pos_label="spam",
            zero_division=0
        )

        f1 = f1_score(
            y_test,
            predictions,
            pos_label="spam",
            zero_division=0
        )

        results[name] = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

        print(f"Accuracy  : {accuracy:.4f}")
        print(f"Precision : {precision:.4f}")
        print(f"Recall    : {recall:.4f}")
        print(f"F1 Score  : {f1:.4f}")

        print("\nClassification Report:")
        print(
            classification_report(
                y_test,
                predictions,
                zero_division=0
            )
        )

        print(
            "Confusion Matrix "
            "(rows=true, columns=predicted)"
        )

        print(
            confusion_matrix(
                y_test,
                predictions,
                labels=["ham", "spam"]
            )
        )

        # Select best model using spam F1
        if f1 > best_f1:

            best_f1 = f1
            best_model = model
            best_model_name = name

    # -----------------------------------------------------
    # Model comparison
    # -----------------------------------------------------

    print("\n" + "=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)

    results_df = pd.DataFrame(
        results
    ).T

    print(
        results_df.round(4)
    )

    # -----------------------------------------------------
    # Best model
    # -----------------------------------------------------

    print("\n" + "=" * 70)
    print("BEST MODEL")
    print("=" * 70)

    print(
        f"Selected model: {best_model_name}"
    )

    print(
        f"Spam F1-score: {best_f1:.4f}"
    )

    # -----------------------------------------------------
    # Save model
    # -----------------------------------------------------

    print("\n[6/6] Saving model...")

    os.makedirs(
        MODEL_DIR,
        exist_ok=True
    )

    vectorizer_path = os.path.join(
        MODEL_DIR,
        "vectorizer.pkl"
    )

    model_path = os.path.join(
        MODEL_DIR,
        "spam_classifier.pkl"
    )

    results_path = os.path.join(
        MODEL_DIR,
        "model_results.csv"
    )

    with open(
        vectorizer_path,
        "wb"
    ) as f:

        pickle.dump(
            vectorizer,
            f
        )

    with open(
        model_path,
        "wb"
    ) as f:

        pickle.dump(
            best_model,
            f
        )

    results_df.to_csv(
        results_path
    )

    print(
        f"\nVectorizer saved to:"
        f"\n{vectorizer_path}"
    )

    print(
        f"\nBest model saved to:"
        f"\n{model_path}"
    )

    print(
        f"\nModel results saved to:"
        f"\n{results_path}"
    )

    print("\n" + "=" * 70)
    print("TRAINING COMPLETE 🚀")
    print("=" * 70)


if __name__ == "__main__":
    main()