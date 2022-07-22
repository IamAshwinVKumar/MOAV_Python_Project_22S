""" main script holding all the functions implemented in this project
    authors: Ashwin and Yin
"""

from Data_handling import *
from plot import *

# Range of available data in years
Years = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
         "2020", "2021"]

# Instantiating the class DataHandler
P = DataHandler(Years)
frame = P.data_handler()


def split(frame):
    """
    Splitting the Pandas' data frame into two training and test sets

    :param frame: Pandas data frame
    :return: Training and test sets
    """
    x = frame.drop(labels=["COD_mg/l"], axis=1)
    y = frame["COD_mg/l"].values
    y = y.astype("int")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.4, random_state=20)
    return x_train, x_test, y_train, y_test


# Calling the function split
x_train, x_test, y_train, y_test = split(frame)


def rf_model(x_train, y_train, x_test):
    """
    Running the random forest model

    :param x_train: Pandas data frame
    :param y_train: Pandas data frame
    :param x_test: Pandas data frame
    :return: Predicting values for the test datas
    """
    model = RandomForestClassifier(n_estimators=10, random_state=30)
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    return prediction


# Calling the function RF model
Prediction = rf_model(x_train, y_train, x_test)


# Determining Accuracy
Accuracy = (metrics.accuracy_score(y_test, Prediction))
