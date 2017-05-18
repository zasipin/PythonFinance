import pandas as pd

def test_run():
    df = pd.read_csv("data/HCN.csv")
    print (df.head())
    print ("tail: ")
    print (df.tail())
    print (df[5:14])

if __name__ == "__main__":
    test_run()
