"""
generate_dataset.py
--------------------
Generates a synthetic (but realistic-looking) labeled dataset of spam and
legitimate ("ham") emails and saves it as data/spam.csv.

Why synthetic data?
- Keeps the repo self-contained (no external downloads required).
- Lets anyone clone the repo and immediately run train.py without hunting
  for a dataset file.
- You can freely swap this out for a real-world dataset later, e.g. the
  classic "SMS Spam Collection" or "Enron Spam" datasets — just make sure
  the resulting CSV has two columns: `label` (spam/ham) and `text`.

Run:
    python data/generate_dataset.py
"""

import csv
import random

random.seed(42)

# --------------------------------------------------------------------------
# Building blocks used to assemble varied spam / ham messages
# --------------------------------------------------------------------------

SPAM_OPENERS = [
    "Congratulations!", "URGENT NOTICE:", "Dear Winner,", "Act Now!",
    "Final Reminder:", "Hello Valued Customer,", "ATTENTION:",
    "Limited Time Offer!", "You have been selected.", "Breaking News:",
]

SPAM_BODIES = [
    "You have WON a ${amount} prize in our lottery! Click the link below to claim your reward now.",
    "Your account will be suspended unless you verify your details immediately at this link.",
    "Get RICH quick! Work from home and earn ${amount} per week with zero effort.",
    "FREE gift card worth ${amount} is waiting for you. Claim before it expires!",
    "Lowest prices ever on prescription meds, no prescription needed. Order today!",
    "Hot singles in your area want to meet you tonight! Click here.",
    "You've been pre-approved for a loan of ${amount}. No credit check required!",
    "Increase your followers instantly! Buy 10,000 followers for just $9.99.",
    "This is not a scam. Wire ${amount} today and double your investment in 24 hours!",
    "Your PayPal account has unusual activity. Login now to avoid permanent suspension.",
    "Exclusive deal just for you: 90% off luxury watches, today only!",
    "Make money fast with this one weird trick banks don't want you to know.",
    "Claim your free vacation to the Bahamas now! Limited slots available.",
    "Your package could not be delivered. Pay a ${amount} fee to reschedule delivery.",
    "Unlock a secret bonus of ${amount} by clicking this link right now!",
]

SPAM_CLOSERS = [
    "Click here: http://bit.ly/free-money-now",
    "Reply YES to claim your reward immediately.",
    "Visit www.claim-your-prize-now.com within 24 hours.",
    "Call this toll-free number now: 1-800-555-0199.",
    "Offer expires soon, act fast!",
    "Do not miss this once in a lifetime opportunity!",
]

HAM_OPENERS = [
    "Hi Team,", "Hey,", "Hello,", "Good morning,", "Hi there,",
    "Dear Sir/Madam,", "Hi Mom,", "Hey everyone,", "Hi John,", "Hello Sarah,",
]

HAM_BODIES = [
    "just wanted to confirm our meeting scheduled for {day} at {time}.",
    "attached is the report you asked for last week. Let me know if you need any changes.",
    "can you send me the updated project timeline before end of day?",
    "thanks for your help with the presentation yesterday, it went really well.",
    "I'll be working from home tomorrow, will join the standup call online.",
    "here are my notes from the client call. Please review before our next sync.",
    "reminder that the invoice for last month is due on {day}.",
    "let's grab lunch sometime next week, I'm free on {day}.",
    "the quarterly numbers look good, great work by the whole team.",
    "could you review the pull request I sent over? Would appreciate your feedback.",
    "happy birthday! Hope you have a wonderful day.",
    "just checking in to see how the migration project is progressing.",
    "attaching the syllabus for next semester's course, let me know if you have questions.",
    "the flight tickets are booked for {day}, I'll send the itinerary shortly.",
    "thanks for dinner last night, we should do that again soon.",
]

HAM_CLOSERS = [
    "Best regards,\nAlex", "Thanks,\nPriya", "Talk soon,\nSam",
    "Cheers,\nJordan", "Best,\nMorgan", "Regards,\nTaylor",
]

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
TIMES = ["9:00 AM", "10:30 AM", "2:00 PM", "3:15 PM", "4:45 PM"]
AMOUNTS = ["500", "1,000", "5,000", "10,000", "25,000", "250"]


def make_spam():
    opener = random.choice(SPAM_OPENERS)
    body = random.choice(SPAM_BODIES).format(amount=random.choice(AMOUNTS))
    closer = random.choice(SPAM_CLOSERS)
    return f"{opener} {body} {closer}"


def make_ham():
    opener = random.choice(HAM_OPENERS)
    body = random.choice(HAM_BODIES).format(
        day=random.choice(DAYS), time=random.choice(TIMES)
    )
    closer = random.choice(HAM_CLOSERS)
    return f"{opener} {body}\n\n{closer}"


def generate_rows(n_spam=250, n_ham=250):
    rows = []
    for _ in range(n_spam):
        rows.append(("spam", make_spam()))
    for _ in range(n_ham):
        rows.append(("ham", make_ham()))
    random.shuffle(rows)
    return rows


def main():
    rows = generate_rows()
    out_path = "data/spam.csv"
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["label", "text"])
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {out_path}")


if __name__ == "__main__":
    main()
