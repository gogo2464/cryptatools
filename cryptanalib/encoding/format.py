import string

formats = dict(
    ascii_charset = {number: hex(ord(number)) for number in string.printable},
    gameboy_pokered_custom_charset = {0x7f: " "}
)