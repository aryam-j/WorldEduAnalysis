import pandas as pd
import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing


def get_countries_with_income(income):
    country_df = pd.read_csv('EdStatsCountry.csv')
    country_df = country_df[country_df['Currency Unit'].notna()]
    return set(country_df[country_df["Income Group"].isin(income)]["Table Name"].to_list())

# country_df = pd.read_csv('EdStatsCountry.csv')
country_list = ["United States",
    "China",
    "India",
    "Brazil",
    "Russia",
    "Nigeria",
    "Japan",
    "Germany",
    "Indonesia",
    "Mexico",
    "Egypt",
    "South Africa",
    "Australia",
    "Canada",
    "Sweden"]

if __name__=="__main__":
    df = pd.read_csv("pivot.csv")
    print(df.index)

    #
    # new_df = df[["SE.ADT.LITR.ZS", "NY.GDP.PCAP.PP.KD", "Country Name"]]
    # print(new_df["SE.ADT.LITR.ZS"].corr(new_df["NY.GDP.PCAP.PP.KD"]))
    # sns.scatterplot(x="SE.ADT.LITR.ZS", y="NY.GDP.PCAP.PP.KD", data=new_df)
    # plt.xlabel("Literacy Rate")
    # plt.ylabel("GDP PPP")
    # plt.title("Literacy rate and GDP PPP")
    # plt.show()

    # COL_1, COL_2, COL_3 = "SE.PRM.ENRR", "SE.PRM.CMPT.ZS", "Country Name" ## "Gross enrolment ratio, primary, both sexes (%)" and "Primary completion rate, both sexes (%)"
    # new_df = df[["SE.PRM.ENRR", "SE.PRM.CMPT.ZS", "Country Name"]]
    # sns.scatterplot(x="SE.PRM.ENRR", y="SE.PRM.CMPT.ZS", data=new_df)
    #
    # # for i, country in enumerate(new_df["Country Name"]):
    # #     if country in country_list:
    # #         plt.text(new_df["SE.PRM.ENRR"][i] + 0.2, new_df["SE.PRM.CMPT.ZS"][i] + 0.2, country)
    #
    # plt.xlabel("SE.PRM.ENRR")
    # plt.ylabel("SE.PRM.CMPT.ZS")
    # plt.title("Gross enrolment ratio, primary, both sexes (%) and Primary completion rate, both sexes (%)")
    # plt.show()



    # COL_1, COL_2, COL_3 = "SE.PRM.TCHR", "SE.PRM.ENRL.TC.ZS", "Country Name" ##"Teachers in primary education, both sexes (number)" and "Pupil-teacher ratio in primary education (headcount basis)"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # plt.xlabel("Literacy Rate")
    # plt.ylabel("GDP PPP")
    # plt.title("Literacy rate and GDP PPP")
    # plt.show()

    # 1111111111111111111
    COL_1, COL_2, COL_3 = "SE.SEC.ENRL.VO.ZS", "Year", "Country Name"
    india_yearly = df.loc[df["Country Name"] == "India",  [COL_2, COL_1]].dropna()
    plt.figure(figsize=(100, 6))
    sns.barplot(x=COL_2, y=COL_1, data=india_yearly)
    plt.xlabel("%")
    plt.ylabel("Year")
    plt.title("Year wise stats of vocational enrollment")
    plt.show()

