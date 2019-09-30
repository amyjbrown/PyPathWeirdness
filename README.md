# PyPathWeirdness
Example of one file being loaded as two modules due to being found through too parts of python path

Pull this and run it anywhere
I am not yet sure if this is implementation specific, but this is behavior I wish to document

`$ python3 goodproject/moduletest.py`

`5`

`$ python3 badproject/moduletest.py`

`AttributeError: module shared has no attribute x`
