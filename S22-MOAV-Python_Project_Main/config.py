# All the folder paths, packages used and the input files are specified here.

# To import basic libraries in python.
try:
    import pandas as pd
    import os
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import metrics
    import matplotlib.pyplot as plt
    import numpy as np

except ModuleNotFoundError as basic:
    print( 'ModuleNotFoundError : Basic libraries are missing')
    print(basic)




