import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/HCP.csv")
    print (df['Adj Close'])
    #df['Adj Close'].plot()
    df[['Close', 'Adj Close']].plot()
    plt.show() # must be called to show plots

if __name__ == "__main__":
    test_run()
