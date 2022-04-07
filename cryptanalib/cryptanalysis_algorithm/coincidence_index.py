import nltk
from cryptanalib.encoding.alphabet import Alphabet
import statistics


class CoincidenceIndex:
    def __init__(self, alphabet = Alphabet().printable):
        self.coincidence_index = None
        self.alphabet = alphabet

    def set_coincidence_index_from_nltk_corpus(self, corpus_names):
        """
        Download one or more corpus from nltk database to set average of index of coincidence for each corpus downloaded.


        :param corpus_names: list of string
        :return: None

        >>> fa = CoincidenceIndex()
        >>> fa.set_coincidence_index_from_nltk_corpus(['gutenberg', 'brown'])
        loading file austen-emma.txt from corpus gutenberg
        loading file austen-persuasion.txt from corpus gutenberg
        loading file austen-sense.txt from corpus gutenberg
        loading file bible-kjv.txt from corpus gutenberg
        loading file blake-poems.txt from corpus gutenberg
        loading file bryant-stories.txt from corpus gutenberg
        loading file burgess-busterbrown.txt from corpus gutenberg
        loading file carroll-alice.txt from corpus gutenberg
        loading file chesterton-ball.txt from corpus gutenberg
        loading file chesterton-brown.txt from corpus gutenberg
        loading file chesterton-thursday.txt from corpus gutenberg
        loading file edgeworth-parents.txt from corpus gutenberg
        loading file melville-moby_dick.txt from corpus gutenberg
        loading file milton-paradise.txt from corpus gutenberg
        loading file shakespeare-caesar.txt from corpus gutenberg
        loading file shakespeare-hamlet.txt from corpus gutenberg
        loading file shakespeare-macbeth.txt from corpus gutenberg
        loading file whitman-leaves.txt from corpus gutenberg
        loading file cats.txt from corpus brown

        >>> fa.coincidence_index
        0.053484400675862256
        """

        for corpus in corpus_names:
            nltk.download(corpus)
            file = nltk.data.find("corpora/" + corpus)
            new_corpus = nltk.corpus.PlaintextCorpusReader(file, r'.*\.txt',
                                                           encoding="latin-1")
            for fileid in new_corpus.fileids():
                print("loading file " + fileid + " from corpus " + corpus)
                target_code = new_corpus.raw(fileids=fileid)
                target_size = len(target_code)

                results = []
                for character in self.alphabet:
                    if character in target_code:
                        apparitions = target_code.count(character)
                        sum_characters = (apparitions * (apparitions - 1))
                        divide_characters = target_size * (target_size - 1)
                        result = sum_characters / divide_characters
                        results.append(result)

        self.coincidence_index = sum(results)


    def measure_coincidence_index_from_target(self, target_code, custom_alphabet=False):
        r"""
        Return frequency of caracters supplied in the target monoalphabetic caracter cipher code in argument.


        :param target_code: list of caracters
        :return: dictionary with caracters (keys) and float (values)

        >>> fa = CoincidenceIndex()
        >>> fa.measure_coincidence_index_from_target(['h', 'e', 'l', 'l', 'o'])
        0.1
        """

        if custom_alphabet == False:
            target_size = len(target_code)

            results = []
            for character in self.alphabet:
                if character in target_code:
                    apparitions = target_code.count(character)
                    sum_characters = (apparitions * (apparitions - 1))
                    divide_characters = target_size * (target_size - 1)
                    result = sum_characters / divide_characters
                    results.append(result)
        else:
            raise("Alphabet not implemented yet.")

        index_of_coincidence = sum(results)
        return index_of_coincidence