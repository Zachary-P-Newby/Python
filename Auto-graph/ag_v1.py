#import required libraries

import pandas as pd, numpy as np, tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    #open window w/ tkinter
    #ask for file_funct
    raw_file = get_file()
    raw_data = read_file(raw_file)
    
    #display file
    display_file(raw_data)

    

#____________________________________________________________________________

#ask for file
def get_file():
    """
    Asks user for file path and returns it as a str. May get rid of.
    """

    filepath = input("Please enter a file path: ")
    #filepath = "accidents.csv"

    return filepath

#____________________________________________________________________________

#file reader
def read_file(filepath = ""):
    """
    Accepts a .csv or .xlsx file and converts it to a Pandas dataframe

    Input: file path as str

    Output: Pandas dataframe
    """

    try:
        if ".csv" in filepath:
            dataframe = pd.read_csv(filepath)
    
        elif ".xlsx" in filepath:
            dataframe = pd.read_excel(filepath)
    
    except (FileNotFoundError, PermissionError) as error:
        print(f"{error} Check the path or permissions of desired the file.")

    return dataframe

#____________________________________________________________________________

def display_file(dataframe):
    #choose display method
    print("""Display methods:
    * pandas data frame (default - if this will be used in the method is unavailible)
    * line graph
    * histogram
    * pie - (first row/coumn only)
    * polar plot
    * Phase Spectrum
    * Angle Spectrum
    * Contour
    * Hexbin
    * Advanced - (Create figure, user will define axes and inputs)
    """)

    method = input("Enter method: ").lower()

    if "advanced" in method:
        #advanced_plot(dataframe)
        pass
    
    if "line" in method:
        array = dataframe.to_numpy()

        plt.plot(array)
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()
    
    elif "hist" in method:
        array = dataframe.to_numpy()

        plt.hist(array)
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()

    elif "pie" in method:
        array = dataframe.to_numpy()

        plt.pie(array[0])
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()

    elif "polar" in method:
        array = dataframe.to_numpy()

        plt.polar(array)
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()

    elif "phase" in method:
        array = dataframe.to_numpy()

        plt.phase_spectrum(array)
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()
    
    elif "angle" in method:
        array = dataframe.to_numpy()

        try:
            plt.angle_spectrum(array)
            save = input("Save plot(Y or N)? ").upper()
            if "Y" in save:
                plt.savefig("plot.png")
            plt.show()
        except ValueError:
            print("Try again with a different file, the values were invalid.")

    elif "contour" in method:
        array = dataframe.to_numpy()

        plt.contour(array)
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()
    
    elif "hex" in method:
        array = dataframe.to_numpy()

        plt.hexbin(array[:,0], array[:,1])
        save = input("Save plot(Y or N)? ").upper()
        if "Y" in save:
            plt.savefig("plot.png")
        plt.show()
    
    else:
        print(dataframe)

    

#____________________________________________________________________________
if __name__ == "__main__":
    main()