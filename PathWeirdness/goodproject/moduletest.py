# tests module.py
# this project demonstrates one example of how a small change can make this work, and further more why it's so hard to catch
# 
# This emulates setting src as a source code directory in an IDE, thus [,,,/badproject] and and [,,,/badproject/src] are in sys.path
import sys, os
relative_directory = os.path.abspath(os.path.dirname(sys.argv[0])) # get the absolute path to parent directory
relative_path = os.path.join(relative_directory, "src") # add currentpath/src to PYTHONPATH
sys.path.append(relative_path)

import src.shared
import src.module

# makes src.shared.x := 5
src.shared.main()  

# Since src.module has `import src.shared` and NOT `import shared`, even though the path modification is still here this will print 5 as logically it should
src.module.main()  
