Default Parsing Behavior
========================

.. automodule:: astroparse.defaults
    :members:
    :member-order: bysource


In addition to these constants, the following behaviors are also assumed:

``hdr = -1``: The input file does not have a header line that shares
identical column format to the data lines.

``lo = 1``: The data lines begin on the first line of the file.

``hi = -1``: The data lines continue until the last line of the file.
