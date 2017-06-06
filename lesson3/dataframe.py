import pandas as pd
import os

def symbol_to_path(symbol, base_dir = "data"):
    """ Return CSV file path given ticker symbol """
    return os.path.join(base_dir, "{}.csv".format(str(symbol))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for givem symbols from CSV file """
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols: # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol),
                                    index_col="Date",
                                    parse_dates=True,
                                    usecols=['Date', 'Adj Close'],
                                    na_values=['nan']
                                    )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp) # use default how = 'left'

    return df.
    

def test_run():
    start_date = '2017-04-20'
    end_date = '2017-04-26'

    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    
    # parse into date obj
    dfHCN = pd.read_csv("data/HCN.csv", index_col="Date",
                                    parse_dates=True,
                                    usecols=['Date', 'Adj Close'],
                                    na_values=['nan']
                                    )
    dfHCN = dfHCN.rename(columns={'Adj Close': 'HCN'})
    
    #df1 = df1.join(dfHCN) # left join by default
    #df1 = df1.join(dfHCN, how='inner')

    # read in more stocks
    symbols = ['AAPL', 'HCP']
                        
    
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col="Date",
                                    parse_dates=True,
                                    usecols=['Date', 'Adj Close'],
                                    na_values=['nan']
                                    )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp) # use default how = 'left'
    
    #Drop NaN Values
    #df1 = df1.dropna()

    print(df1)
    
    """
    df = pd.read_csv("data/HCN.csv")
    print (df.head())
    print ("tail: ")
    print (df.tail())
    print (df[5:14])
    """

if __name__ == "__main__":
    test_run()
