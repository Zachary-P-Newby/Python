import pytest
import pandas as pd, numpy as np, tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt

def main():
    test_1()
    pass

def test_1():
    with open("nums.csv") as nums:
        df = pd.read_csv(nums)
    
    assert type(df["alpha"]) == type(df.iloc[:,0])
    ex = df.iloc[:,0]
    assert ex == df["alpha"]

pytest.main(["-v", "--tb=line", "-rN", __file__])