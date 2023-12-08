import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import preprocessing


if __name__=="__main__":
    df = pd.read_csv("pivot.csv")
    # COL_1, COL_2, COL_3 = "SE.ADT.LITR.ZS", "NY.GDP.PCAP.PP.KD", "Country Name" ### Literacy rate and GDP PPP
    # COL_1, COL_2, COL_3 = "UIS.LPP.AG15T99", "SE.ADT.LITR.MA.ZS", "Country Name" ### male literacy and female literacy
    COL_1, COL_2, COL_3 = "UIS.LPP.AG15T99", "SE.ADT.LITR.MA.ZS", "Country Name"
    new_df = df[[COL_1, COL_2, COL_3]]
    # new_df = new_df[new_df[COL_2] < 500]
    # new_df = new_df[new_df[COL_1] > 80]

    print(
    new_df.dropna(inplace=True))

    print(new_df[[COL_1, COL_2]].corr(method='pearson', min_periods=1000))
    print(new_df.describe())
    sb.scatterplot(y=new_df[COL_1], x=new_df[COL_2])

    # label_offset = 0.5  # Change this offset value as needed
    # for idx, row in new_df.iterrows():
    #     plt.text(row[COL_2] + label_offset, row[COL_1] + label_offset, row[COL_3])
    #
    # plt.xlabel(COL_2)
    # plt.ylabel(COL_1)
    plt.show()

    # for idx, row in new_df.iterrows():
    #     plt.text(row[COL_1], row[COL_2], row[COL_3])

    # plt.show()