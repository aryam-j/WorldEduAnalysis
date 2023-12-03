import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# (886930, 69) without dropna
### LOADED THE DATASET ###

# ed_stats_data_path = r"C:\Users\aryam\OneDrive\Desktop\EDA\EdStatsData.csv"
# print("step 1")
# df = pd.read_csv(ed_stats_data_path)
# print("step 2")

### DELETED THE ROWS THAT HAD LESS THAN 5 VALUES ###

# df.dropna(thresh=5, inplace=True)

### CREATED A NEW CLEANER DATASET ###

# df.to_csv(r"C:\Users\aryam\OneDrive\Desktop\EdStatsData.csv")
# print('DataFrame is written to Excel File successfully.')

### LOADING NEW DATA ###

ed_stats_data_path = r"C:\Users\aryam\OneDrive\Desktop\EdStatsData.csv"
df = pd.read_csv(ed_stats_data_path)

### FINDING MOST USED INDICATOR ###

indicator_count = df["Indicator Name"].value_counts()
filtered_indicators = indicator_count[indicator_count >= 200]

### SAVING INDICATOR DATA IN A TXT FILE ###

# file_path = r"C:\Users\aryam\OneDrive\Desktop\indicators.txt"
# with open(file_path, 'w') as file:
#     file.write(indicators.to_string())

### FINDING UNIQUE COUNTRY CODE ###

# country_names = df["Country Name"].value_counts()

### SAVING COUNTRY NAMES IN A TXT FILE ###

# file_path = r"C:\Users\aryam\OneDrive\Desktop\country name.txt"
# with open(file_path, 'w') as file:
#     file.write(country_names.to_string())

### CREATING DICTIONARY FOR INDICATORS ###

# gdp_values = {}
# vocational = {}
#
# for index, row in df.iterrows():
#     if row["Indicator Name"] == "GDP per capita (current US$)" and row["Country Name"] == "World":
#         for column_name in df.columns:
#             if column_name.isdigit() and int(column_name) >= 1970 and int(column_name) <= 2017:
#                 gdp_values[column_name] = row[column_name]
#     if row["Indicator Code"] == "UIS.GTVP.3.V" and row["Country Name"] == "World":
#         for column_name in df.columns:
#             if column_name.isdigit() and int(column_name) >= 1970 and int(column_name) <= 2017:
#                 vocational[column_name] = row[column_name]

indicators = {}

for index, row in df.iterrows():
    if row["Indicator Name"] in filtered_indicators:
        for column_name in df.columns:
            if column_name.isdigit() and int(column_name) >= 1970 and int(column_name) <= 2017:
                year = int(column_name)
                country = row["Country Name"]
                indicator_name = row["Indicator Name"]
                if year not in indicators:
                    indicators[year] = {}
                # indicators[year] = row[column_name]
                if country not in indicators[year]:
                    indicators[year][country] = {}
                # indicators[year][country] = row["Indicator Name"]
                if row["Indicator Name"] not in indicators[year][country]:
                    indicators[year][country][indicator_name] = row[column_name]
                indicators[year][country][indicator_name] = row[column_name]

print(indicators)


# for key in indicators:
