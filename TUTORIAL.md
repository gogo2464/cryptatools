Get frequency analysis database from nltk corpus database:

```python
from cryptanalib.cryptanalysis_algorithm.frequency import *

if __name__ == "__main__":
    fa = FrequencyAnalysis()
    fa.set_letters_frequency_from_nltk_corpus(['gutenberg', 'brown'])
    print(fa.caracters_frequency)
    print(fa.corpus_caracters_frequency)
```