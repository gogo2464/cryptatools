import doctest
import unittest

modules = ("cryptanalib.cryptanalysis_algorithm.frequency",
           "cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector",
           "cryptanalib.encoding.format",)

suite = unittest.TestSuite()
for mod in modules:
    suite.addTest(doctest.DocTestSuite(mod))
runner = unittest.TextTestRunner()
runner.run(suite)