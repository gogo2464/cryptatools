from cryptanalib.encoding.format import Format
from cryptanalib.encoding.alphabet import Alphabet

class CaesarNumberEncryption:
    def __init__(self, alphabet):
        """
        Class to encrypt with caesar shifting algorithm.

        :param alphabet: list of int
        """
        self.format = Format()
        self.alphabet_size = len(alphabet)

    def encrypt(self, plain_text, key):
        """
        Encrypt the plain text and shift with key range.

        :param plain_text: list of int
        :return: a list of int (hex values).

        >>> from cryptanalib.encryption.caesar_number_encryption import CaesarNumberEncryption
        >>> from cryptanalib.encoding.alphabet import Alphabet
        >>> c = CaesarNumberEncryption(Alphabet().ascii_albhabet)
        >>> "".join([chr(cipher_text_list) for cipher_text_list in c.encrypt([0x41, 0x41, 0x41], 1)])
        'BBB'
        >>> c = CaesarNumberEncryption(Alphabet().ascii_albhabet)
        >>> "".join([chr(cipher_text_list) for cipher_text_list in c.encrypt([0x41, 0x41, 0x41], 10)])
        'KKK'
        >>> c = CaesarNumberEncryption(Alphabet().ascii_albhabet)
        >>> "".join([chr(cipher_text_list) for cipher_text_list in c.encrypt([0x53, 0x55, 0x50, 0x45, 0x52, 0x21], 10)])
        ']_ZO\\\+'
        >>> c = CaesarNumberEncryption(Alphabet().ascii_albhabet)#SUPER - 2 = QSNCP = 51 53 4E 43 50
        >>> "".join([chr(cipher_text_list) for cipher_text_list in c.encrypt([0x51, 0x53, 0x4E, 0x43, 0x50], 2)])
        'SUPER'
        """
        result = []

        for i in range(len(plain_text)):
            char = plain_text[i]
            char = (char + key) % self.alphabet_size
            result.append(char)
        return result

    def reverse_encrypt(self, plain_text, key):
        result = []

        for i in range(len(plain_text)):
            char = plain_text[i]
            char = (char - key) % self.alphabet_size
            result.append(char)
        return result