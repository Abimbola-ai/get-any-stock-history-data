from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]


setup(
    name='stocks',
    url='https://github.com/Abimbola-ai/get-any-stock-history-data',
    author='Abimbola Ojikutu',
    author_email='abimbola.ojikutu@iubh.de',
    packages=['stocks'],
    version='0.1',
    license='MIT',
    description='Get any stock input data from yahoo finance website',
)