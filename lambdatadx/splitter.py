def spltr(X):

    """
    Param is a date column in a pd.DataFrame
    Function will split dates ("MM/DD/YYYY")
    into multiple columns 
    """
    


    return X

# d = splitter(df)
# print(d)
if __name__ == "__main__":
     X = X.copy()
    X['Date'] = pandas.to_datetime(X['Date'], infer_datetime_format=True)
    X['Year'] = X['Date'].dt.year 
    X['Month'] = X['Date'].dt.month
    X['Day'] = X['Date'].dt.day
    X = X.drop(columns='Date')
    df = spltr(df)
    print(df.head())