# # 222222222222222222222222222222222222222222222222222
#     COL_1, COL_2, COL_3 = "SE.PRM.REPT.ZS", "SE.PRM.PRSL.ZS", "Country Name" ##"Percentage of repeaters in primary education, all grades, both sexes (%)" and "Survival rate to the last grade of primary education, both sexes (%)"
#     new_df = df[[COL_1, COL_2, COL_3]]
#     sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
#     print(new_df["SE.PRM.REPT.ZS"].corr(new_df["SE.PRM.PRSL.ZS"]))
#     plt.xlabel("Percentage of repeaters in primary education")
#     plt.ylabel("Survival rate to the last grade of primary education")
#     plt.title("percentage of repeaters and survival rate to last grade of primary education")
#     plt.show()

    # 33333333333333333333333333333333333333333333333333
    # COL_1, COL_2, COL_3 = "SE.PRM.ENRR.FE", "Year", "Country Name" ##"Gross enrolment ratio, primary, female (%)"
    # india_yearly = df.loc[df["Country Name"] == "India",  [COL_2, COL_1]].dropna()
    # print(india_yearly)
    # sns.barplot(x=COL_2, y=COL_1, data=india_yearly)
    # plt.xlabel("Year")
    # plt.ylabel("%")
    # plt.title("Number of female enrollment in primary education in India year wise")
    # plt.show()

    #4444444444444444444444444444444444444444444444444
    # COL_1, COL_2, COL_3 = "UIS.NERT.1", "SH.DYN.MORT", "Country Name" ##"Total net enrolment rate, primary, both sexes (%)" and "Mortality rate, under-5 (per 1,000)"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df["UIS.NERT.1"].corr(new_df["SH.DYN.MORT"]))
    # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()
    #5555555555555555555555555555555555555555555555555
    # COL_1, COL_2, COL_3 = "SE.SEC.ENRR", "Year", "Country Name"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # india_yearly = df.loc[df["Country Name"] == "India",  [COL_2, COL_1]].dropna()
    # print(india_yearly)
    # sns.barplot(x=COL_2, y=COL_1, data=india_yearly)
    # plt.xlabel("Year")
    # plt.ylabel("%")
    # plt.title("Year wise Gross enrolment ratio, primary, both sexes (%) of India")
    # plt.show()

    #6666666666666666666666666666666666666666666666666
    # COL_1, COL_2, COL_3 = "UIS.E.1.PR", "UIS.E.1.PU", "Year"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # new_df = new_df.melt(value_vars=[COL_1, COL_2], id_vars=[COL_3]).dropna()
    # print(new_df)
    # sns.barplot(x="Year", y="value", data=new_df, hue="variable")
    # plt.xlabel("Year")
    # plt.ylabel("%")
    # plt.title("Private and public enrollment in India")
    # plt.show()


    ######## BARCHART ########
    #7777777777777777777777777777777777777777777777777
    # enrollment_df = df[df["Country Name"].isin({"India", "Norway", "Brazil", "Japan"})]
    # #
    # COL_1, COL_2 = "SE.XPD.TOTL.GB.ZS", "Year"
    # enrollment_df = enrollment_df[[COL_1, COL_2, "Country Name"]]
    # enrollment_df.dropna(inplace=True)
    #
    # enrollment_df = enrollment_df.pivot(index="Year", columns="Country Name", values=COL_1)[["India", "Norway", "Japan", "Brazil"]].dropna()
    # enrollment_df = enrollment_df.melt(value_vars=["India", "Norway", "Japan", "Brazil"], ignore_index=False)
    #
    # sns.set(style="whitegrid")
    # sns.barplot(x=enrollment_df.index, y='value', data=enrollment_df, hue='Country Name')
    # plt.title('')
    # plt.xlabel('Year')
    # plt.ylabel('% Spent on Edu')
    # plt.legend(title='Countries')
    # plt.show()

    ######## HISTOGRAM ########
    #888888888888888888888888888888888888888888888888
    # plt.hist(df["SE.PRM.ENRL.TC.ZS"])
    # plt.xlabel("Pupil-teacher ratio")
    # plt.ylabel("Number of occurrence")
    # plt.title("Pupil-teacher ratio in primary education (headcount basis)")
    # plt.show()

    ######## BOX PLOT ########
    #999999999999999999999999999999999999999999999999
    # COL_1, COL_2, COL_3 = "SE.PRM.ENRL.FE.ZS", "SE.SEC.ENRL.FE.ZS", "SE.TER.ENRL.FE.ZS"
    # new_df = df[[COL_1, COL_2, COL_3, "Year", "Country Name"]]
    # new_df = new_df[new_df["Year"] >= 2014]
    #
    # new_df.dropna(inplace=True)
    #
    # data = [new_df[COL_1].values, new_df[COL_2].values, new_df[COL_3].values]
    # plt.figure(figsize=(10, 6))
    # plt.boxplot(data, labels=['Primary', 'Secondary', 'Tertiary'])
    # plt.xlabel('Education Levels')
    # plt.ylabel('Enrollment Rate')
    # plt.title("Gross enrolment ratio, primary, both sexes (%) vs Gross enrolment ratio, secondary, both sexes (%)")
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()

    ## 10101010101100110101001010110010101010101010101010
    # COL_1, COL_2, COL_3 = "IT.NET.USER.P2", "NY.GDP.PCAP.CD", "Country Name" ##Internet users per 100 people and GDP per capita
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()

    ## 11111111111111111111111111111111111111111111111111

    # COL_1, COL_2, COL_3 = "NY.GDP.PCAP.CD", "SE.TER.ENRR", "Country Name" ##GDP per capita and Gross Enrolment Ratio in Tertiary Education
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()


    ##1212121212121212121212121212121212121212121212121212
    # COL_1, COL_2 = "SE.SEC.TCHR", "SE.SEC.ENRL" ##Enrolment in secondary education, both sexes, and teachers in secondary education, both sexes
    # new_df = df[[COL_1, COL_2]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()


    ##1313131313131313131313131313131313131313131313131313
    # COL_1, COL_2, COL_3 = "SE.PRE.ENRL","SP.PRE.TOTL.IN", "Country Name" ##Enrolment in pre-primary education and Population of the official age for pre-primary education, both sexes
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()

    ##1414141414141414141414141414141414141414141414141414
    # COL_1, COL_2, COL_3 = "SE.PRE.ENRL","SP.PRE.TOTL.IN", "Country Name" ##Enrolment in pre-primary education and Population of the official age for pre-primary education, both sexes
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()

    ##15151515151515155155151515151515151515155511515151515
    # COL_1, COL_2, COL_3 = "SE.SEC.ENRR.UP","NY.GDP.PCAP.CD", "Country Name" ## "Gross Enrolment Ratio, Upper Secondary, both sexes, and GDP per capita, current US$"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()

    ##1616161616161616161616161616161611616161661616161611616

    # COL_1, COL_2, COL_3 = "SP.TER.TOTL.IN","SE.TER.TCHR", "Country Name" ## "Population of the official age for tertiary education, both sexes, and Teachers in tertiary education, both sexes"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()

    ## 171717171717171717171717171717117171717711717711717171

    # COL_1, COL_2, COL_3 = "SE.PRM.TENR","SE.PRM.REPT.ZS", "Country Name" ## Comparison between India and China Unemployed
    # new_df = df[[COL_1, COL_2, COL_3]]
    # sns.scatterplot(x=COL_1, y=COL_2, data=new_df)
    # print(new_df[COL_1].corr(new_df[COL_2]))
    # # plt.xlabel("Total net enrolment rate, primary, both sexes (%")
    # # plt.ylabel("Mortality rate, under-5 (per 1,000)")
    # # plt.title("Total net enrolment rate, primary, both sexes (%) and Mortality rate, under-5 (per 1,000)")
    # plt.show()

    ## 181818181818181818818181818181818181818181881818181818

    # COL_1, COL_2, COL_3 = "SL.UEM.TOTL.ZS", "Year", "Country Name" ##"Comparison between India and China government's expenditure on education
    # # india_yearly = df.loc[df["Country Name"] == "India",  [COL_2, COL_1]].dropna()
    # india_yearly = df.loc[df["Country Name"].isin(["India", "China"]), [COL_2, COL_1, COL_3]].dropna()
    # print(india_yearly)
    # sns.barplot(x=COL_2, y=COL_1, data=india_yearly, hue="Country Name")
    # plt.xlabel("Year")
    # plt.ylabel("%")
    # plt.title("Number of female enrollment in primary education in India year wise")
    # plt.show()

    ## 19191919191919191911919191911919191919191919919191919191
    # COL_1, COL_2, COL_3 = "UIS.LR.AG25T64", "Year", "Country Name" ##"Gross enrolment ratio, primary, female (%)"
    # # india_yearly = df.loc[df["Country Name"] == "India",  [COL_2, COL_1]].dropna()
    # india_yearly = df.loc[df["Country Name"].isin(["India", "China"]), [COL_2, COL_1, COL_3]].dropna()
    # print(india_yearly)
    # sns.barplot(x=COL_2, y=COL_1, data=india_yearly, hue="Country Name")
    # plt.xlabel("Year")
    # plt.ylabel("%")
    # plt.title("Number of female enrollment in primary education in India year wise")
    # plt.show()