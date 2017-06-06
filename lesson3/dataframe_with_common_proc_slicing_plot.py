import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir = "data"):
    """ Return CSV file path given ticker symbol """
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """ Read stock data (adjusted close) for givem symbols from CSV file """
    df = pd.DataFrame(index=dates)
    #if 'SPY' not in symbols: # add SPY for reference, if absent
    #    symbols.insert(0, 'SPY')
    counter = 0
    for symbol in symbols:
        counter = counter + 1
        df_temp = pd.read_csv(symbol_to_path(symbol),
                                    index_col="Date",
                                    parse_dates=True,
                                    usecols=['Date', 'Adj Close'],
                                    na_values=['nan']
                                    )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp) # use default how = 'left'
        if counter == 1:
            df = df.dropna(subset=[symbol])
            
    return df

def plot_data(df, title = "Stock prices"):
    ''' Plot stock prices '''
    ax = df.plot(title = title, fontsize = 5)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    df = df.ix[start_index : end_index, columns]
    plot_data(df, title = "Selected data")    
    
def normalize_data(df):
    """ Normalize stock prices using the first row of the dataframe """
    return df / df.ix[0, :]

def test_run():
    start_date = '2017-04-01'
    end_date = '2017-05-26'

    dates = pd.date_range(start_date, end_date)

    #df1 = df1.join(dfHCN) # left join by default
    #df1 = df1.join(dfHCN, how='inner')

    # read in more stocks
    symbols = ['HCN', 'AAPL', 'HCP']
    df = get_data(symbols, dates)

    # Slice by row range (dates) using DataFrame.ix[] selector
    # df.ix['2010-01-01':'2010-01-31']

    # Slice by column
    # df['GOOG'] # a single label selects a single column
    # df[['IBM', 'GLD']] # a list of labels selects multiple columns

    # Slice by row and column
    # df.ix['2010-01-01':'2010-01-31', ['IBM', 'GLD']]

    #Drop NaN Values
    #df1 = df1.dropna()

    #plot_selected(df, ['AAPL', 'HCP'], '2010-01-01', '2018-01-01')
    plot_data(normalize_data(df))
    #print(df)
    

if __name__ == "__main__":
    test_run()
