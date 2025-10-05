"""
This file defines the default behaviors of the parser at runtime.
"""

### DEFAULT PARSER VALUES

# Regular expression that matches spaces/tabs as separators in input file.
sep_reg = r"(?<=\S)( |\t)+(?!\s)"

# Regular expression that matches three dots as empty/NaN entries in input file.
nan_reg = "nan"

# Maximum number lines that will be read from the input file.
MAX_LINE = 1_000_000
