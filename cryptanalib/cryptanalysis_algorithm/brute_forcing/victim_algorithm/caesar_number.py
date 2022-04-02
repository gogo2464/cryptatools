from cryptanalib.cryptanalysis_algorithm.brute_forcing.generic_brute_forcer import GenericBruteForcer
from cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector import PlainTextDetector
from cryptanalib.encoding.format import Format
from cryptanalib.encryption.caesar_number_encryption import CaesarNumberEncryption
from cryptanalib.encoding.alphabet import Alphabet

import re

class CaesareNumberBruteForcer(GenericBruteForcer):
    def __init__(self, alphabet=Alphabet().ascii_albhabet, ignore_characters=None):
        """
        Class to handle brute forcing on the caesar algorithm.

        The default alphabet used by Caesar is the ascii (127 characters). This can be changed by the parameter alphabet to this class.


        :param alphabet: string
        """
        self.alphabet = alphabet
        self.ignore_characters=ignore_characters

    def brute_force(self, cipher_text, format="ascii_charset", language="english", frequency_required=0.25, max_retries=None):
        """
        Brute force any possibility of alphabets shifting with the caesar encryption algorithm.

        First decode the format given with the variable format.
        Then if some natural language words correspond to a dictionary of language specified by the language in the variable language, return a list of hex values of the decoded palin text.

        :param cipher_text: list of int
        :param format: string
        :param language: string
        :return: array of hex values

        >>> from cryptanalib.cryptanalysis_algorithm.brute_forcing.victim_algorithm.caesar_number import CaesareNumberBruteForcer
        >>> from cryptanalib.encoding.alphabet import Alphabet
        >>> cnbf = CaesareNumberBruteForcer(alphabet=Alphabet().ascii_albhabet)
        >>> cnbf.brute_force([ord(number) for number in list("A5&AI<R!I<R!A(&=R96%T(&1A>2!T;R!D:64@=&]D87DA")], format="uu_charset", language="english", frequency_required=0.25)
        1.0 level of similarity with the common words: ['This', 'is', 'a', 'great', 'day', 'to', 'die', 'today', '!'].
        Caesar number algorithm successfully brute forced with key 0
        'This is a great day to die today!'

        >>> cnbf = CaesareNumberBruteForcer(alphabet=Alphabet().ascii_albhabet)
        >>> cnbf.brute_force([ord(number) for number in list("<0!<D7M∟D7M∟<#!8M41 O#!,<9-∟O6M∟?51/;8!X?32?<")], format="uu_charset", language="english", frequency_required=0.75)
        0.42857142857142855 level of similarity with the common words: ['@', '$', '$', '`', 'M', "'"].
        0.6 level of similarity with the common words: [']', '&', 'nU', '#', ']', '`', 'Y', '$', '`'].
        0.5714285714285714 level of similarity with the common words: [']', ']', 'h', '>'].
        0.5 level of similarity with the common words: [']', '@'].
        0.46153846153846156 level of similarity with the common words: ['(', '(', 'T', '#', '#', ']'].
        1.0 level of similarity with the common words: ['This', 'is', 'a', 'great', 'day', 'to', 'die', 'today', '!'].
        Caesar number algorithm successfully brute forced with key 5
        'This is a great day to die today!'
        >>> from cryptanalib.encoding.format import Format
        >>> c = CaesarNumberEncryption(Alphabet().ascii_albhabet)
        >>> f = Format()
        >>> f.decoding["uu_charset"]("".join([chr(cipher_text_list) for cipher_text_list in c.encrypt([ord(number) for number in list("<0!<D7M∟D7M∟<#!8M41 O#!,<9-∟O6M∟?51/;8!X?32?<")], 5)]))
        'This is a great day to die today!'
        """
        ptd = PlainTextDetector(language=language)
        f = Format()
        caesar = CaesarNumberEncryption(self.alphabet)
        if max_retries == None:
            max_retries = len(self.alphabet)

        if format == "uu_charset":
            for i in range(max_retries):
                brute_forced_text = caesar.encrypt(cipher_text, i)
                potentially_decoded_brute_forced_text = f.decoding[format]("".join([chr(text) for text in brute_forced_text]))#todo: pass hex to uu next
                is_plain_text_found = ptd.detect_plain_text(potentially_decoded_brute_forced_text, frequency_required)

                if is_plain_text_found == True:
                    print("Caesar number algorithm successfully brute forced with key {0}".format(i))
                    return potentially_decoded_brute_forced_text
        elif format == "ascii_charset":
            for i in range(max_retries):
                delimiters = dict()
                for d in self.ignore_characters:
                    delimiters[d] = []
                if self.ignore_characters != None:
                    for c in range(len(cipher_text)):
                        for split in self.ignore_characters:
                            if split == chr(cipher_text[c]):
                                delimiters[split].append(c)

                    brute_forced_text = caesar.encrypt(cipher_text, i)
                    potentially_decoded_brute_forced_text = "".join([chr(text) for text in brute_forced_text])

                    for d in self.ignore_characters:
                        for l in delimiters[d]:
                            potentially_decoded_brute_forced_text = potentially_decoded_brute_forced_text[:l] + d + potentially_decoded_brute_forced_text[l+1:]
                else:
                    brute_forced_text = caesar.encrypt(cipher_text, i)
                    potentially_decoded_brute_forced_text = "".join([chr(text) for text in brute_forced_text])
                is_plain_text_found = ptd.detect_plain_text(potentially_decoded_brute_forced_text, frequency_required)

                if is_plain_text_found == True:
                    print("Caesar number algorithm successfully brute forced with key {0}".format(i))
                    return potentially_decoded_brute_forced_text
                else:
                    print("Sentence {0}/{1}: not detected on '{2}'".format(i, max_retries, potentially_decoded_brute_forced_text))

            print("Now in reverse mode:")
            for i in range(max_retries):
                brute_forced_text = caesar.reverse_encrypt(cipher_text, i)
                potentially_decoded_brute_forced_text = "".join([chr(text) for text in brute_forced_text])
                is_plain_text_found = ptd.detect_plain_text(potentially_decoded_brute_forced_text, frequency_required)

                if is_plain_text_found == True:
                    print("Caesar number algorithm successfully brute forced with key {0}".format(i))
                    return potentially_decoded_brute_forced_text
                else:
                    print("Sentence {0}/{1}: not detected on '{2}'".format(i, max_retries, potentially_decoded_brute_forced_text))

        else:
            raise ("need to be implemented!")

        raise ("Brute forcing failed.")