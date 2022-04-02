API
===

.. autosummary::
    :toctree: generated

.. automodule:: cryptatools

.. automodule:: cryptanalib

.. automodule:: cryptanalib.cryptanalysis_algorithm

.. autoclass:: cryptanalib.cryptanalysis_algorithm.frequency::FrequencyAnalysis

    .. automethod:: set_letters_frequency_from_nltk_corpus(corpus_names)

    .. automethod:: measure_frequency_from_target(target_code)

.. automodule:: cryptanalib.cryptanalysis_algorithm.brute_forcing

.. automodule:: cryptanalib.cryptanalysis_algorithm.brute_forcing.victim_algorithm

    .. autoclass:: cryptanalib.cryptanalysis_algorithm.brute_forcing.victim_algorithm.caesar_number::CaesareNumberBruteForcer(cipher_text, alphabet)

        .. automethod:: brute_force(format="ascii_charset", language="english", frequency_required=0.25)

.. autoclass:: cryptanalib.cryptanalysis_algorithm.brute_forcing.plain_text_detector::PlainTextDetector(language)

    .. automethod:: detect_plain_text(plain_or_cipher_text, similarity_level=0.5)

.. automodule:: cryptanalib.encoding

.. autoclass:: cryptanalib.encoding.format.Format
   :members: encoding, decoding

    .. automethod:: encode_uu_charset(cipher_text)

    .. automethod:: decode_uu_charset(cipher_text)

    .. automethod:: get_bits(num, start, end, length=64)

.. automodule:: cryptanalib.encryption

.. autoclass:: cryptanalib.encryption.caesar_number_encryption::CaesarNumberEncryption

    .. automethod:: encrypt(plain_text, key)