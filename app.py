"""
Spam Sentinel
-------------
AI-powered email spam detection using:

    • NLTK
    • TF-IDF
    • Linear SVM
    • Streamlit

Run:
    streamlit run app.py
"""

import os
import pickle
import sys
import math

import streamlit as st


# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(
    BASE_DIR,
    "model"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "spam_classifier.pkl"
)

VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "vectorizer.pkl"
)


# =========================================================
# PREPROCESSING
# =========================================================

SRC_DIR = os.path.join(
    BASE_DIR,
    "src"
)

sys.path.insert(
    0,
    SRC_DIR
)

from preprocess import clean_text


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Spam Sentinel",
    page_icon="📧",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #888888;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .result-title {
        font-size: 1.8rem;
        font-weight: 700;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_artifacts():

    if not os.path.exists(MODEL_PATH):
        return None, None

    if not os.path.exists(VECTORIZER_PATH):
        return None, None

    with open(
        MODEL_PATH,
        "rb"
    ) as f:

        model = pickle.load(f)

    with open(
        VECTORIZER_PATH,
        "rb"
    ) as f:

        vectorizer = pickle.load(f)

    return model, vectorizer


# =========================================================
# PREDICTION + EXPLAINABILITY
# =========================================================

def predict_email(
    email_text,
    model,
    vectorizer
):

    # -----------------------------------------------------
    # Clean text
    # -----------------------------------------------------

    cleaned_text = clean_text(
        email_text
    )

    # -----------------------------------------------------
    # TF-IDF transformation
    # -----------------------------------------------------

    vectorized_text = vectorizer.transform(
        [cleaned_text]
    )

    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    prediction = model.predict(
        vectorized_text
    )[0]

    # -----------------------------------------------------
    # Linear SVM decision score
    # -----------------------------------------------------

    decision_score = model.decision_function(
        vectorized_text
    )[0]

    # Convert decision score into a probability-like
    # confidence value for the UI.
    spam_probability = 1 / (
        1 + math.exp(-decision_score)
    )

    # -----------------------------------------------------
    # Explain prediction
    # -----------------------------------------------------

    feature_names = (
        vectorizer
        .get_feature_names_out()
    )

    coefficients = model.coef_[0]

    feature_values = (
        vectorized_text
        .toarray()[0]
    )

    # Contribution of each feature
    contributions = (
        feature_values * coefficients
    )

    # -----------------------------------------------------
    # Features supporting SPAM
    # -----------------------------------------------------

    spam_indices = (
        contributions
        .argsort()[::-1]
    )

    spam_features = []

    for index in spam_indices:

        contribution = contributions[index]

        if contribution <= 0:
            break

        spam_features.append(
            (
                feature_names[index],
                float(contribution)
            )
        )

        if len(spam_features) >= 5:
            break

    # -----------------------------------------------------
    # Features supporting HAM
    # -----------------------------------------------------

    ham_indices = (
        contributions
        .argsort()
    )

    ham_features = []

    for index in ham_indices:

        contribution = contributions[index]

        if contribution >= 0:
            break

        ham_features.append(
            (
                feature_names[index],
                float(abs(contribution))
            )
        )

        if len(ham_features) >= 5:
            break

    return (
        prediction,
        cleaned_text,
        spam_probability,
        spam_features,
        ham_features
    )


# =========================================================
# MAIN APPLICATION
# =========================================================

