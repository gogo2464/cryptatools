import doctest
import unittest

modules = ("cryptanalib.cryptanalysis_algorithm.coincidence_index",
           "cryptanalib.cryptanalysis_algorithm.frequency",
           "cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector",
           "cryptanalib.cryptanalysis_algorithm.brute_forcing.generic_brute_forcer",
           "cryptanalib.cryptanalysis_algorithm.brute_forcing.victim_algorithm.caesar_number",
           "cryptanalib.encryption.caesar_number_encryption",
           "cryptanalib.encoding.encoding",
           "cryptanalib.encoding.alphabet",
)

suite = unittest.TestSuite()
for mod in modules:
    suite.addTest(doctest.DocTestSuite(mod))
runner = unittest.TextTestRunner()
runner.run(suite)