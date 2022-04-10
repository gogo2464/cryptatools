import nltk
from cryptanalib.encoding.alphabet import Alphabet
import statistics


class CoincidenceIndex:
    def __init__(self, alphabet = Alphabet().printable):
        self.coincidence_index = {
            0.0639: 1,
            0.0511: 2,
            0.0468: 3,
            0.0446: 4,
            0.0438: 5,
            0.0426: 6
        }
        self.target_coincidence_index = None
        self.alphabet = alphabet

    def set_coincidence_index_from_nltk_corpus(self, corpus_names):
        r"""
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
        {0.0639: 1, 0.0511: 2, 0.0468: 3, 0.0446: 4, 0.0438: 5, 0.0426: 6, 1: 0.053484400675862256}
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

        self.coincidence_index[1] = sum(results)


    def set_target_coincidence_index_from_target(self, target_code, custom_alphabet=False):
        r"""
        Return frequency of caracters supplied in the target monoalphabetic caracter cipher code in argument.


        :param target_code: list of caracters
        :return: dictionary with caracters (keys) and float (values)

        >>> fa = CoincidenceIndex()
        >>> fa.set_target_coincidence_index_from_target(['h', 'e', 'l', 'l', 'o'])
        Warning: the cipher text is only 5 characters. This may be too short to rely entierely on coincidence index.
        >>> fa.target_coincidence_index
        0.1
        """

        if len(target_code) < 100:
            print("Warning: the cipher text is only {0} characters. This may be too short to rely entierely on coincidence index.".format(len(target_code)))

        target_size = len(target_code)

        results = []
        for character in self.alphabet:
            apparitions = target_code.count(character)
            sum_characters = (apparitions * (apparitions - 1))
            divide_characters = target_size * (target_size - 1)
            result = sum_characters / divide_characters
            results.append(result)

        index_of_coincidence = sum(results)
        self.target_coincidence_index = index_of_coincidence

    def guess_key_size(self):
        r"""
        Return the target corpus key size.

        :return: int

        >>> fa = CoincidenceIndex()
        >>> fa.set_target_coincidence_index_from_target(['h', 'e', 'l', 'l', 'o'])
        Warning: the cipher text is only 5 characters. This may be too short to rely entierely on coincidence index.
        >>> fa.guess_key_size()
        1

        >>> import string
        >>> cipher_text = "twohouseholdsbothalikeindignityinfairveronawherewelayourscenefromancientgrudgebreaktonewmutinywherecivilbloodmakescivilhandsuncleanfromforththefatalloinsofthesetwofoesapairofstarcrossdloverstaketheirl"
        >>> c = CoincidenceIndex(alphabet=string.ascii_lowercase)
        >>> c.set_target_coincidence_index_from_target(cipher_text)
        >>> c.target_coincidence_index
        0.059497487437185935
        >>> c.guess_key_size()
        1

        >>> cipher_text = "kkalclgqlccrefckvmpwbsurrzuzmhpwzjozfhiffbmavvfqascoksiigoibvtdsarbomsehsviuuqffvowxcesiqikwzckysdiqzjuppccaharyqwqzjupvrbpwieqxioetdsawcdxvkvqjokoxpczbestkvqwskkajcvgmtozfajgkodgffgehzfjqvgkowihysuvz"
        >>> c = CoincidenceIndex(alphabet=string.ascii_lowercase)
        >>> c.set_target_coincidence_index_from_target(cipher_text)
        >>> c.target_coincidence_index
        0.04135678391959799
        >>> c.guess_key_size()
        6
        """

        difference = lambda input_list: abs(input_list - self.target_coincidence_index)
        coincidence_index = min(self.coincidence_index.keys(), key=difference)

        return self.coincidence_index[coincidence_index]