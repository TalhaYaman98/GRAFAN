import matplotlib.pyplot as plt  # For plotting graphs with Matplotlib
import numpy as np  # For numerical operations and arrays
import sys
from PyQt5 import QtWidgets  # PyQt5 for creating the user interface
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip  # PyQt5 application window and tooltip
from PyQt5.QtGui import QIcon  # For setting window icon
from Interface import Ui_MainWindow  # Import the interface class from a separate file


# Main class for the GUI, derived from QMainWindow
class analiz(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()  # Initialize the user interface
        self.ui.setupUi(self)  # Set up the interface
        self.setWindowIcon(QIcon("re1.jpg"))  # Set the window icon
        self.setToolTip("Proceed")  # Set a tooltip for the interface

        # Connect buttons to respective functions
        self.ui.pushButton.clicked.connect(self.std)  # Standard plot
        self.ui.pushButton_2.clicked.connect(self.ygn)  # Stack plot
        self.ui.pushButton_3.clicked.connect(self.piey)  # Pie chart
        self.ui.pushButton_4.clicked.connect(self.bar)  # Bar chart
        self.ui.pushButton_5.clicked.connect(self.hist)  # Histogram chart


    # Function to plot a standard graph
    def std(self):
        x = self.ui.lineEdit.text()  # Get X-axis data from the user input
        y = self.ui.lineEdit_2.text()  # Get Y-axis data from the user input
        xli = x.split(",")  # Split the data by commas to convert it into a list
        yli = y.split(",")
        listx = list(map(float, xli))  # Convert the data to floats
        listy = list(map(float, yli))
        plt.plot(listx, listy, "o--b")  # Plot the data with blue dashed lines and circles
        plt.title("Standard Graph")  # Set the title for the plot
        plt.xlabel("X Axis")  # Label for the X axis
        plt.ylabel("Y Axis")  # Label for the Y axis
        plt.legend()  # Display legend for the plot
        plt.show()  # Show the graph on the screen
    
    # Function to plot a stack plot
    def ygn(self):
        d1 = self.ui.lineEdit_3.text()  # First dataset
        d2 = self.ui.lineEdit_4.text()  # Second dataset
        s = self.ui.lineEdit_5.text()  # Constants (X values)
        d1li = d1.split(",")  # Split the data by commas to convert it into a list
        d2li = d2.split(",")
        sli = s.split(",")
        listd1 = list(map(float, d1li))  # Convert the data to floats
        listd2 = list(map(float, d2li))
        lists = list(map(float, sli))
        plt.stackplot(lists, listd2, listd1, colors=["grey", "black"])  # Create a stack plot with two datasets
        plt.legend()  # Display legend for the plot
        plt.title("Stack Plot")  # Set the title for the plot
        plt.xlabel("Constants")  # Label for the X axis
        plt.ylabel("Variables")  # Label for the Y axis
        plt.show()  # Show the graph on the screen


    # Function to plot a pie chart
    def piey(self):
        p1 = self.ui.lineEdit_6.text()  # Pie slice labels
        p2 = self.ui.lineEdit_7.text()  # Pie slice percentages
        p1x = p1.split(",")  # Split the data by commas to convert it into a list
        p2x = p2.split(",")
        listp1 = list(p1x)  # List of labels
        listp2 = list(map(float, p2x))  # Convert percentages to floats
        plt.pie(listp2, labels=listp1, shadow=True, autopct="%1.1f%%")  # Plot the pie chart
        plt.title("Pie Chart")  # Set the title for the chart
        plt.show()  # Show the pie chart on the screen

   
    # Function to plot a bar chart
    def bar(self):
        # Get data for X and Y axes from user input
        barx1 = self.ui.lineEdit_8.text()  # First X-axis data
        barx2 = self.ui.lineEdit_10.text()  # Second X-axis data
        bary1 = self.ui.lineEdit_9.text()  # First Y-axis data
        bary2 = self.ui.lineEdit_11.text()  # Second Y-axis data
        barxisim = self.ui.lineEdit_12.text()  # Label for the first bar set
        baryisim = self.ui.lineEdit_13.text()  # Label for the second bar set
        bx1 = barx1.split(",")  # Split the data by commas to convert it into a list
        bx2 = barx2.split(",")
        by1 = bary1.split(",")
        by2 = bary2.split(",")
        lbx1 = list(map(float, bx1))  # Convert data to floats
        lbx2 = list(map(float, bx2))
        lby1 = list(map(float, by1))
        lby2 = list(map(float, by2))
        plt.bar(lbx1, lbx2, label=barxisim, width=.2)  # Plot the first bar chart
        plt.bar(lby1, lby2, label=baryisim, width=.2)  # Plot the second bar chart
        plt.xlabel("X Axis")  # Label for the X axis
        plt.ylabel("Y Axis")  # Label for the Y axis
        plt.title("Bar Chart")  # Set the title for the chart
        plt.legend()  # Display legend
        plt.show()  # Show the bar chart on the screen


    # Function to plot a histogram chart
    def hist(self):
        hx = self.ui.lineEdit_14.text()  # X-axis data for the histogram
        hy = self.ui.lineEdit_15.text()  # Y-axis data for the histogram

        hxs = hx.split(",")  # Split the data by commas to convert it into a list
        hys = hy.split(",")

        hxl = list(map(float, hxs))  # Convert X data to floats
        hyl = list(map(float, hys))  # Convert Y data to floats

        plt.hist(hxl, hyl, histtype="bar", rwidth=0.8)  # Plot the histogram
        plt.xlabel("X Axis")  # Label for the X axis
        plt.ylabel("Y Axis")  # Label for the Y axis
        plt.title("Histogram Chart")  # Set the title for the chart
        plt.show()  # Show the histogram on the screen

    
# Code to start the application
uyg = QApplication(sys.argv)  # Start the PyQt5 application
pen = analiz()  # Create an instance of the main window
pen.show()  # Show the main window
uyg.exec_()  # Execute the application's main loop
