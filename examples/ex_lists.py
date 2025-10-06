"""
Example script demonstrating the use of the `Reader` class on multiple
similarly-formatted input files.
"""

from astroparse import Reader

if __name__ == "__main__":

    # data source: https://www.unige.ch/sciences/astro/evolution/en/database

    # input file names
    flist = [
        "test_data/M002Z00V0.dat",
        "test_data/M002Z00V4.dat",
        "test_data/M003Z00V0.dat",
        "test_data/M003Z00V4.dat"
    ]
    
    # output file names
    out_list = [
        "file1.csv",
        "file2.csv",
        "file3.csv",
        None            # no output desired for the fourth file!
    ]

    # header line of input files is L1
    hdr = 1

    # first line of data in input files is L4
    lo = 4

    # create Reader object with these data as defaults for parsing all files
    reader = Reader(hdr=hdr, lo=lo)

    # read the data from the files into Python
    tbl_list = reader.from_lists(flist, out_list=out_list)

    # pretty print each astropy Table
    for tbl in tbl_list:
        tbl.pprint()
