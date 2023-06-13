#import required libraries

import pandas as pd, numpy as np, tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
from tkinter import messagebox

class GUI:

    def __init__(self):
        
        self.root = tk.Tk()

        self.root.title("Auto-Graph")
        self.root.geometry("800x600")
        self.root.configure(bg="#095256")

        self.header = tk.Label(self.root, text="Auto-Graph", font = ("Arial", 20), foreground="#86A873", bg="#087F8C", relief="ridge", borderwidth=5)
        self.header.pack(padx=20, pady= 20)

        self.step_1 = tk.Label(self.root, text="Step 1: Enter a file path with .csv or .xlsx:", font = ("Arial", 14), foreground="#86A873", bg="#095256", borderwidth=5, relief="ridge")
        self.step_1.pack(padx=20, pady= 20)

        #self.entry_bar = tk.Frame(self.root, background= "red", borderwidth = 1)
        #self.entry_bar.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 12), borderwidth=5, relief="ridge")
        self.entry.pack(padx=5, pady=5)
        #self.entry.grid(column=0, row=0, padx=2.5)

        #self.search_button = tk.Button(self.entry_bar, font=("Arial", 12), text="Search",command=self.get_filepath)
        #self.search_button.grid(column=1, row=0, padx=2.5)

        self.step_2 = tk.Label(self.root, text="Step 2: Press a button to create a graph.", font = ("Arial", 14), foreground="#86A873", bg="#095256", borderwidth=5, relief="ridge")
        self.step_2.pack(padx=20, pady= 20)

        self.graph_menu = tk.Frame(self.root, borderwidth=1, bg="#095256")
        self.graph_menu.columnconfigure(0, weight=1)
        self.graph_menu.columnconfigure(1, weight=1)
        self.graph_menu.columnconfigure(2, weight=1)
        self.graph_menu.columnconfigure(3, weight=1)
        self.graph_menu.pack()
# column=0, row=0, 

        self.pandas_button = tk.Button(self.graph_menu, text="Dataframe", font=("Arial", 8),command = lambda graph_method="pandas": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.pandas_button.grid(column=0, row=0, sticky="NEWS")
        
        self.linear_button = tk.Button(self.graph_menu, text="Linear", font=("Arial", 8),command = lambda graph_method="linear": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.linear_button.grid(column=1, row=0, sticky="NEWS")

        self.hist_button = tk.Button(self.graph_menu, text="Histogram", font=("Arial", 8),command = lambda graph_method="hist": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.hist_button.grid(column=2, row=0, sticky="NEWS")

        self.polar_button = tk.Button(self.graph_menu, text="Polar", font=("Arial", 8),command = lambda graph_method="polar": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.polar_button.grid(column=3, row=0, sticky="NEWS")

        self.pie_button = tk.Button(self.graph_menu, text="Pie Chart", font=("Arial", 8),command = lambda graph_method="pie": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.pie_button.grid(column=0, row=1, sticky="NEWS")

        self.phase_button = tk.Button(self.graph_menu, text="Phase Spectrum", font=("Arial", 8),command = lambda graph_method="phase": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.phase_button.grid(column=1, row=1, sticky="NEWS")

        self.contour_button = tk.Button(self.graph_menu, text="Contour", font=("Arial", 8),command = lambda graph_method="contour": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.contour_button.grid(column=2, row=1, sticky="NEWS")

        self.hexbin_button = tk.Button(self.graph_menu, text="Hexbin", font=("Arial", 8), command=lambda graph_method="hex": self.get_filepath(graph_method), bg="#087F8C", relief="raised", borderwidth=5)
        self.hexbin_button.grid(column=3, row=1, sticky="NEWS")
        
        self.credits = tk.Button(text="Credits", font=("Arial", 10), command=self.show_credits, foreground="black", bg="#087F8C", relief="raised", borderwidth=5)
        self.credits.pack(padx=10, pady=10)

        self.tip = tk.Label(self.root, text="Tip: Use double forward slashes in filepath, or else python cannot find the file.", font = ("Arial", 14), foreground="#86A873", bg="#095256", borderwidth=5, relief="ridge")
        self.tip.pack(padx=20, pady= 20)

        self.copyright = tk.Label(self.root, text="Copyright Zach Newby 2023", font = ("Arial", 10), foreground="#86A873", bg="#095256")
        self.copyright.place(x=20, y=580)

        self.root.mainloop()


    def get_filepath(self, graph_method):
        try:
            filepath = self.entry.get()
            df = read_file(filepath)
            display_file(df, method=graph_method)
            #graph_file(df)

        except FileNotFoundError or PermissionError:
            messagebox.showinfo(title="Error", message="Invalid file, please check name or path and re-enter")
        
        except ValueError:
            messagebox.showinfo(title="Error", message="Invalid Values, select a different method.")
        
        except AttributeError:
            messagebox.showinfo(title="Error", message="Enter a filepath.")

    def show_credits(self):
        messagebox.showinfo(title="Credits", message="""
            Coding: Zach Newby
            Used Libraries:
            pandas, 
            matplotlib,
            tkinter,
            numpy
            
            Thanks to: God,
        Users Jack MarrekNožka, Charles Anderson, & rjmunro on Stack overflow,
        Keith Gali, Derek Banas, & NeuralNine on Youtube,
        Microsoft,
        StackHowto,
        Coolors,
        Tkdocs,
        the creators of the used libraries,
        and CSE 111 Teacher William Clemments""")


def read_file(filepath = ""):
    """
    Accepts a .csv or .xlsx file and converts it to a Pandas dataframe

    Input: file path as str

    Output: Pandas dataframe
    """
    if ".csv" in filepath:
        dataframe = pd.read_csv(filepath)
        return dataframe
    
    elif ".xlsx" in filepath:
        dataframe = pd.read_excel(filepath)
        return dataframe


def display_file(dataframe, method = "linear"):
    """Display methods:
    * pandas data frame (default - if this will be used in the method is unavailible)
    * line graph
    * histogram
    * pie - (first row/coumn only)
    * polar plot
    * Phase Spectrum
    * Contour
    * Hexbin
    """
    if method == "pandas":
        messagebox.showinfo(title="Error", message=f"{dataframe.head(5), dataframe.sample()}")
        #print(dataframe)

    elif "linear" == method:
        array = dataframe.to_numpy()

        plt.plot(array)
        plt.show()
    
    elif "hist" == method:
        array = dataframe.to_numpy()

        plt.hist(array)
        plt.show()

    elif "pie" == method:
        array = dataframe.to_numpy()

        plt.pie(array[0])
        plt.show()

    elif "polar" == method:
        array = dataframe.to_numpy()

        plt.polar(array)
        plt.show()

    elif "phase" == method:
        array = dataframe.to_numpy()

        plt.phase_spectrum(array)
        plt.show()

    elif "contour" == method:
        array = dataframe.to_numpy()

        plt.contour(array)
        plt.show()
    
    elif "hex" == method:
        array = dataframe.to_numpy()

        plt.hexbin(array[:,0], array[:,1])
        plt.show()
    
    else:
        pass



if __name__ == "__main__":
    GUI()
