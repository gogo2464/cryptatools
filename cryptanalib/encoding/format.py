import string

def get_bits(num, start, end, length=64):
    mask = 2**(end-start)-1
    shift = length - (end-start) - start

    return (num & (mask << shift)) >> shift


def encode_uu_charset(text):
    size_opcode = 1
    size_code = chr(len(text) + 32)

    if (len(text) % 3 < 3):
        size_code += "0" * (len(text) % 3 - size_opcode)

    plain_text = ""
    plain_text += size_code

    six_bits_flow = []
    for c in list(zip(*[iter(text)]*3)):
        c = "".join(c)
        six_bits_flow.append(bin(get_bits(ord(c[0:0+1]), 0, 6, 8))[2:].zfill(6))
        six_bits_flow.append((str(bin(get_bits(ord(c[0:0+1]), 6, 8, 8))[2:].zfill(2)) + str(bin(get_bits(ord(c[1:1+1]), 0, 4, 8))[2:].zfill(4))).zfill(6))
        six_bits_flow.append((str(bin(get_bits(ord(c[1:1+1]), 4, 8, 8))[2:].zfill(4)) + str(bin(get_bits(ord(c[2:2+1]), 0, 2, 8))[2:].zfill(2))).zfill(6))
        six_bits_flow.append(str(bin(get_bits(ord(c[2:2+1]), 2, 8, 8))[2:].zfill(4)).zfill(6))

    if len(text) % 3 == 1:
        six_bits_flow.append(bin(get_bits(ord(text[len(text) - 1]), 0, 6, 8))[2:].zfill(6))
    elif len(text) % 3 == 2:
        six_bits_flow.append(bin(get_bits(ord(text[:-1]), 0, 6, 8))[2:].zfill(6))

    six_bits_flow_decimal = [int(decimal, 2) for decimal in six_bits_flow]
    six_bits_flow_decimal_encoded = [((decimal + 32) % 95) for decimal in six_bits_flow_decimal]#% 64
    six_bits_flow_decimal_encoded_ascii = "".join(map(lambda ascii: chr(ascii), [decimal for decimal in six_bits_flow_decimal_encoded]))

    plain_text += six_bits_flow_decimal_encoded_ascii

    if len(plain_text) % 3 == 1:
        plain_text += "00"
    elif len(plain_text) % 3 == 2:
        plain_text += "0"

    return plain_text

formats = dict(
    ascii_charset = {number: hex(ord(number)) for number in string.printable},
    uu_charset = lambda a: encode_uu_charset(a)
)
r"""
Encode text to a specific encoding. 

:param ascii_charset: encode single char to ascii hexadecimal
:param uu_charset: encode text to uu encoding

>>> from cryptanalib.encoding.format import formats, encode_uu_charset
>>> formats["ascii_charset"]["A"]
    0x41
>>> formats["uu_charset"]("ABCDAZERTY") == encode_uu_charset("ABCDAZERTY")
    True
"""