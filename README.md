# README

The exercise is to write a command-line text search engine.
 > Remember that the code should be executable on different machines running different operating systems and configurations.

There are different ways how to achieve that: VM, Docker container... Here  I used
`Python` virtual environment. To be really independent I  could put the code
on a  remote   machine.

>What constitutes a word

The word in this case is what is left  after reading all the file content as a string,
and removing all the characters  except `[^A-Za-z\s-]` and  changing new line
to space.

>Data structure design: the in memory representation to search against

In  this case for sake of simplicity and speed, the `set` was used.
Each text file content after filtering is being  prerpocessed by applying
`set` to `list`. The first thing is it  removes word duplicates, so we get
a vocabulary to search against. And the second reason is performance --
operation for  `element is set` has a O(1) complexity,
what  is the best possible.

>What constitutes two words being equal (and matching)

A hashes of the words should be equal to make words equal.

>Ranking score design

It is super simple: `# of matches/ # of words in search`

>Testability

A very simple tests with `pytest` are implemented.


## Usage:

1. `❯ git clone https://github.com/raalesir/sch.git`
1. `cd sch`
1. create virtual env for python3
    ```bash
    python3 -m venv sch
    source sch/bin/activate
    ```
    or use already existing
    ```bash
    source schibsted/bin/activate
    ```
1. install `pytest`
```bash
pip3 install -r requirements.txt
```
or skip it if used created  environment
1. run tests
```bash
pytest search.py
```
Both should pass
1. launch text search engine:
```bash
./search.py
```

##  Example of usage:

Text  files should be put  into the `data` folder.

```bash
 ❯ ./search.py                                                                                                                                                                                                          [08:42:08]
hello from python 3.7.7
input  words separated by space
to quit type  'q'
search>  hi hello test a
words to look for:  {'test', 'hello', 'a', 'hi'}
text file:  data/text3
text file:  data/text2
text file:  data/text1
the results:
{'name': 'data/text3', 'match_fraction': 50.0}
{'name': 'data/text2', 'match_fraction': 25.0}
{'name': 'data/text1', 'match_fraction': 25.0}
==============================
input  words separated by space
to quit type  'q'
search>
```
