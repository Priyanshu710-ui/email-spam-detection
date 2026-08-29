import os
import re
import csv
from email import policy
from email.parser import BytesParser


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "spam.csv")


# ---------------------------------------------------------
# Text Cleaning
# ---------------------------------------------------------

def clean_email_text(text):
    """
    Perform basic cleaning on extracted email text.
    """

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Replace URLs with a common token
    text = re.sub(r"http\S+|www\S+", " URL ", text)

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ---------------------------------------------------------
# Email Extraction
# ---------------------------------------------------------

def extract_email_text(file_path):
    """
    Extract readable text from an email file.
    """

    try:
        with open(file_path, "rb") as f:
            message = BytesParser(
                policy=policy.default
            ).parse(f)

        text_parts = []

        # Handle multipart emails
        if message.is_multipart():

            for part in message.walk():

                content_type = part.get_content_type()

                # We mainly want plain-text content
                if content_type == "text/plain":

                    try:
                        content = part.get_content()

                        if isinstance(content, str):
                            text_parts.append(content)

                    except Exception:
                        pass

        # Handle non-multipart emails
        else:

            try:
                content = message.get_content()

                if isinstance(content, str):
                    text_parts.append(content)

            except Exception:
                pass

        # Combine all extracted text
        text = " ".join(text_parts)

        # Clean extracted text
        return clean_email_text(text)

    except Exception as e:

        print(f"Could not read {file_path}: {e}")

        return ""


# ---------------------------------------------------------
# Label Detection
# ---------------------------------------------------------

def get_label(folder_name):
    """
    Determine whether a folder contains spam or ham emails.
    """

    folder_name = folder_name.lower()

    if "spam" in folder_name:
        return "spam"

    if "ham" in folder_name:
        return "ham"

    return None


# ---------------------------------------------------------
# Dataset Creation
# ---------------------------------------------------------

def build_dataset():

    rows = []

    print("=" * 60)
    print("EMAIL SPAM DATASET PREPARATION")
    print("=" * 60)

    # -----------------------------------------------------
    # Process every folder inside raw/
    # -----------------------------------------------------

    for folder_name in os.listdir(RAW_DIR):

        folder_path = os.path.join(
            RAW_DIR,
            folder_name
        )

        # Ignore files
        if not os.path.isdir(folder_path):
            continue

        # Determine label
        label = get_label(folder_name)

        # Ignore folders that aren't ham/spam
        if label is None:
            continue

        print(f"\nProcessing: {folder_name}")
        print(f"Label: {label}")

        # Walk through all files
        for root, _, files in os.walk(folder_path):

            for filename in files:

                file_path = os.path.join(
                    root,
                    filename
                )

                text = extract_email_text(file_path)

                # Only keep emails where text was successfully extracted
                if text:

                    rows.append(
                        {
                            "label": label,
                            "text": text
                        }
                    )

    # -----------------------------------------------------
    # Initial statistics
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("INITIAL DATASET")
    print("=" * 60)

    print(f"Total emails collected: {len(rows)}")

    # -----------------------------------------------------
    # Remove duplicate emails
    # -----------------------------------------------------

    print("\nRemoving duplicate emails...")

    unique_rows = {}

    for row in rows:

        text = row["text"].strip()

        # Use email text as the unique key
        if text not in unique_rows:

            unique_rows[text] = row

    rows = list(unique_rows.values())

    print(
        f"After removing duplicates: {len(rows)}"
    )

    # -----------------------------------------------------
    # Count classes
    # -----------------------------------------------------

    spam_count = sum(
        1
        for row in rows
        if row["label"] == "spam"
    )

    ham_count = sum(
        1
        for row in rows
        if row["label"] == "ham"
    )

    # -----------------------------------------------------
    # Final statistics
    # -----------------------------------------------------

    print("\n" + "=" * 60)
    print("FINAL DATASET")
    print("=" * 60)

    print(f"Total unique emails: {len(rows)}")
    print(f"Spam emails: {spam_count}")
    print(f"Ham emails: {ham_count}")

    if len(rows) > 0:

        spam_percentage = (
            spam_count / len(rows)
        ) * 100

        ham_percentage = (
            ham_count / len(rows)
        ) * 100

        print(
            f"Spam percentage: {spam_percentage:.2f}%"
        )

        print(
            f"Ham percentage: {ham_percentage:.2f}%"
        )

    # -----------------------------------------------------
    # Save dataset
    # -----------------------------------------------------

    print("\nSaving dataset...")

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=["label", "text"]
        )

        writer.writeheader()

        writer.writerows(rows)

    print("\n" + "=" * 60)
    print("SUCCESS")
    print("=" * 60)

    print(
        f"Dataset saved to:\n{OUTPUT_FILE}"
    )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    build_dataset()