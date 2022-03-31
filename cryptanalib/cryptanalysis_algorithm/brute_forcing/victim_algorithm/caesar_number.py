from cryptanalib.cryptanalysis_algorithm.brute_forcing.generic_brute_forcer import GenericBruteForcer

class CaesareNumberBruteForcer(GenericBruteForcer):
    def __init__(self, cipher_text):
        self.cipher_text = cipher_text

    def brute_force(self, format="ascii_charset"):
        pass