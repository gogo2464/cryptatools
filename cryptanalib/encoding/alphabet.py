import string

class Alphabet:
    def __init__(self):
        self.printable = string.printable
        self.ascii_albhabet = [chr(i) for i in range(129)]
        self.uu_encoding_albhabet = [character for character in " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"]

