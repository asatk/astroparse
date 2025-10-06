astroparse documentation
========================

About
-----

Having trouble reading data tables into Python using conventional methods like
Pandas or Astropy? AstroParse is the right package for you! It is a simple,
customizable tool that allows you to parse text data from sources with
non-standard formats. This package originally targeted astronomical data
that often come in irregular text forms that are not easy to read by both
humans and Python.

Getting Started
---------------

Install astroparse: ``pip install astroparse``

TL;DR

The function `parse_file` is a simple way to parse an irregular data table
within Python. This file can be saved to an output file or used within Python
as an Astropy Table.

The `Reader` allows users to parse multiple files at once. The method
`Reader.read_lists` is best for parsing multiple files of similar formats
and structure; the method `Reader.read_dicts` is best for parsing multiple
files of different formats or structures. All methods use the same or
similar interface to `parse_file`.

Contents
--------

.. toctree::
    parse_file
    reader
    defaults


