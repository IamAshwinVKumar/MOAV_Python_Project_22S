from config import *
from Data_handling import *
from plot import *

Years = ["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]

# Instantiating the class DataHandler
P = DataHandler(Years)
Frame = P.DataHandlers()



def split(Frame):
    """
    Splitting the pandas data frame into two training and test sets

    :param Frame: Pandas data frame
    :return: Training and test sets
    """
    X = Frame.drop(labels = ["COD_mg/l"], axis = 1)
    Y = Frame["COD_mg/l"].values
    Y= Y.astype("int")
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = .4, random_state = 20)
    return X_train, X_test, Y_train, Y_test

# Calling the function split
X_train, X_test, Y_train, Y_test = split(Frame)


def rf_model(X_train, Y_train, X_test):
    """
    Running the random forest model

    :param X_train: Pandas data frame
    :param Y_train: Pandas data frame
    :param X_test: Pandas data frame
    :return: Predicting values for the test datas
    """
    model = RandomForestClassifier(n_estimators=10, random_state=30)
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    return  prediction

# Calling the function RF model
Prediction = rf_model(X_train,Y_train, X_test)

# Determining Accuracy
Accuracy = (metrics.accuracy_score(Y_test,Prediction))








