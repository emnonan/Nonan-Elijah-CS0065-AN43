"""
Analyze 10 sentences using TextBlob.
"""

from textblob import TextBlob


def read_sentence(prompt):
    """Keep asking until the user enters a nonempty sentence."""
    while True:
        sentence = input(prompt).strip()
        if sentence:
            return sentence
        print("Please enter a sentence.")


def laboratory_activity():
    """Analyze exactly 10 sentences and summarize their sentiments."""
    print("TEXTBLOB SENTIMENT ANALYSIS")
    counts = {"Positive": 0, "Neutral": 0, "Negative": 0}

    for number in range(1, 11):
        sentence = read_sentence(f"\nEnter sentence {number}/10: ")
        s = TextBlob(sentence)
        p = s.sentiment.polarity

        if p < 0:
            sentiment = "Negative"
        elif p == 0:
            sentiment = "Neutral"
        else:
            sentiment = "Positive"

        counts[sentiment] += 1
        print(f"Sentiment: {sentiment}")
        print(f"Polarity: {p:.4f}")

    print("\nSUMMARY")
    for sentiment, count in counts.items():
        print(f"{sentiment} sentences: {count}")
    print(f"Total sentences: {sum(counts.values())}")


if __name__ == "__main__":
    laboratory_activity()