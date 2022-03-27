import doctest
import unittest

modules = ("cryptalib.frequency",
           "cryptalib.alphabets")
suite = unittest.TestSuite()
for mod in modules:
    suite.addTest(doctest.DocTestSuite(mod))
runner = unittest.TextTestRunner()
runner.run(suite)