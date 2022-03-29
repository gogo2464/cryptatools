<!-- GETTING STARTED -->
## Getting Started

This is a cryptanalysis tool for exploit developers and ctf players.

The name come from pwntools a similar tool to exploit memory corruption vulnerabilities. This software aims to work like pwntools but for cryptanalysis.

Then this program include a library like pwnlib. And it will expose some command line tools. Like pwntools.

### Installation for Windows

Run:

  ```shell
  Invoke-WebRequest -uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
  python get-pip.py
  pip install virtualenv
  python -m venv "venv3"
  .\venv3\Scripts\activate
  
  git clone https://github.com/gogo2464/cryptatools
  cd cryptatools
  pip install setup.py
  ```

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation for Linux

Run:

  ```sh
  sudo apt install virtualenv pip -y
  virtualenv -p python3 venv3
  source venv3/bin/activate
  
  git clone https://github.com/gogo2464/cryptatools
  cd cryptatools
  pip install setup.py
  
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can download corpus from nltk corpus database to make frequential analysis.

```python
from cryptalib.frequency import *

if __name__ == "__main__":
    fa = FrequencyAnalysis()
    fa.set_letters_frequency_from_nltk_corpus(['gutenberg', 'brown'])
    print(fa.caracters_frequency)
    print(fa.corpus_caracters_frequency)
```

_For more examples, please refer to the [Tutorial](https://example.com) or to the documentation [Documentation](https://example.com)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- TESTING EXAMPLES -->
## Testing

In order to run unit tests, you MUST be in the directory cryptatools at root.
Run unit tests with doctests with the command:

```shell
nosetests --with-doctest .\tests\doctests.py --verbose
```

You could also run for a specific file like with:
````shell
python -m doctest .\cryptalib\frequency.py -v
````

Unit test are made with doctests.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- DOCUMENTATION EXAMPLE -->
## Documentation

First, to edit documentation, edit the file `cryptatools/docs/source/api.rst` and follow this [guide](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html).

In order to generate documentation from root folder do:

```shell
make -C .\docs\ html
```

This project uses Sphinx.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Document your work. See [the how to make documentation chapter](https://github.com/gogo2464/cryptatools#documentation)
2. Fork the Project
3. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

I did not choose the license type yet... Fell free to ask me if you absolutely want top get a license name then I could choose.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

gogo - gogo246475@gogo246475@gmail.com

Project Link: [https://github.com/gogo2464/cryptatools](https://github.com/gogo2464/cryptatools)

<p align="right">(<a href="#top">back to top</a>)</p>