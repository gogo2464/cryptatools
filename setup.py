from setuptools import setup

setup(
   name='cryptatools',
   version='1.0',
   description='A ctf tool like pwntools but for cryptanalysis instead of pwn.',
   author='gogo',
   author_email='gogo246475@gmail.com',
   packages=['cryptalib', 'crypta'],
   install_requires=['nltk', 'nose'],
)