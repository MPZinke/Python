

import os
from pathlib import Path
import sys


from .RunMacros import run_macros


assert(len(sys.argv) == 2), "Usage: tsmacros <mapping_json_path> [<source_directory_path>]"
mappings_file_path = Path(os.path.join(os.getcwd(), Path(sys.argv[1])))

run_macros(mappings_file_path)
