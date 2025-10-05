# Welcome to AstroParse!

## About

Having trouble reading data tables into Python using conventional methods like
Pandas or Astropy? AstroParse is the right package for you! It is a simple,
customizable tool that allows you to parse text data from sources with 
non-standard formats. This package originally targeted astronomical data 
that often come in irregular text forms that are not easy to read by both 
humans and Python.

## Getting Started

Download the contents of AstroParse into your working directory:

```git clone https://github.com/asatk/astroparse.git```

In your code, use:

`from astroparse import parse_file` to parse an individual file.

-- OR --

`from astroparse import Reader` to access the flexible
`Reader` to parse multiple files at once; it uses the same interface as
`parse_file`.

## Next Steps

Check out the examples in `astroparse/tests`!

