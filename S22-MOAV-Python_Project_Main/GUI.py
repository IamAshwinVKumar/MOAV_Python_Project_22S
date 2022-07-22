""" The Graphical user interface(GUI), a stand-alone script incorporating all the programs """

import tkinter as tk
from main import *
from tkinter.messagebox import showinfo


class Interface(tk.Frame):
    """
    Class authors: Ashwin and Yin
    Class for generating Graphical User Interface and
    displaying the results and plots.
    Associated parameters: master, which represents the main window in tkinter
    """

    def __init__(self, master=None):
        """
        Here we assign values to the class attributes and all the associated parameters.
        :param master:is the parameter which represents the main window of the tkinter
        """
        tk.Frame.__init__(self, master)
        # The icon and the heading of the GUI window is defined here
        self.master.title("Prediction Model for WWTP Parameter(GUI)")
        self.master.iconbitmap("Images/icon.ico")
        # Dimensioning of the GUI window
        w = 600  # Width
        h = 375  # Height
        # Defines the window position
        wx = (self.master.winfo_screenwidth() - w) / 2
        wy = (self.master.winfo_screenwidth() - h) / 2
        # Window geometry
        self.master.geometry("%dx%d+%d+%d" % (w, h, wx, wy))
        # Space around the window
        self.dx = 5
        self.dy = 5
        # Colour filling the window is defined here
        self.master.configure(bg="light blue")
        self.pack()
        # Defining labels/buttons
        table_label = tk.Label(master, text="The WWTP data is already fed")
        table_label.pack()
        group_button = tk.Button(master, text="Predict WWTP data using Random Forest Model",
                                 command=lambda: self.message("Prediction Model is complete"))
        group_button.pack()
        red_button = tk.Button(master, text="Click to view the accuracy",
                               command=lambda: self.messages("Accuracy is {}".format(Accuracy)))
        red_button.pack()
        green_button = tk.Button(master, text="Result plot of prediction model (RF Model)",
                                 command=lambda: self.plot())
        green_button.pack()
        # Window close Button
        self.close_button = tk.Button(text="Exit and Close", fg='red',
                                      command=lambda: self.master.quit())
        self.close_button.place(anchor=tk.E, x=535, y=290, rely=0.1)

    def message(self, message):
        """ Display the message after clicking the button
        :param message: string
        :return: The message
        """
        showinfo("Prediction process!!", message)

    def messages(self, message):
        """ Accuracy of the RF prediction model is displayed """
        showinfo("ACCURACY ", message)

    def plot(self):
        """
        Plot the predicted and the measured values
        :return: Plot
        """
        b = plot
        b.plotting(Prediction, y_test)
        showinfo("Plotted!")


# Instantiate a User interface object
if __name__ == "__main__":
    Interface().mainloop()
