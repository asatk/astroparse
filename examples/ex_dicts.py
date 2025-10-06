"""
Example script demonstrating the use of the `Reader` class on multuple
differently-formatted input files.
"""

from astroparse import Reader

if __name__ == "__main__":
    
    # create Reader object accepting the default parsing behavior for all files
    reader = Reader()

    # provide the parsing arguments specific to each file
    dict_list = [
        dict(fname_in="test_data/0.08M_history.data",
             hdr=6, lo=7),
        dict(fname_in="test_data/EEM_dwarf_UBVIJHK_colors_Teff.txt",
             nan_reg=r"\.\.\.+", hdr=23, lo=24, hi=141, fname_out="file.csv"),
        dict(fname_in="test_data/M003Z00V4.dat",
             hdr=1, lo=4)
    ]
    
    # read the data from the files into Python
    tbl_list = reader.from_dicts(dict_list)

    # pretty print each astropy Table
    for tbl in tbl_list:
        tbl.pprint()
