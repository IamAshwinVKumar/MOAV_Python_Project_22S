from config import *

"""

"""

class DataHandler:
    """

    """
    def __init__(self, years):
        self.years = years
        self.header = 0
        self.A = pd.DataFrame()
        self.path = str
    def DataHandlers(self):
        """
        Pre-process the required data into pandas dataframe

        :return: combined data frame of all the input files
        """


        for year in self.years:
            self.path = os.path.abspath("") + "/" + "WWTP-data-input/" + "WWTP_data_" + year + ".xlsx"
            Data = pd.read_excel(self.path, header=self.header)
            self.A = self.A.append(Data)
        return self.A

    def print(self):
        """
         Display the pandas data frame
        :return: Print the combined value
        """
        print(self.A)
