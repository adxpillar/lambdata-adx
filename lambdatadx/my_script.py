import pandas

from lambdatadx.splitter import spltr

print("Here is your dataframe")

df = pandas.DataFrame({"Date": ['10/04/1990','13/06/1991','4/05/1992'],
                "Model": ['D','S','B']})
print(df.head())

print(spltr(df))

    