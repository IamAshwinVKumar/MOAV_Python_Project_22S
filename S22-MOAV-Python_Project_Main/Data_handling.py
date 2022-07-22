""" Custom class for data handling """
from config import *


class DataHandler:
    """ Class Author: Ashwin
        Class with Methods, for data manipulation and printing.
        Involves extracting data from ".xlxs" file and sorting.
        Methods:
            data_handler(): Method pre-processes the data into pandas dataframe
            print(): Method for printing the dataframe
    """
    def __init__(self, years):
        """ Instantiating objects in the class """
        self.years = years
        self.header = 0
        self.A = pd.DataFrame()
        self.path = str

    def data_handler(self):
        """
        Pre-process the required data into pandas dataframe
        :return: combined data frame of all the input files
        """
        for year in self.years:
            self.path = os.path.abspath("") + "/" + "WWTP-data-input/" + "WWTP_data_" + year + ".xlsx"
            data = pd.read_excel(self.path, header=self.header)
            self.A = self.A.append(data)
        return self.A

    def print(self):
        """
         Display the pandas' data frame
        :return: Print the combined value
        """
        print(self.A)

