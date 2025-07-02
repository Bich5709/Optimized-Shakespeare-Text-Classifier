"""
unique-words-classifier.py: The program takes an arbitrary file from the folder
`test-set` and predicts whether it is written by Shakespeare.

Author: ...
"""

from pathlib import Path
import matplotlib.pyplot as plt

SHAKESPEARE_WORDS_FILE = "shakespeare-words.txt"
TEST_SET_PATH = Path("test-set")

def main():
    # Get shakespeare words
    shakespeare_words = load_shakespeare_words(SHAKESPEARE_WORDS_FILE)

    # Get an arbitrary file from the dataset
    text_file_name = get_text_file_names(TEST_SET_PATH)[300]


    # Check if the file was written by shakespeare
    is_shakespeare = is_written_by_shakespeare(text_file_name)

    if is_shakespeare:
        print(f"The text {text_file_name} is written by Shakespeare")
    else:
        print(f"The text {text_file_name} is not written by Shakespeare")

    # Predict step 1, get scores
    with open(text_file_name, 'r', encoding='UTF-8') as file:
        score = calculate_shakespeare_score(file.read(), shakespeare_words)

    # Predict step 2, try multiple thresholds
    thresholds = [t/20 for t in list(range(0, 4))]
    for threshold in thresholds:
        if score >= threshold:
            print(f"With a threshold of {threshold} we predict that Shakespeare is the author.")
        else:
            print(f"With a threshold of {threshold} we predict that Shakespeare is not the author.")

    accuracies = compute_all_accuracies(thresholds, text_file_names, shakespeare_words)
    print(accuracies)


# Change this function in favor of efficiency
def load_shakespeare_words(filename):
    """
    Load the file containing words typicaly for Shakespearean language. Assumes
    that the input file does not contain any duplicate words.
    """
    words = []
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            words.append(line.rstrip('\n'))
    return words

def get_text_file_names(path, extension='txt'):
    """
    Get all paths of files with given (.txt) extension.
    """
    return list(Path(path).glob(f'*.{extension}'))


# Change this function in favor of efficiency.
# With N being the length of shakespeare_words:
# Complexity before changes: O(N^2)
# Complexity after changes: O(N)
def calculate_shakespeare_score(text, shakespeare_words):
    """
    Compute the score of a text fragment by checking the relative overlap of
    words in the text with the shakespeare word list.
    """
    word_list = tokenize_text(text)

    # get all unique words in text
    unique_words = set(word_list)
    shakespeare_words = set(shakespeare_words)

    return len(unique_words & shakespeare_words) / len(unique_words)

def is_written_by_shakespeare(file_name):
    """
    Checks for a given filename if it contains the text "shakespeare"
    """
    by_shakespeare = file_name.name.split('.')[0] == "shakespeare"
    return by_shakespeare

def tokenize_text(text):
    """
    Returns a list of words from string text.
    """
    words = []
    for word in text.split():
        clean = word.lower().strip(' ,;.:\'"[]()-_?!')
        if clean.isalpha():
            words.append(clean)
    return words

#step 1: Get all text files
text_file_names = get_text_file_names('test-set')


def calculate_accuracy(actual, predicted):
    correct = 0
    for a, p in zip(actual, predicted):
        if a == p:
            correct += 1
    accuracy = correct / len(predicted)
    return accuracy

#step 2
def compute_all_accuracies(thresholds, text_file_names, shakespeare_words):


    #Determine the actual authorship information for all text fragments
    actual = []
    for file in text_file_names:
        actual_author = is_written_by_shakespeare(file)
        actual.append(actual_author)

    #compute for each text fragment the Shakespeare score
    scores = []
    for file in text_file_names:
        with open(file, 'r', encoding='UTF-8') as f:
            text = f.read()
        score = calculate_shakespeare_score(text, shakespeare_words)
        scores.append(score)

    #Determine the actual authorship by thresold
    accuracies = []
    for threshold in thresholds:
        predicted = []
        for score in scores:
            if score >= threshold:
                predicted.append(True)
            else:
                predicted.append(False)

        accuracy = calculate_accuracy(actual, predicted)
        accuracies.append(accuracy)

    return accuracies

    #shakespeare_words = ["wassail", "halcyon", "cannoneer", "darnel", "beggarly", "dispraise"]

   plt.plot(thresholds, accuracies)
    plt.xlabel('Threshold')
    plt.ylabel('Accuracy')
    plt.title('Accuracy of Shakespeare classifier vs Threshold')
    plt.show()

if __name__ == "__main__":
    main()



# import timeit
# time = timeit.timeit("calculate_shakespeare_score(text, shakespeare_words)",
# setup =
# """from __main__ import load_shakespeare_words, calculate_shakespeare_score
# shakespeare_words = load_shakespeare_words("shakespeare-words.txt")
# with open('./test-set/shakespeare.0350.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()
# """, number=1000)
# print(time)
