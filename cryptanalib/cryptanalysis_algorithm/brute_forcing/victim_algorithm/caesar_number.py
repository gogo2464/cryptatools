from cryptanalib.cryptanalysis_algorithm.brute_forcing.generic_brute_forcer import GenericBruteForcer
from cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector import PlainTextDetector
from cryptanalib.encoding.format import Format
from cryptanalib.encryption.caesar_number_encryption import CaesarNumberEncryption
from cryptanalib.encoding.alphabet import Alphabet

class CaesareNumberBruteForcer(GenericBruteForcer):
    def __init__(self, alphabet=Alphabet().ascii_albhabet, ignore_characters=None):
        """
        Class to handle brute forcing on the caesar algorithm.

        The default alphabet used by Caesar is the ascii (127 characters). This can be changed by the parameter alphabet to this class.


        :param alphabet: string
        """
        self.alphabet = alphabet
        self.ignore_characters=ignore_characters

    def brute_force(self, cipher_text, encoding="no_encoding", language="english", frequency_required=0.25, max_retries=None):
        r"""
        Brute force any possibility of alphabets shifting with the caesar encryption algorithm.

        First decode the format given with the variable format.
        Then if some natural language words correspond to a dictionary of language specified by the language in the variable language, return a list of hex values of the decoded palin text.

        :param cipher_text: list of int
        :param encoding: string
        :param language: string
        :return: array of hex values

        >>> from cryptanalib.cryptanalysis_algorithm.brute_forcing.victim_algorithm.caesar_number import CaesareNumberBruteForcer
        >>> from cryptanalib.encoding.alphabet import Alphabet
        >>> from cryptanalib.encoding.format import Format
        >>> cnbf = CaesareNumberBruteForcer(alphabet=Alphabet().ascii_albhabet)
        >>> cnbf.brute_force([ord(number) for number in list("A5&AI<R!I<R!A(&=R96%T(&1A>2!T;R!D:64@=&]D87DA")], encoding="uu_charset", language="english", frequency_required=0.25)
        1.0 level of similarity with the common words: ['This', 'is', 'a', 'great', 'day', 'to', 'die', 'today', '!'].
        Caesar number algorithm successfully brute forced with key 0
        'This is a great day to die today!'
        >>> cnbf = CaesareNumberBruteForcer(alphabet=Alphabet().ascii_albhabet)
        >>> cnbf.brute_force([ord(number) for number in list("<0!<D7M∟D7M∟<#!8M41 O#!,<9-∟O6M∟?51/;8!X?32?<")], encoding="uu_charset", language="english", frequency_required=0.75)
        0.42857142857142855 level of similarity with the common words: ['@', '$', '$', '`', 'M', "'"].
        0.6 level of similarity with the common words: [']', '&', 'nU', '#', ']', '`', 'Y', '$', '`'].
        0.5714285714285714 level of similarity with the common words: [']', ']', 'h', '>'].
        0.5 level of similarity with the common words: [']', '@'].
        0.46153846153846156 level of similarity with the common words: ['(', '(', 'T', '#', '#', ']'].
        1.0 level of similarity with the common words: ['This', 'is', 'a', 'great', 'day', 'to', 'die', 'today', '!'].
        Caesar number algorithm successfully brute forced with key 5
        'This is a great day to die today!'
        >>> c = CaesarNumberEncryption(Alphabet().ascii_albhabet)
        >>> f = Format()
        >>> f.decoding["uu_charset"]("".join([chr(cipher_text_list) for cipher_text_list in c.encrypt([ord(number) for number in list("<0!<D7M∟D7M∟<#!8M41 O#!,<9-∟O6M∟?51/;8!X?32?<")], 5)]))
        'This is a great day to die today!'
        >>> basic_alphabet = "abcdefghijklmnopqrstuvwxyz"
        >>> abc = "gdkkn gnv zqd xnt"
        >>> cnbf = CaesareNumberBruteForcer(basic_alphabet, ignore_characters=[" ", "\n"])
        >>> cipher_text = [basic_alphabet.index(cipher_text) % 26 if cipher_text != " " and cipher_text != "\n" else cipher_text for cipher_text in abc]
        >>> cnbf.brute_force(cipher_text, encoding="no_encoding", language="english", frequency_required=0.75)
        [6, 3, 10, 10, 13, ' ', 6, 13, 21, ' ', 25, 16, 3, ' ', 23, 13, 19]
        0.0 level of similarity with the common words: [].
        Sentence 0/26: not detected on 'gdkkn gnv zqd xnt'
        [6, 3, 10, 10, 13, ' ', 6, 13, 21, ' ', 25, 16, 3, ' ', 23, 13, 19]
        1.0 level of similarity with the common words: ['hello', 'how', 'are', 'you'].
        Caesar number algorithm successfully brute forced with key 1
        'hello how are you'
        >>> import string
        >>> abc = "gdkkn gnv zqd xnt"
        >>> ascii_alphabet = string.printable
        >>> cnbf = CaesareNumberBruteForcer(ascii_alphabet, ignore_characters=[" "])
        >>> cipher_text = [ascii_alphabet.index(cipher_text) if cipher_text != " " else cipher_text for cipher_text in abc]
        >>> cnbf.brute_force(cipher_text, encoding="no_encoding", language="english", frequency_required=0.75)
        [16, 13, 20, 20, 23, ' ', 16, 23, 31, ' ', 35, 26, 13, ' ', 33, 23, 29]
        0.0 level of similarity with the common words: [].
        Sentence 0/100: not detected on 'gdkkn gnv zqd xnt'
        [16, 13, 20, 20, 23, ' ', 16, 23, 31, ' ', 35, 26, 13, ' ', 33, 23, 29]
        1.0 level of similarity with the common words: ['hello', 'how', 'Are', 'you'].
        Caesar number algorithm successfully brute forced with key 1
        'hello how Are you'
        """
        ptd = PlainTextDetector(language=language)
        f = Format()
        caesar = CaesarNumberEncryption(self.alphabet)
        if max_retries == None:
            max_retries = len(self.alphabet)

        if encoding == "uu_charset":
            for i in range(max_retries):
                brute_forced_text = caesar.encrypt(cipher_text, i)
                potentially_decoded_brute_forced_text = f.decoding[encoding]("".join([chr(text) for text in brute_forced_text]))#todo: pass hex to uu next
                is_plain_text_found = ptd.detect_plain_text(potentially_decoded_brute_forced_text, frequency_required)

                if is_plain_text_found == True:
                    print("Caesar number algorithm successfully brute forced with key {0}".format(i))
                    return potentially_decoded_brute_forced_text
        elif encoding == "no_encoding":
            for i in range(len(self.alphabet)):
                if self.ignore_characters != None:
                    j = 0
                    brute_forced_text = []
                    brute_forced_chunk = []
                    print(cipher_text)
                    while j < len(cipher_text):
                        if cipher_text[j] not in self.ignore_characters:
                            brute_forced_chunk.append(cipher_text[j])
                            j += 1
                        else:
                            brute_forced_text += caesar.encrypt(brute_forced_chunk, i)
                            try:
                                brute_forced_text += cipher_text[j]
                            except:
                                pass
                            j += 1
                            brute_forced_chunk = []

                    brute_forced_text += caesar.encrypt(brute_forced_chunk, i)
                    potentially_decoded_brute_forced_text = "".join([self.alphabet[c] if c not in self.ignore_characters else c for c in brute_forced_text])

                else:
                    brute_forced_text = caesar.encrypt(cipher_text, i)
                    potentially_decoded_brute_forced_text = "".join(brute_forced_text)
                is_plain_text_found = ptd.detect_plain_text(potentially_decoded_brute_forced_text, frequency_required)

                if is_plain_text_found == True:
                    print("Caesar number algorithm successfully brute forced with key {0}".format(i))
                    return potentially_decoded_brute_forced_text
                else:
                    print("Sentence {0}/{1}: not detected on '{2}'".format(i, max_retries, potentially_decoded_brute_forced_text))

        else:
            raise ("encoding {0} need to be implemented!".format(encoding))

        raise ("Brute forcing failed.")