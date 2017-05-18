import pandas as pd

def get_max_close(symbol):
    """ return th maximum closing value for stock indicated by symbol
    Note: data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) # read in data
    return df['Close'].max() # compute and return max

def get_mean_volume(symbol):
    """ return th maximum closing value for stock indicated by symbol
    Note: data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol)) # read in data
    return df['Volume'].mean() # compute and return max


def test_run():
    for symbol in ['HCN', 'HCP']:
        print ("Max close")
        print (symbol, get_max_close(symbol))

if __name__ == "__main__":
    test_run()
        
    
