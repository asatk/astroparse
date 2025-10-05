"""
Example script demonstrating the use of the `parse_file` function.
"""

from src import parse_file

if __name__ == "__main__":

    # input file name
    fname = "test_data/0.08M_history.data"

    # header line of input file is L6
    hdr = 6

    # first line of data in input file is L7
    lo = 7

    # read the data from the file into Python
    tbl = parse_file(fname, hdr=hdr, lo=lo)

    # pretty print the astropy Table
    tbl.pprint()

