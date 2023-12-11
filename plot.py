import pandas as pd
import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing


def get_countries_with_income(income):
    country_df = pd.read_csv('EdStatsCountry.csv')
    country_df = country_df[country_df['Currency Unit'].notna()]
    return set(country_df[country_df["Income Group"].isin(income)]["Table Name"].to_list())

country_df = pd.read_csv('EdStatsCountry.csv')


if __name__=="__main__":
    df = pd.read_csv("pivot.csv")


    new_df = df[["SE.ADT.LITR.ZS", "NY.GDP.PCAP.PP.KD", "Country Name"]]

    sns.scatterplot(x="SE.ADT.LITR.ZS", y="NY.GDP.PCAP.PP.KD", data=new_df)
    plt.xlabel("Literacy Rate")
    plt.ylabel("GDP PPP")
    plt.title("Literacy rate and GDP PPP")
    plt.show()

# COL_1, COL_2, COL_3 = "UIS.LPP.AG15T99", "SE.ADT.LITR.MA.ZS", "Country Name" ###
    new_df1 = df[["UIS.LPP.AG15T99", "SE.ADT.LITR.MA.ZS"]]

    sns.scatterplot(x="UIS.LPP.AG15T99", y="SE.ADT.LITR.MA.ZS", data=new_df1)
    plt.xlabel("Literacy Rate")
    plt.ylabel("GDP PPP")
    plt.title("male literacy and female literacy")
    plt.show()



    # COL_1, COL_2, COL_3 = "SE.PRM.ENRR", "SE.PRM.CMPT.ZS", "Country Name" ## "Gross enrolment ratio, primary, both sexes (%)" and "Primary completion rate, both sexes (%)"
    # COL_1, COL_2, COL_3 = "SE.PRM.TCHR", "SE.PRM.ENRL.TC.ZS", "Country Name" ##"Teachers in primary education, both sexes (number)" and "Pupil-teacher ratio in primary education (headcount basis)"
    # COL_1, COL_2, COL_3 = "SE.SEC.ENRL.VO.ZS", "UIS.GTVP.23.GPV", "Country Name" ##"Percentage of students in secondary education enrolled in vocational programmes, both sexes (%)" and "Percentage of students in secondary education enrolled in general programmes, both sexes (%)"
    # COL_1, COL_2, COL_3 = "SE.PRM.REPT.ZS", "SE.PRM.PRSL.ZS", "Country Name" ##"Percentage of repeaters in primary education, all grades, both sexes (%)" and "Survival rate to the last grade of primary education, both sexes (%)"
    # COL_1, COL_2, COL_3 = "SE.PRM.ENRR.FE", "SE.PRM.ENRR.MA", "Country Name" ##"Gross enrolment ratio, primary, female (%)" and "Gross enrolment ratio, primary, male (%)"


    # COL_1, COL_2, COL_3 = "UIS.NERT.1", "SH.DYN.MORT", "Country Name" ##"Total net enrolment rate, primary, both sexes (%)" and "Mortality rate, under-5 (per 1,000)"
    # COL_1, COL_2, COL_3 = "SE.PRM.ENRR", "SE.SEC.ENRR", "Country Name" ## Scatter Plot "Gross enrolment ratio, primary, both sexes (%)" vs "Gross enrolment ratio, secondary, both sexes (%)"
    # COL_1, COL_2, COL_3 = "UIS.E.1.PR", "SE.SEC.ENRR", "Country Name"
    # new_df = df[[COL_1, COL_2, COL_3]]
    # new_df = new_df[new_df[COL_2] < 500]
    # new_df = new_df[new_df[COL_1] > 80]

    ######## BARCHART ########
    # private, public, country = "UIS.E.1.PR", "UIS.E.1.PU", "Country Name"  ##Bar Chart "Enrolment in primary education, private institutions, both sexes (number)" vs "Enrolment in primary education, public institutions, both sexes (number)" by location
    # new_df = df[[private, public, country]]
    #
    # fig = plt.figure(figsize=(10, 5))
    #
    # plt.bar(new_df[country], new_df[private],
    #         width=0.4)
    # plt.bar(df[country], df[public],
    #         width=0.4, bottom=public)
    # plt.xlabel("Countries")
    # plt.ylabel("No. of students enrolled")
    # plt.title("Students enrolled in different courses")
    # plt.show()


    # high_df = df[df["Country Name"].isin(get_countries_with_income(["High income: nonOECD", "High income: OECD"]))]
    # COL_1, COL_2, COL_3 = "SE.XPD.TOTL.GB.ZS", "NY.GDP.MKTP.CD", "Year"
    # new_df = high_df[[COL_1, COL_2, COL_3, "Country Name"]]
    # new_df.dropna(inplace=True)
    # new_df["Spent on Edu"] = new_df[COL_1] * new_df[COL_2] / 100
    #
    # high_grouped_df = new_df[["Year", COL_2, "Spent on Edu"]].groupby("Year").aggregate("sum")
    # high_grouped_df["% Spent On Edu"] = high_grouped_df["Spent on Edu"] / high_grouped_df[COL_2] * 100
    #
    # ## upper middle ##
    #
    # upper_middle_df = df[df["Country Name"].isin(get_countries_with_income(["Upper middle income"]))]
    # new_um_df = upper_middle_df[[COL_1, COL_2, COL_3, "Country Name"]]
    # new_um_df.dropna(inplace=True)
    # new_um_df["Spent on Edu"] = new_um_df[COL_1] * new_um_df[COL_2] / 100
    #
    # um_grouped_df = new_um_df[["Year", COL_2, "Spent on Edu"]].groupby("Year").aggregate("sum")
    # um_grouped_df["% Spent On Edu"] = um_grouped_df["Spent on Edu"] / um_grouped_df[COL_2] * 100
    #
    # ## lower middle ##
    # lower_middle_df = df[df["Country Name"].isin(get_countries_with_income(["Lower middle income"]))]
    # new_lm_df = lower_middle_df[[COL_1, COL_2, COL_3, "Country Name"]]
    # new_lm_df.dropna(inplace=True)
    # new_lm_df["Spent on Edu"] = new_lm_df[COL_1] * new_lm_df[COL_2] / 100
    #
    # lm_grouped_df = new_lm_df[["Year", COL_2, "Spent on Edu"]].groupby("Year").aggregate("sum")
    # lm_grouped_df["% Spent On Edu"] = lm_grouped_df["Spent on Edu"] / lm_grouped_df[COL_2] * 100
    #
    # # low income ##
    # low_df = df[df["Country Name"].isin(get_countries_with_income(["Low income"]))]
    # new_l_df = low_df[[COL_1, COL_2, COL_3, "Country Name"]]
    # new_l_df.dropna(inplace=True)
    # new_l_df["Spent on Edu"] = new_l_df[COL_1] * new_l_df[COL_2] / 100
    #
    # l_grouped_df = new_l_df[["Year", COL_2, "Spent on Edu"]].groupby("Year").aggregate("sum")
    # l_grouped_df["% Spent On Edu"] = l_grouped_df["Spent on Edu"] / l_grouped_df[COL_2] * 100
    #
    # combined_df = pd.concat([high_grouped_df["% Spent On Edu"], um_grouped_df["% Spent On Edu"], lm_grouped_df["% Spent On Edu"], l_grouped_df["% Spent On Edu"]], axis=1)
    # combined_df.columns = ['High', 'Upper Middle', 'Lower Middle', 'Low']
    #
    # combined_df_melted = combined_df.melt(var_name='Groups', value_name='Values')
    # sns.set(style="whitegrid")
    # sns.barplot(x='Groups', y='Values', data=combined_df_melted, hue='Groups')
    # plt.title('Grouped Bar Plot of Columns')
    # plt.xlabel('Income Group')
    # plt.ylabel('% Spent on Edu')
    # plt.legend(title='Columns')
    # plt.show()

    ######## HISTOGRAM ########

    # plt.hist(df["SE.PRM.ENRL.TC.ZS"])
    # plt.xlabel("Pupil-teacher ratio")
    # plt.ylabel("Number of occurrence")
    # plt.title("Pupil-teacher ratio in primary education (headcount basis)")
    # plt.show()

    ######## BOX PLOT ########
    # new_df = df[["SE.PRM.ENRR", "SE.SEC.ENRR", "SE.TER.ENRR"]]
    # data = [new_df["SE.PRM.ENRR"].dropna().values, new_df["SE.SEC.ENRR"].dropna().values, new_df["SE.TER.ENRR"].dropna().values]
    # plt.figure(figsize=(10, 6))
    # plt.boxplot(data, labels=['Primary', 'Secondary', 'Tertiary'])
    # plt.xlabel('Education Levels')
    # plt.ylabel('Enrollment Rate')
    # plt.title("Gross enrolment ratio, primary, both sexes (%) vs Gross enrolment ratio, secondary, both sexes (%)")
    # plt.grid(True)
    # plt.tight_layout()
    # plt.show()