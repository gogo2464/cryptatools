import string

class Format:
    r"""
    Instanciate this class to handle or process a specific format.
    """
    def __init__(self):
        self.encoding = dict(
            ascii_charset={number: hex(ord(number)) for number in string.printable},
            uu_charset=lambda a: self.encode_uu_charset(a)
        )
        r"""
        Encode text to specific encoding. 

        :param ascii_charset: encode single char to ascii hexadecimal
        :param uu_charset: encode text to uu encoding
        """

        self.decoding = dict(
            ascii_charset={hex(ord(number)): number for number in string.printable},
            uu_charset=lambda a: self.decode_uu_charset(a)
        )
        r"""
        Decode text to specific encoding. 

        :param ascii_charset: decode single hexadecimal char
        :param uu_charset: decode uu encoded text to plain text
        """

    def encode_uu_charset(self, cipher_text):
        """
        Encode the cipher text string to a plain text ascii string.

        :param cipher_text: String
        :return: string

        >>> from cryptanalib.encoding.format import Format
        >>> format = Format()
        >>> format.encoding["ascii_charset"]["A"]
        '0x41'
        >>> format.encoding["uu_charset"]("ABCDAZERTY") == format.encode_uu_charset("ABCDAZERTY")
        True
        """
        size_code = chr(len(cipher_text) + 32)

        plain_text = ""
        plain_text += size_code

        six_bits_flow = []
        for c in list(zip(*[iter(cipher_text)] * 3)):
            c = "".join(c)
            six_bits_flow.append(bin(self.get_bits(ord(c[0:0+1]), 0, 6, 8))[2:].zfill(6))
            six_bits_flow.append((str(bin(self.get_bits(ord(c[0:0+1]), 6, 8, 8))[2:].zfill(2)) + str(bin(self.get_bits(ord(c[1:1+1]), 0, 4, 8))[2:].zfill(4))).zfill(6))
            six_bits_flow.append((str(bin(self.get_bits(ord(c[1:1+1]), 4, 8, 8))[2:].zfill(4)) + str(bin(self.get_bits(ord(c[2:2+1]), 0, 2, 8))[2:].zfill(2))).zfill(6))
            six_bits_flow.append(str(bin(self.get_bits(ord(c[2:2+1]), 2, 8, 8))[2:].zfill(4)).zfill(6))

        if len(cipher_text) % 3 == 1:
            six_bits_flow.append(bin(self.get_bits(ord(cipher_text[-1]), 0, 6, 8))[2:].zfill(6))
            six_bits_flow.append(bin(self.get_bits(ord(cipher_text[-1]), 6, 8, 8))[2:].zfill(2) + "0000")
            six_bits_flow.append(str(bin(self.get_bits(int("0", 2), 6, 8, 8))[2:].zfill(6)))
            six_bits_flow.append(str(bin(self.get_bits(int("0", 2), 6, 8, 8))[2:].zfill(6)))

        elif len(cipher_text) % 3 == 2:
            six_bits_flow.append(bin(self.get_bits(ord(cipher_text[len(cipher_text) - 2:-1]), 0, 6, 8))[2:].zfill(6))
            six_bits_flow.append(str(bin(self.get_bits(ord(cipher_text[len(cipher_text) - 2:-1]), 6, 8, 8))[2:].zfill(2)
                    + str(bin(self.get_bits(ord(cipher_text[-1]), 0, 4, 8))[2:].zfill(4))))
            six_bits_flow.append(str(bin(self.get_bits(ord(cipher_text[-1]), 4, 8, 8))[2:].zfill(4)) +
                    str(bin(self.get_bits(ord(cipher_text[-1]), 4, 6, 8))[2:].zfill(2)))
            six_bits_flow.append(str(bin(self.get_bits(int("0", 2), 6, 8, 8))[2:].zfill(6)))

        six_bits_flow_decimal = [int(decimal, 2) for decimal in six_bits_flow]
        six_bits_flow_decimal_encoded = [((decimal + 32) % 95) for decimal in six_bits_flow_decimal]#% 64
        six_bits_flow_decimal_encoded_ascii = "".join(map(lambda ascii: chr(ascii), [decimal for decimal in six_bits_flow_decimal_encoded]))

        plain_text += six_bits_flow_decimal_encoded_ascii

        return plain_text


    def decode_uu_charset(self, cipher_text):
        """
        Decode the uu encoded string in argument to ascii string.

        :param cipher_text: string
        :return: string

        >>> from cryptanalib.encoding.format import Format
        >>> format = Format()
        >>> format.decoding["ascii_charset"]["0x41"]
        'A'
        >>> format.decoding["uu_charset"]("ABCDAZERTY") == format.decode_uu_charset("ABCDAZERTY")
        True
        >>> "AAAAB" == format.decoding["uu_charset"](format.encoding["uu_charset"]("AAAAB"))
        True
        >>> format.decoding["uu_charset"]("A5&AI<R!I<R!A(&=R96%T(&1A>2!T;R!D:64@=&]D87DA")
        'This is a great day to die today!'
        """
        plain_text = ""

        three_characters = []
        for character_group in list(zip(*[iter(cipher_text[1:len(cipher_text)])] * 4)):
            character_group = "".join(character_group)
            four_six_bits = []
            for c in character_group:
                c = bin((ord(c) - 32) % 64)[2:].zfill(6)
                four_six_bits.append(c)
            three_characters.append(
                chr(int(str(bin(self.get_bits(int(four_six_bits[0], 2), 0, 6, 6))[2:].zfill(6)) +
                str(bin(self.get_bits(int(four_six_bits[1], 2), 0, 2, 6))[2:].zfill(2)), 2))
            )
            three_characters.append(
                chr(int(str(bin(self.get_bits(int(four_six_bits[1], 2), 2, 6, 6))[2:].zfill(4)) +
                str(bin(self.get_bits(int(four_six_bits[2], 2), 0, 4, 6))[2:].zfill(4)), 2))
            )
            three_characters.append(
                chr(int(str(bin(self.get_bits(int(four_six_bits[2], 2), 4, 6, 6))[2:].zfill(2)) +
                str(bin(self.get_bits(int(four_six_bits[3], 2), 0, 6, 6))[2:].zfill(6)), 2))
            )
        for c in three_characters:
            if ord(c) != 0:
                plain_text += c

        return plain_text


    def get_bits(self, num, start, end, length=64):
        mask = 2**(end-start)-1
        shift = length - (end-start) - start

        return (num & (mask << shift)) >> shift