API
===

.. autosummary::
    :toctree: generated

.. automodule:: cryptanalib

.. automodule:: cryptanalib.cryptanalysis_algorithm

.. autoclass:: cryptanalib.cryptanalysis_algorithm.frequency::FrequencyAnalysis

    .. automethod:: set_letters_frequency_from_nltk_corpus(corpus_names)

    .. automethod:: measure_frequency_from_target(target_code)

.. automodule:: cryptanalib.cryptanalysis_algorithm.brute_forcing

.. autoclass:: cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector::PlainTextDetector(language)

    .. automethod:: detect_plain_text(self, plain_or_cipher_text, similarity_level=0.5)

.. automodule:: cryptanalib.encoding

.. autoclass:: cryptanalib.encoding.format.Format
   :members: encoding, decoding

    .. automethod:: encode_uu_charset(self, cipher_text)

    .. automethod:: decode_uu_charset(self, cipher_text)

    .. automethod:: get_bits(num, start, end, length=64)