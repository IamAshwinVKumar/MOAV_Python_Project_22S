"""All the folder paths, packages used, the input files are specified here."""

# To import basic libraries in python.
try:
    import os
    import logging
except ModuleNotFoundError as basic:
    print('ModuleNotFoundError : Basic libraries are missing (suggested: logging, os, math)')
    print(basic)

# To import global libraries in python.
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    # To import Random Forest(RF) Model
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import metrics
except ModuleNotFoundError as additional:
    print('ModuleNotFoundError: Missing global packages (required: numpy, pandas, matplotlib, scikit-learn)')
    print(additional)
