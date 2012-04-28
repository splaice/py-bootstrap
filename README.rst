py-boostrap: Python Package Bootstrap Project
=========================

Python Package Bootstrap Project is an example boilerplate for creating
distributable Python packages.

There are lots of information detailing how to create a Python package
but few examples that are comprehensive. The goal of this project is to
provide Python developers with a boilerplate project they can use as a
guide and example.


Features
--------

- Example package and module layout
- Example testing integration and layout using testify
- Example `setup.py` using distutils
- Example `Makefile` for quick development setup using virtualenv, pip and ipython
- Simple project creation using boilerplate via `bin/boostrap.sh`


Use
---

To create a new project derived from the boilerplate: ::

    ~/Projects $ git clone https://github.com/splaice/py-bootstrap.git
    ~/Projects $ cd py-bootstrap
    ~/Projects/py-bootstrap $ bin/boostrap.sh project ~/Projects/Project

Now you should have a reasonable working python project. You can set it up in development mode using the `Makefile`

    ~/Projects/Project $ make dev

The tests should all work:

    ~/Projects/Project $ make test
    .
    PASSED.  1 test / 1 case: 1 passed, 0 failed.  (Total test time 0.00s)

If you need to debug your application with ipython:

    ~/Projects/Project $ make shell
    Python 2.7.3 (default, Apr 27 2012, 21:31:10) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.12.1 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: from project.models import Project

    In [2]:

Contribute
----------

#. Fork the project on github to start making your changes
#. Send pull requests with your bug fixes or features
#. Submit and create issues on github
