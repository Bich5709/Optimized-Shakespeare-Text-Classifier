# Unique Words Part 1: Optimize the Classifier

## Overview

This project involves developing and optimizing a simple text classification algorithm to determine whether a given text fragment was written by William Shakespeare. The classifier works by measuring how many **unique words** from a predefined list of Shakespearean vocabulary appear in a given text fragment.

The project emphasizes **performance optimization**, specifically improving the runtime of the classification algorithm by reducing its time complexity from **O(N²)** to **O(N)**.

---

## Problem Statement

Given a list of words typically used by Shakespeare and a collection of text fragments, the goal is to:

- Calculate a **Shakespeare score** for each fragment.
- Classify each fragment as **Shakespearean** or **not**, based on a threshold.
- Optimize the algorithm's performance using efficient data structures (e.g., sets).

---

## Shakespeare Score

The Shakespeare score is calculated as:

```
Shakespeare Score = 
    (Number of unique Shakespearean words in the text)
    /
    (Number of unique words in the text)
```

Example:

For a fragment with 4 unique Shakespearean words and 29 total unique words:

```
Score = 4 / 29 ≈ 0.139
```

A threshold (e.g., 0.05) is used to classify the text:
- If score ≥ threshold → predicted as **Shakespeare**
- Otherwise → predicted as **Not Shakespeare**

---

## Files Provided

- `shakespeare-words.txt`: List of Shakespearean words.
- `test-set/`: Directory containing text fragments.
- `unique-word-classifier.py`: The main classification script.

---

## How to Run

Ensure you have Python 3 installed. Then, run the script:

```bash
python unique-word-classifier.py
```

Example Output:

```
The text test-set/shakespeare.0350.txt is written by Shakespeare
With a threshold of 0.0 we predict that Shakespeare is the author.
With a threshold of 0.05 we predict that Shakespeare is the author.
With a threshold of 0.1 we predict that Shakespeare is not the author.
With a threshold of 0.15 we predict that Shakespeare is not the author.
```

---

## Code Overview

### Main Functions

- **`main()`**: Entry point; loads data, calculates scores, and outputs predictions.
- **`load_shakespeare_words(filename)`**: Loads the Shakespearean word list.
- **`get_text_file_names(path)`**: Returns `.txt` files from a directory.
- **`calculate_shakespeare_score(text, shakespeare_words)`**: Computes the Shakespeare score *(to be optimized)*.
- **`is_written_by_shakespeare(file_name)`**: Returns True if the filename indicates Shakespearean origin.
- **`tokenize_text(text)`**: Cleans and splits text into unique lowercase words.

---

## Task: Optimization

### Current Bottleneck

The function `calculate_shakespeare_score()` currently uses nested loops and list membership checks, which makes it **O(N²)** in time complexity.

### Optimization Goal

- Use `set` operations instead of loops to compare unique words.
- Achieve **O(N)** time complexity.

### Hint

Convert both the Shakespearean word list and the text’s unique words into sets. Then compute the intersection:

```python
shakespeare_words_set = set(shakespeare_words)
text_words_set = set(tokenize_text(text))
overlap = shakespeare_words_set & text_words_set
score = len(overlap) / len(text_words_set)
```

---

## Performance Testing

To measure runtime performance, use the `timeit` library:

```python
import timeit

time = timeit.timeit("calculate_shakespeare_score(text, shakespeare_words)",
    setup="""
from __main__ import load_shakespeare_words, calculate_shakespeare_score
shakespeare_words = load_shakespeare_words("shakespeare-words.txt")
with open('./test-set/shakespeare.0350.txt', 'r', encoding='UTF-8') as file:
    text = file.read()
""", number=1000)

print(time)
```

- Expected runtime **before optimization**: ~2 seconds
- Expected runtime **after optimization**: ~0.03 seconds

---

## Testing

Run the following to check your implementation:

```bash
checkpy unique-word-classifier
```

Only the **first two tests** should pass for this part of the assignment. Later tests apply to future parts.

---

## Summary

In this project you:

- Implemented a simple classifier based on unique word overlap.
- Measured and optimized the runtime of a key function.
- Used set operations to drastically improve performance.

---


