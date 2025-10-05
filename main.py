"""
Example script demonstrating how to use the parseutil package.
"""

from astroparse import parse_file, Reader

if __name__ == "__main__":
    


    ### Directly calling the parse_file function

    fname_func = "0.08M_history.data"
    tbl_func = parse_file(fname_func, hdr=6, lo=7)
    tbl_func.pprint()



    ### Using the Reader object on one file

    fname_one = "EEM_dwarf_UBVIJHK_colors_Teff.txt"
    reader_one = Reader(nan_reg=r"\.\.\.+", hdr=23, lo=24, hi=141)
    tbl_one = reader_one.parse_file(fname_one)
    tbl_one.pprint()


    
    ### Using the Reader object on multiple similarly-formatted files

    # data from this website I found when looking for an arbitrary stellar
    # evolution track database:
    # https://www.unige.ch/sciences/astro/evolution/en/database

    flist = [
        "M002Z00V0.dat",
        "M002Z00V4.dat",
        "M003Z00V0.dat",
        "M003Z00V4.dat"
    ]
    
    out_list = [
        "file1.csv",
        "file2.csv",
        "file3.csv",
        None
    ]

    reader_many = Reader(hdr=1, lo=4)
    tbl_list = reader_many.read_lists(flist, out_list=out_list)
    for tbl in tbl_list:
        tbl.pprint()



    ### Using the Reader object on multiple differently-formatted files

    reader_dict = Reader()
    dict_list = [
        dict(fname_in="0.08M_history.data",
             hdr=6, lo=7),
        dict(fname_in="EEM_dwarf_UBVIJHK_colors_Teff.txt",
             nan_reg=r"\.\.\.+", hdr=23, lo=24, hi=141, fname_out="file.csv"),
        dict(fname_in="M003Z00V4.dat",
             hdr=1, lo=4)
    ]

    tbl_list_dict = reader_dict.read_dicts(dict_list)
    for tbl in tbl_list_dict:
        tbl.pprint()
