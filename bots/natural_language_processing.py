import os
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def stop_words_demo():
    worf_quote = "Sir, I protest. I am not a merry man!"

    words_in_quote = word_tokenize(worf_quote)
    print(f"\nwords in worf quote:\n{words_in_quote}")
    """
    Example:
    ['Sir', ',', 'I', 'protest', '.', 'I', 'am', 'not', 'a', 'merry', 'man', '!']
    """

    # Filter out stop words in the quote:
    # What are stop words? https://kavita-ganesan.com/what-are-stop-words/
    stop_words = set(stopwords.words("english"))
    filtered_list = []

    for word in words_in_quote:
        if word.casefold() not in stop_words:
            filtered_list.append(word)
    
    print(f"\nFiltered out stop words from Worf quote:\n{filtered_list}")



def tokenizer_demo():
    example_string = """
    Muad'Dib learned rapidly because his first training was in how to learn. 
    And the first lesson of all was the basic trust that he could learn.
    It's shocking to find how many people do not believe they can learn,
    and how many more believe learning to be difficult.
    """

    print("\ntokenized sentences:")
    sentences = sent_tokenize(example_string)
    print(sentences)
    """
    Example:
    [
        "\nMuad'Dib learned rapidly because his first training was in how to learn.", 
        'And the first lesson of all was the basic trust that he could learn.', 
        "It's shocking to find how many people do not believe they can learn,\n    and how many more believe learning to be difficult."
    ]
    """

    print("\ntokenized words:")
    words = word_tokenize(example_string)
    print(words)
    """
    Example:
    [
        "Muad'Dib", 
        'learned', 
        'rapidly', 
        'because', 
        'his', 
        'first', 
        'training', 
        'was', 
        'in', 
        'how', 
        'to', 
        'learn', 
        '.', 
        'And', 
        'the', 
        'first', 
        'lesson', 
        'of', 
        'all', 
        'was', 
        'the', 
        'basic', 
        'trust', 
        'that', 
        'he', 
        'could', 
        'learn', 
        '.', 
        'It', 
        "'s", 
        'shocking', 
        'to', 
        'find', 
        'how', 
        'many', 
        'people', 
        'do', 
        'not', 
        'believe', 
        'they', 
        'can', 
        'learn', 
        ',', 
        'and', 
        'how', 
        'many', 
        'more', 
        'believe', 
        'learning', 
        'to', 
        'be', 
        'difficult', 
        '.'
    ]
    """


def download_nltk_data():
    download_directory = os.path.abspath("./nltk_data/")

    nltk.download("punkt", download_dir=download_directory)
    nltk.download("stopwords", download_dir=download_directory)


def main():
    download_nltk_data()
    tokenizer_demo()
    stop_words_demo()

if __name__ == "__main__":
    main()
