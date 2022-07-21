from config import *
"""
"""

class plot:
    """

    """
    def __init__(self,prediction,measurment_value):
        """

        """


    def plotting(prediction, measurment_value):
        """
        plot the measurment and predicted value

        :param measurment_value: numpy array
        :return: numpy array
        """
        fig, axes = plt.subplots(figsize=(10, 6))
        plt.plot(prediction, label="prediction", color="green")
        plt.plot(measurment_value, label="measured", color="purple")
        plt.grid()
        plt.legend(title="color")
        plt.title("Comparison")
        plt.show()

