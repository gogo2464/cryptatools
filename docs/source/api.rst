API
===

.. autosummary::
    :toctree: generated

.. automodule:: cryptanalib

.. autoclass:: cryptanalib.cryptanalysis_algorithm.frequency::FrequencyAnalysis

    .. automethod:: set_letters_frequency_from_nltk_corpus(corpus_names)

    .. automethod:: measure_frequency_from_target(target_code)

.. autoclass:: cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector::PlainTextDetector(language)

    .. automethod:: detect_plain_text(self, plain_or_cipher_text, similarity_level=0.5)