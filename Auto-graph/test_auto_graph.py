import pytest
import pandas
import numpy
import auto_graph_v2 as AG

def main():
    test_1()



def test_1():
    with open("nums.csv") as nums:

        df = pandas.read_csv(nums)
        df = df.to_numpy()

        df2 = AG.read_file("nums.csv")
        print(nums)

        #assert type(df2) == type(pandas.DataFrame)

main()
#pytest.main(["-v", "--tb=line", "-rN", __file__])