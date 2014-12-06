abjad-ipython
=============

A small application to allow the interaction between IPython Notebook with
abjad (a musical notation system in Python).

Caveat: The current version was tested only on Python 3.4. If you have
problems with previous versions, please do contact me.


Important note
--------------

This has been now integrated into abjad. So no need to use this project.
It will stay here for future reference.


Requirements
------------

1. abjad - currently the github version, not the stable one
2. IPython Notebook. Version 2.0
3. Lilypond (required by abjad anyway)
4. wand (a Python ImageMagick library)
5. configobj
6. ply


Installation instructions
-------------------------

These instructions are for Ubuntu Linux. For other operating systems please
adapt.

Get abjad from github. On Ubuntu, the default IPython is not enough, get 2.0
(from github, pip or conda).

The default Lilypond version of the latest Ubuntu is also not enough. You need
at least 2.17

apt-get python3-wand python3-ply

configobj: pip3 install configobj --user


The examples
------------

A few examples are provided, there were taken from abjad documentation.
I am not the author of them (other than the conversion to notebooks).


How does it work?
-----------------

The system was designed to be as transparent as possible: after the typical

```python
from abjad import *
```

just add

```python
%run ../src/abjad-nb.py
```

(or whatever location you have for abjad-nb.py)

Now, abjad's show function will be replaced by one that will pipe the results
to the notebook. This includes the ability to pipe multi-page outputs.

License
-------

This code is distributed under a CC 1.0 Universal license. See the file
LICENSE.txt for details.

./tiago
