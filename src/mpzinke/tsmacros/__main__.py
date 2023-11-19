

from pathlib import Path
import sys


from .RunMacros import run_macros


assert(len(sys.argv) == 2), "Usage: tsmacros <tsc_file_path> <mapping_json_path> [<outfilename>]"
mappings_file_path = Path(sys.argv[1])

run_macros(mappings_file_path)
