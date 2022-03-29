import doctest
import unittest

modules = ("cryptanalib.cryptanalysis_algorithm.frequency",
           "cryptanalib.encoding.charsets")

suite = unittest.TestSuite()
for mod in modules:
    suite.addTest(doctest.DocTestSuite(mod))
runner = unittest.TextTestRunner()
runner.run(suite)