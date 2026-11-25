# Technical Assessment 5: Sentence Sentiment Analyzer

A Python activity that demonstrates sentiment analysis through two standalone console programs: TextBlob polarity classification and a dictionary-based happy–sad word counter.

## Learning objectives

- Understand how sentiment analysis classifies text.
- Use TextBlob to obtain a sentence's polarity.
- Apply conditions, loops, functions, and dictionaries to analyze and summarize results.
- Use public positive and negative word lists to determine a sentence's tone.

## Project files

| File                 | Purpose                                                                    |
| -------------------- | -------------------------------------------------------------------------- |
| `lab_activity_vi.py` | Part VI: analyze 10 sentences and summarize sentiment counts.              |
| `challenge_vii.py`   | Part VII: count happy and sad words in one sentence and classify its tone. |
| `README.md`          | Setup instructions, program descriptions, and usage examples.              |

Each Python file runs independently. Neither requires the earlier combined `laboratory_activity_2.py` file.

## Requirements and setup

- Python 3 and pip.
- TextBlob for Part VI.
- NLTK and its `opinion_lexicon` dataset for Part VII.
- An internet connection for the initial package and dataset downloads.

### Using PyCharm

1. Open your project in PyCharm and place both Python files in the project folder.
2. Select the project's Python interpreter in PyCharm's settings. A project virtual environment is recommended.
3. Open **View → Tool Windows → Terminal**.
4. With the project environment active, run:

   ```bash
   python -m pip install textblob nltk
   python -m nltk.downloader opinion_lexicon
   ```

5. Right-click the desired Python file and select **Run**.
6. Enter sentences in the **Run** panel when prompted.

Use the same Python environment for installation and execution. Once setup is complete, these programs do not need an internet connection for analysis.

## TextBlob sentiment analysis

Run `SentenceSentimentAnalyzer.py` in PyCharm or from the project terminal:

```bash
python SentenceSentimentAnalyzer.py
```

The program asks for 10 nonempty sentences. For each sentence, it creates a `TextBlob` object, reads `sentiment.polarity`, and prints the classification and polarity value.

| Polarity (`p`) | Sentiment |
| -------------- | --------- |
| `p < 0`        | Negative  |
| `p == 0`       | Neutral   |
| `p > 0`        | Positive  |

Polarity ranges from −1 to 1. After all 10 sentences, the program prints the number classified as positive, neutral, and negative, followed by the total.

Illustrative summary format (counts depend on the sentences entered):

```text
SUMMARY
Positive sentences: 4
Neutral sentences: 3
Negative sentences: 3
Total sentences: 10
```

## Happy and sad word counter

Run `SentenceSentimentAnalyzerChallenge.py` in PyCharm or from the project terminal:

```bash
python SentenceSentimentAnalyzerChallenge.py
```

The program asks for one nonempty sentence and compares its words against the positive and negative lists in the **Hu and Liu Opinion Lexicon**, distributed through NLTK. These serve as the activity's happy and sad word datasets.

| Function                 | Purpose                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------- |
| `read_sentence(prompt)`  | Request input until a nonempty sentence is entered.                                     |
| `words_in(sentence)`     | Convert text to lowercase and extract words, allowing internal hyphens and apostrophes. |
| `number_happy(sentence)` | Return the number of occurrences matching the positive word list.                       |
| `number_sad(sentence)`   | Return the number of occurrences matching the negative word list.                       |
| `challenge()`            | Collect input, compare counts, and display the analysis.                                |

Repeated words count each time they appear. Matching is case-insensitive and uses complete extracted words rather than substrings.

| Comparison                            | Analysis         |
| ------------------------------------- | ---------------- |
| Happy count > sad count               | Positive (happy) |
| Sad count > happy count               | Negative (sad)   |
| Counts are equal, including both zero | Neutral          |

Illustrative output format:

```text
Happy words: 2
Sad words: 1
Analysis: Positive (happy)
```

The two programs use different methods, so they may classify the same sentence differently.

## Limitations

These programs demonstrate basic sentiment analysis for English text. Predictions may be inaccurate for sarcasm, slang, ambiguous wording, or mixed emotions. The challenge uses word counts only: it does not interpret negation or context, so a phrase such as “not happy” still contains a happy word. It also does not perform stemming or lemmatization; a word form must appear in the dataset to match.

## Troubleshooting

| Problem                                        | Solution                                                                                    |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `ModuleNotFoundError` for `textblob` or `nltk` | Install the packages using the same interpreter selected for the PyCharm run configuration. |
| `LookupError` mentioning `opinion_lexicon`     | Run `python -m nltk.downloader opinion_lexicon` in the active project environment.          |
| `python` is not recognized                     | Check your Python installation and PyCharm interpreter configuration.                       |
| Program appears to wait without continuing     | Click the Run panel, type a sentence, and press Enter.                                      |

## References

- Course handout: _Laboratory Activity - Sentiment Analysis_, CS054 Intelligent Systems.
- [TextBlob documentation](https://textblob.readthedocs.io/en/dev/)
- [NLTK Opinion Lexicon documentation](https://www.nltk.org/api/nltk.corpus.reader.opinion_lexicon.html)
