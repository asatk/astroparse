"""
Parse data tables with weird formats, e.g., spaces separating columns, dots
specifying missing data. 

Author: Anthony Atkinson
Created: 2025.09.22
Modified: 2025.10.03
"""

import argparse as ap
from astropy.table import Table
import re

###### parse functions

# default values for command-line arguments for file parsing
DF = {
    "c": r"( |\t)+(?![\t\n ])",     # regex pattern for spaces and tabs
    "d": ",",
    "m": -1,
    "n": r"\.\.\.+",            # regex pattern for filler chars/missing data
    "o": None,
    "p": "",
    "r": (0, None),
    "s": "_new",
    "x": ".txt",
}

# help text for command-line arguments
help = {
    "c": "Delimiter/separator regex pattern to be replaced in input file.",
    "d": "Delimiter character/string to be used for output file.",
    "f": "Filename to be parsed.",
    "m": "Metadata/header line number.",
    "n": "NaN regex pattern to be replaced in input file.",
    "o": "Output filename. Overrides any settings with `prefix`, `suffix`, "+\
        "and extension.",
    "p": "Prefix for the output filename.",
    "r": "Range of lines from input file to be parsed as data. The range is "+\
        "one or two numbers, e.g., `lo hi` where lo is included and hi is " +\
        "excluded. `hi` is optional; will default to the end of the file.",
    "s": "Suffix for the output filename (goes before the extension).",
    "x": "Extension for the output filename.",
}

# constant number of maximum lines the parser will parse
MAXLINE = 1_000_000

# parse command line arguments
def parse_args():
    """
    Parse command-line arguments
    """
    # set up parser
    parser = ap.ArgumentParser(
            prog="parse_table.py",
            usage="%(prog)s filename [options]",
            description=__doc__,
            formatter_class=ap.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--regdelim", type=str, default=DF["c"],
                        help=help["c"])
    parser.add_argument("-d", "--delimiter", type=str, default=DF["d"],
                        help=help["d"])
    parser.add_argument("filename", type=str, help=help["f"])
    parser.add_argument("-n", "--regnan", type=str, default=DF["n"],
                        help=help["n"])
    parser.add_argument("-m", "--meta", type=int, default=DF["m"],
                        help=help["m"])
    parser.add_argument("-o", "--out", type=str, default=DF["o"],
                        help=help["o"])
    parser.add_argument("-p", "--prefix", type=str, default=DF["p"],
                        help=help["p"])
    parser.add_argument("-r", "--range", type=int, nargs="*", default=DF["r"],
                        help=help["r"])
    parser.add_argument("-s", "--suffix", type=str, default=DF["s"],
                        help=help["s"])
    parser.add_argument("-x", "--extension", type=str, default=DF["x"],
                        help=help["x"])

    return vars(parser.parse_args())


def parse_file(args: dict):
    """
    Read a file line by line. Replace input delimiter with output delimiter and
    replace missing data pattern with `nan`.
    """

    # keep the header line if desired
    hdr = args["meta"]

    # parse only the lines from the input file that the user is interested in
    line_range = args["range"]
    # lower limit of data range -- header cannot be in data section
    lo = max(line_range[0], hdr)
    # upper limit of data range -- can be end of file if None provided
    if len(line_range) == 1 or line_range[1] is None:
        hi = MAXLINE
    else:
        hi = line_range[1]

    ### PATTERNS
    # regex pattern matching input file separator/delimiter.
    pdelim = re.compile(args["regdelim"])

    # regex pattern matching input file missing data.
    pnan = re.compile(args["regnan"])

    # output delimiter
    delim = args["delimiter"]

    ### FILE I/O
    # open input file `filename`
    fnamein = args["filename"]
    fin = open(fnamein, "r")
    
    # construct output filename
    fnameout = args["out"]
    if args["out"] is None:
        ext = args["extension"]
        pfx = args["prefix"]
        sfx = args["suffix"]

        # locate the position of the file extension in the input filename
        ext_loc = fnamein.rfind(".")
        # create the new filename
        fnameout = pfx + fnamein[:ext_loc] + sfx + ext
    print(f"writing data to new file -- {fnameout}")

    # open output file, overwriting previous contents of file if they existed
    fout = open(fnameout, "w")

    # track line number as file is read
    linect = 1

    # read first line to initiate reading process
    line = fin.readline()

    # NOTE end of file reached when `line` is empty string, i.e., ''


    ### PRE LOOP / HEADER
    # skip lines before the range of desired lines
    while linect < lo and line != '':

        # extract header if desired
        if linect == hdr:
            # if the header line matches the regular line pattern, sub for delim
            if pdelim.search(line) is not None:
                line_new = pdelim.sub(delim, line)
            else:
                line_new = line
            # write the header line to output
            fout.write(line_new)

        # read next line in file
        line = fin.readline()
        linect += 1


    ### MAIN LOOP
    # iterate through file's lines from lo (incl.) to hi (excl.)
    while linect < hi and line != '':

        # end of file reached
        if line == '':
            break

        # replace missing data chars with nan
        line_nonan = pnan.sub("nan", line)

        # matches for whitespace in each line
        line_new = pdelim.sub(delim, line_nonan)

        # write to the new file
        fout.write(line_new)

        # read next line in file
        line = fin.readline()
        linect += 1

    # close input and output files before terminating executation
    fin.close()
    fout.close()


# don't accidentally execute script if somehow this module is loaded by
# something else. this is the code 'entry point'
if __name__ == "__main__":
    args = parse_args()
    parse_file(args)
