import nltk
nltk.download('words')
import string
from pathlib import Path


class PlainTextDetector:
    def __init__(self, language="english"):
        self.language = language
        nltk.download('words')

    def detect_plain_text(self, plain_or_cipher_text, similarity_level=0.25):
        """
        Check if the parameter plain_or_cipher_text is plain text and return True if the code is plain text. Return False if the text is still encrypted. The text will be considered as plain by default if more than 25% or the words are presents in a dictionnary of the language selected by the parameter language. In order to change the default level value, change the parameter similarity_level

        :param plain_or_cipher_text: list of string
        :param similarity_level: float
        :return:

        >>> import nltk
        >>> nltk.download("words")
        True
        >>> from cryptanalib.cryptanalysis_algorithm.brute_forcing import plain_text_detector
        >>> ptd = PlainTextDetector("any")
        >>> ptd.detect_plain_text(['H', 'e', 'l', 'l', 'o', '.', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', ' ', '?', ' ', 'I', ' ', 'a', 'm', ' ', 'f', 'i', 'n', 'e', ' ', 'a', 'n', 'd', ' ', 'y', 'o', 'u', ' ', '?'])
        1.0 level of similarity with the common words: ['Hello', '.', 'How', 'are', 'you', '?', 'I', 'am', 'fine', 'and', 'you', '?'].
        True
        """
        words_list = nltk.word_tokenize("".join(plain_or_cipher_text))

        if self.language == "english" or self.language == "any":
            try:
                nltk.download("words")
                file = nltk.data.find(str(Path("corpora") / "words"))
                new_corpus = nltk.corpus.PlaintextCorpusReader(file, r'en', encoding="latin-1")#.*\.txt
                common_words = [word for word in words_list if word.lower() in new_corpus.words() or word in string.punctuation]
                print("{0} level of similarity with the common words: {1}.".format(len(common_words) / len(words_list), common_words))
                if len(common_words) / len(words_list) > similarity_level:
                    return True
                else:
                    return False
            except ZeroDivisionError:
                return False
        else:
            raise("Language {0} not supported yet.")