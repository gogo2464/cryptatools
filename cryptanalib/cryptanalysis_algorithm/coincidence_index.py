import nltk
from cryptanalib.encoding.alphabet import Alphabet
import statistics
from os.path import exists
from pathlib import Path


class CoincidenceIndex:
    def __init__(self, alphabet = Alphabet().printable):
        self.coincidence_index = {
            1: 0.0639,
            2: 0.0511,
            3: 0.0468,
            4: 0.0446,
            5: 0.0438,
            6: 0.0426,
        }
        self.target_coincidence_index = None
        self.alphabet = alphabet

    def set_coincidence_index_from_nltk_corpus(self, corpus_names, categories=None):
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
        {0: 0.053484400675862256}

        >>> fa.set_coincidence_index_from_nltk_corpus(['gutenberg', 'brown', 'punkt'], categories=['news'])
        loading file ca01 from corpus brownon category news
        loading file ca02 from corpus brownon category news
        loading file ca03 from corpus brownon category news
        loading file ca04 from corpus brownon category news
        loading file ca05 from corpus brownon category news
        loading file ca06 from corpus brownon category news
        loading file ca07 from corpus brownon category news
        loading file ca08 from corpus brownon category news
        loading file ca09 from corpus brownon category news
        loading file ca10 from corpus brownon category news
        loading file ca11 from corpus brownon category news
        loading file ca12 from corpus brownon category news
        loading file ca13 from corpus brownon category news
        loading file ca14 from corpus brownon category news
        loading file ca15 from corpus brownon category news
        loading file ca16 from corpus brownon category news
        loading file ca17 from corpus brownon category news
        loading file ca18 from corpus brownon category news
        loading file ca19 from corpus brownon category news
        loading file ca20 from corpus brownon category news
        loading file ca21 from corpus brownon category news
        loading file ca22 from corpus brownon category news
        loading file ca23 from corpus brownon category news
        loading file ca24 from corpus brownon category news
        loading file ca25 from corpus brownon category news
        loading file ca26 from corpus brownon category news
        loading file ca27 from corpus brownon category news
        loading file ca28 from corpus brownon category news
        loading file ca29 from corpus brownon category news
        loading file ca30 from corpus brownon category news
        loading file ca31 from corpus brownon category news
        loading file ca32 from corpus brownon category news
        loading file ca33 from corpus brownon category news
        loading file ca34 from corpus brownon category news
        loading file ca35 from corpus brownon category news
        loading file ca36 from corpus brownon category news
        loading file ca37 from corpus brownon category news
        loading file ca38 from corpus brownon category news
        loading file ca39 from corpus brownon category news
        loading file ca40 from corpus brownon category news
        loading file ca41 from corpus brownon category news
        loading file ca42 from corpus brownon category news
        loading file ca43 from corpus brownon category news
        loading file ca44 from corpus brownon category news

        >>> fa.coincidence_index
        {0: 0.060591077352534786}
        """

        for corpus in corpus_names:
            nltk.download(corpus)
            if categories is None:
                try:
                    file = nltk.data.find(str(Path("corpora") / corpus))
                except:
                    pass
                try:
                    file = nltk.data.find(str(Path("tokenizers") / corpus))
                except:
                    pass
                new_corpus = nltk.corpus.PlaintextCorpusReader(file, r'.*\.txt', encoding="latin-1")
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

                self.coincidence_index = {0: sum(results)}

            else:
                try:
                    file = nltk.data.find(str(Path("corpora") / corpus))
                except:
                    pass
                try:
                    file = nltk.data.find(str(Path("tokenizers") / corpus))
                except:
                    pass

                new_corpus = nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader(file, r'.*\.*', cat_file='cats.txt'
                    , encoding="latin-1")

                if exists(str(Path(file) / "cats.txt")):
                    for category in new_corpus.categories():#for fileid in new_corpus.fileids(categories=categories):
                        if category in categories:
                            for fileid in new_corpus.fileids(category):
                                print("loading file " + fileid + " from corpus " + corpus + "on category " + category)
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

                    self.coincidence_index[0] = sum(results)
    def set_target_coincidence_index_from_target(self, target_code):
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
        >>> cipher_text = "two house holds both a like indignity in fair ver on a where wela your scene from ancient grudge break to new mutiny where civil blood makes civil hand sun clean from forth the fatalloins of these two foes a pair of star crossd lover stake the irl"
        >>> c = CoincidenceIndex(alphabet=string.ascii_lowercase + " ")
        >>> c.set_target_coincidence_index_from_target(cipher_text)
        >>> c.target_coincidence_index
        0.07455317468154439
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
        coincidence_index = min(self.coincidence_index.values(), key=difference)

        key_size = [k for k, v in self.coincidence_index.items() if v == coincidence_index][0]

        return key_size