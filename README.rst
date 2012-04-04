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
- Example `Makefile` for quick development setup using virtualenv and pip


Use
---

To create a new project derived from the boilerplate: ::

    ~/Projects $ git clone https://github.com/splaice/py-bootstrap.git
    ~/Projects $ cd py-bootstrap
    ~/Projects/py-bootstrap $ mkdir ~/Projects/myproject && git archive master | tar -x -C ~/Projects/myproject

Now you should have a reasonable working python project. You can set it up in development mode using the `Makefile`

    ~/Projects/myproject $ make dev

The tests should all work:

    ~/Projects/myproject $ make test


Contribute
----------

#. Fork the project on github to start making your changes
#. Send pull requests with your bug fixes or features
#. Submit and create issues on github