def main():

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        '<div class="main-title">📧 Spam Sentinel</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-powered Email Spam Detection using NLP & Machine Learning'
        '</div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # LOAD MODEL
    # =====================================================

    model, vectorizer = load_artifacts()

    if model is None or vectorizer is None:

        st.error(
            "🚨 Trained model files were not found."
        )

        st.info(
            "Train the model first using:"
        )

        st.code(
            "python src\\train.py"
        )

        return

    # =====================================================
    # MODEL INFORMATION
    # =====================================================

    with st.expander(
        "🤖 Model Information"
    ):

        st.write(
            "**Algorithm:** Linear Support Vector Machine"
        )

        st.write(
            "**Feature Extraction:** TF-IDF"
        )

        st.write(
            "**N-grams:** Unigrams + Bigrams"
        )

        st.write(
            "**Training Dataset:** 4,273 unique emails"
        )

        st.write(
            "**Test Accuracy:** 98.60%"
        )

        st.write(
            "**Spam F1 Score:** 98.00%"
        )

    # =====================================================
    # EMAIL INPUT
    # =====================================================

    st.subheader(
        "✉️ Analyze an Email"
    )

    email_text = st.text_area(
        "Email Content",
        height=260,
        placeholder=(
            "Paste an email here...\n\n"
            "Example:\n"
            "Congratulations! You have won a FREE prize. "
            "Click here to claim your reward."
        ),
        label_visibility="collapsed"
    )

    # =====================================================
    # BUTTONS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        analyze_clicked = st.button(
            "🔍 Analyze Email",
            type="primary",
            use_container_width=True
        )

    with col2:

        clear_clicked = st.button(
            "🗑️ Clear",
            use_container_width=True
        )

    if clear_clicked:

        st.rerun()

    # =====================================================
    # ANALYSIS
    # =====================================================

    if analyze_clicked:

        if not email_text.strip():

            st.warning(
                "⚠️ Please paste an email before analyzing."
            )

            return

        # -------------------------------------------------
        # Run prediction
        # -------------------------------------------------

        with st.spinner(
            "🔎 Analyzing email..."
        ):

            (
                prediction,
                cleaned_text,
                spam_probability,
                spam_features,
                ham_features
            ) = predict_email(
                email_text,
                model,
                vectorizer
            )

        # =================================================
        # RESULT
        # =================================================

        st.divider()

        if prediction == "spam":

            st.error(
                "🚨 SPAM DETECTED"
            )

            confidence = spam_probability

        else:

            st.success(
                "✅ LEGITIMATE EMAIL"
            )

            confidence = (
                1 - spam_probability
            )

        # =================================================
        # CONFIDENCE
        # =================================================

        st.metric(
            "Prediction Confidence",
            f"{confidence * 100:.1f}%"
        )

        st.progress(
            min(
                max(
                    confidence,
                    0.0
                ),
                1.0
            )
        )

        # =================================================
        # SCORES
        # =================================================

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "🚨 Spam Score",
                f"{spam_probability * 100:.1f}%"
            )

        with col2:

            st.metric(
                "✅ Legitimate Score",
                f"{(1 - spam_probability) * 100:.1f}%"
            )

        # =================================================
        # EXPLAINABILITY
        # =================================================

        st.divider()

        st.subheader(
            "🔍 Why did the model decide this?"
        )

        if prediction == "spam":

            st.write(
                "These words or phrases contributed "
                "most strongly toward the spam prediction:"
            )

            if spam_features:

                for word, score in spam_features:

                    st.markdown(
                        f"🔴 **{word}**"
                    )

            else:

                st.info(
                    "No strong individual spam signals "
                    "were detected."
                )

        else:

            st.write(
                "These words or phrases contributed "
                "most strongly toward the legitimate prediction:"
            )

            if ham_features:

                for word, score in ham_features:

                    st.markdown(
                        f"🟢 **{word}**"
                    )

            else:

                st.info(
                    "No strong individual legitimate signals "
                    "were detected."
                )

        # =================================================
        # PROCESSED TEXT
        # =================================================

        with st.expander(
            "🔬 View processed text"
        ):

            st.caption(
                "This is the cleaned text passed to "
                "the TF-IDF vectorizer."
            )

            st.code(
                cleaned_text
                if cleaned_text
                else "(empty after preprocessing)"
            )

    # =====================================================
    # FOOTER
    # =====================================================

    st.divider()

    st.caption(
        "Built with Python • Pandas • NLTK • "
        "scikit-learn • TF-IDF • Linear SVM • Streamlit"
    )


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":

    main()