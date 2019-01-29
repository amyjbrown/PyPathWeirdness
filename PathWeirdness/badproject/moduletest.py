# tests module.py
# This shows how different import paths lead to non-shared state

# This emulates setting src as a source code directory in an IDE, thus [,,,/badproject] and and [,,,/badproject/src] are in sys.path
import sys, os
relative_directory = os.path.abspath(os.path.dirname(sys.argv[0])) # get the absolute path to parent directory
relative_path = os.path.join(relative_directory, "src") # add currentpath/src to PYTHONPATH
sys.path.append(relative_path)

import src.shared
import src.module

# makes src.shared.x := 5
src.shared.main()  

# As src.shared.x has been set to x via above, this should print '5', but will raise an attribute error
src.module.main()  
