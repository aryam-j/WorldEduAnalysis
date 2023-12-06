import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from tqdm import tqdm



def drop_columns(df, to_remove=[]):
    print("Dropping Columns...")
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.drop("Unnamed: 69", axis=1, inplace=True)
    df.drop("Indicator Name", axis=1, inplace=True)
    df.drop("Country Code", axis=1, inplace=True)

    for col in df.columns:
        try:
            if int(col) > 2017:
                df.drop(col, axis=1, inplace=True)
        except ValueError:
            continue

    for col in to_remove:
        df.drop(col, axis=1, inplace=True)



def pivot(df):
    pivots = []
    print("Pivotting...")
    for col in tqdm(df.columns):
        if col.isnumeric():
            pivot_df = df.pivot(index=['Country Name'], columns="Indicator Code", values=col)
            pivot_df["Year"] = col
            pivots.append(pivot_df)

    return pd.concat(pivots)


def indicator_code_2_name(df):
    print("Mapping Indicator name to code..")
    name_2_code = {}

    for _, row in df.iterrows():
        name_2_code[row["Indicator Code"]] = row["Indicator Name"]

    return name_2_code



if __name__=="__main__":

    ### LOADING THE DATA ###
    ed_stats_data_path = r"C:\Users\aryam\OneDrive\Desktop\EdStatsData.csv"
    df = pd.read_csv(ed_stats_data_path)

    ### COUNTING THE FREQUENCY OF INDICATORS ###
    indicator_count = df["Indicator Code"].value_counts()

    ### CREATING CODE TO NAME DICTIONARY ###
    indicator_dict = indicator_code_2_name(df)

    ### CREATING A LIST OF INDICATORS TO FILTER ###
    filtered_indicators = indicator_count[indicator_count < 229] #30
    filtered_indicators = filtered_indicators.index.to_list()

    ### REMOVING UNNECESSARY COLUMNS ###
    drop_columns(df)

    ### PIVOTING ###
    df = pivot(df)
    print(f' after pivoting {df.shape}')

    ### FILTERING INDICATORS ###
    print("filtering")
    df.drop(columns=filtered_indicators, inplace=True, axis=1)

    ### CHANGING "YEAR" COLUMN POSITION ###
    temp_cols = df.columns.tolist()
    new_cols = temp_cols[-1:] + temp_cols[:-1]
    df = df[new_cols]

    ### DROPPING ROWS WITH NA VALUE ###
    print(f' after filtering {df.shape}')
    df = df.dropna()
    print(f' after dropna {df.shape}')

    ### FILTERING CODE TO INDICATOR NAME DICTIONARY ###
    keys_to_delete = []
    for indicator_key in indicator_dict.keys():
        if indicator_key not in df.columns:
            keys_to_delete.append(indicator_key)

    for key in keys_to_delete:
        del indicator_dict[key]
    print(indicator_dict)

    ### CREATING A NEW FILE ###
    df.to_csv("pivot.csv")

    ### CREATING HEATMAP OF CORRELATIONS ###

    df = df.drop(columns="Year")
    # plt.figure(figsize=(15, 10))
    # sb.heatmap(df.corr(), cmap='coolwarm')
    #
    # plt.show()
    correlation_matrix = df.corr()
    for i in range(len(correlation_matrix.columns)):
        for j in range(i):
            # Print variables with high correlation
            if abs(correlation_matrix.iloc[i, j]) > 0.7 or abs(correlation_matrix.iloc[i, j]) < - 0.7:
                print(f'{indicator_dict[correlation_matrix.columns[i]]} || {indicator_dict[correlation_matrix.columns[j]]} --> {correlation_matrix.iloc[i, j]}')





# if __name__=="__main__":
#     ed_stats_data_path = r"C:\Users\aryam\OneDrive\Desktop\EdStatsData.csv"
#     df = pd.read_csv(ed_stats_data_path)
#
#     indicator_count = df["Indicator Code"].value_counts()
#     drop_columns(df)
#
#     df = pivot(df)
#     print(f' after pivoting {df.shape}')
#
#     for i in range(100, 240, 1):
#         filtered_indicators = indicator_count[indicator_count < i].index.tolist()
#
#         existing_columns = [col for col in filtered_indicators if col in df.columns]
#         df_filtered = df.drop(columns=existing_columns, axis=1)
#         print(f' after filtering {df_filtered.shape}')
#
#         df_filtered = df_filtered.dropna()
#         print(f' after dropna {i} {df_filtered.shape}')