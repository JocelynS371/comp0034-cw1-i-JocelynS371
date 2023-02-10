import matplotlib.pyplot as plt
import pandas as pd


def main():
    df=pd.read_csv(data_set_prepared.csv)
    column_label=df.columns
    print(df.shape)
main()