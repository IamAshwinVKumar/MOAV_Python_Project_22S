from config import *


class plot:
    """ Class author: Yin
        Class for plotting the COD parameter, both recorded and prediction.
    """
    def __init__(self):
        """
        Used for assigning of input values to class attributes
        """

    def plotting(prediction, recorded_value):
        """
        Plot the recorded and predicted value of Chemical oxygen demand(COD) parameter
        :param recorded_value: numpy array
        :return: numpy array
        """
        fig, axes = plt.subplots(figsize=(10, 6))
        plt.plot(prediction, label="prediction", color="green")
        plt.plot(recorded_value, label="measured", color="purple")
        plt.grid()
        axes.set_xlabel("Time_period(years)")
        axes.set_ylabel("COD(mg/l)")
        plt.legend(title="color")
        plt.title("Comparison of COD parameter")
        plt.show()
