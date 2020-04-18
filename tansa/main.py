from .tansa import finder
from .tansa import jreader

import sys

if __name__ == '__main__':
    file_list = finder.FileFinder(sys.argv[1]).file_list
    print(jreader.JReader().json_dispenser(file_list))