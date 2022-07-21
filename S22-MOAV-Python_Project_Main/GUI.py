import tkinter as tk
from main import *
from tkinter.messagebox import showinfo


class VanillaApp(tk.Frame):
    """

    """
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        table_label = tk.Label(master, text="WWTP data is already fed")
        table_label.pack()
        vanilla_button = tk.Button(master, text="Predict WWTP data", command=lambda: self.message("Prediction is done"))
        vanilla_button.pack()
        red_button = tk.Button(master, text="Click to view the accuracy", command=lambda: self.messages("Accuracy is {}".format(Accuracy)))
        red_button.pack()
        green_button = tk.Button(master, text="Result plot",
                               command=lambda: self.plot())
        green_button.pack()
    def message(self, message):
        """
        Display the message after clicking the button
        :param message: string
        :return: The message
        """
        showinfo("Prediction process !!!", message)
    def messages(self,messagee):
        showinfo("ACCURACY ", messagee)
    def plot(self):
        """
        Plot the predicted and the measured values
        :return: Plot
        """
        B = plot
        B.plotting(Prediction, Y_test)



# instantiate a VanillaApp object
if __name__ == "__main__":
    VanillaApp().mainloop()