import pandas as pd
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


def indicator_name_2_code(df):
    print("Mapping Indicator name to code..")
    name_2_code = {}

    for _, row in df.iterrows():
        name_2_code[row["Indicator Name"]] = row["Indicator Code"]

    return name_2_code


if __name__=="__main__":
    ed_stats_data_path = r"C:\Users\aryam\OneDrive\Desktop\EdStatsData.csv"
    df = pd.read_csv(ed_stats_data_path)

    indicator_count = df["Indicator Code"].value_counts()
    filtered_indicators = indicator_count[indicator_count >= 230]

    print(type(filtered_indicators))

    drop_columns(df)

    df = pivot(df)

    print(f' after pivoting {df.shape}')

    for column in df.columns:
        if column not in filtered_indicators and not "Country Name":
            df.drop(column, inplace=True)


    temp_cols = df.columns.tolist()
    new_cols = temp_cols[-1:] + temp_cols[:-1]
    df = df[new_cols]
    print(f' after filtering {df.shape}')
    df = df.dropna(axis=1)
    print(f' after dropna {df.shape}')
    df.to_csv("pivot.csv")