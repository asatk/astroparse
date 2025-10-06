"""
Example script demonstrating the use of the `Reader` class.
"""

from astroparse import Reader

if __name__ == "__main__":
    
    # input file name
    fname = "test_data/EEM_dwarf_UBVIJHK_colors_Teff.txt"

    # header line of input file is L23
    hdr = 23

    # first line of data in input file is L24
    lo = 24

    # last line of data in input file is L 141
    hi = 141

    # capture NaNs using custom regex pattern
    nan_reg = r"\.\.\.+"

    # create Reader object with these data as defaults for parsing a file
    reader = Reader(nan_reg=nan_reg, hdr=hdr, lo=lo, hi=hi)

    # read the data from the file into Python
    tbl = reader.parse_file(fname)

    # pretty print the astropy Table
    tbl.pprint()
