import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import preprocessing


def get_countries_with_income(income):
    country_df = pd.read_csv('EdStatsCountry.csv')
    country_df = country_df[country_df['Currency Unit'].notna()]
    return set(country_df[country_df["Income Group"].isin(income)]["Table Name"].to_list())

country_df = pd.read_csv('EdStatsCountry.csv')
print(country_df["Income Group"].unique())


if __name__=="__main__":
    df = pd.read_csv("pivot.csv")
    # COL_1, COL_2, COL_3 = "SE.ADT.LITR.ZS", "NY.GDP.PCAP.PP.KD", "Country Name" ### Literacy rate and GDP PPP
    # COL_1, COL_2, COL_3 = "UIS.LPP.AG15T99", "SE.ADT.LITR.MA.ZS", "Country Name" ### male literacy and female literacy
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
    # COL_1, COL_2, COL_3 = "UIS.E.1.PR", "UIS.E.1.PU", "Country Name"  ##Bar Chart "Enrolment in primary education, private institutions, both sexes (number)" vs "Enrolment in primary education, public institutions, both sexes (number)" by location
    # new_df = df[[COL_1, COL_2, COL_3]]
    #
    # fig = plt.figure(figsize=(10, 5))
    #
    # plt.bar(df[COL_3], df[COL_1],
    #         width=0.4)
    # plt.bar(df[COL_3], df[COL_2],
    #         width=0.4, bottom=COL_1)
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

    ## low income ##
    # low_df = df[df["Country Name"].isin(get_countries_with_income(["Low income"]))]
    # new_l_df = low_df[[COL_1, COL_2, COL_3, "Country Name"]]
    # new_l_df.dropna(inplace=True)
    # new_l_df["Spent on Edu"] = new_l_df[COL_1] * new_l_df[COL_2] / 100
    #
    # l_grouped_df = new_l_df[["Year", COL_2, "Spent on Edu"]].groupby("Year").aggregate("sum")
    # l_grouped_df["% Spent On Edu"] = l_grouped_df["Spent on Edu"] / l_grouped_df[COL_2] * 100

    # plt.bar(l_grouped_df.index, l_grouped_df["% Spent On Edu"],
    #         width=0.4)

    # plt.xlabel("Year")
    # plt.ylabel("% of expenditure")
    # plt.title("Government expenditure on education as % of GDP (%) and others")
    # plt.show()

    ######## HISTOGRAM ########

    # COL_1 = "SE.PRM.ENRL.TC.ZS"
    # plt.hist(df[COL_1])
    # plt.xlabel("Pupil-teacher ratio")
    # plt.ylabel("Number of occurrence")
    # plt.title("Pupil-teacher ratio in primary education (headcount basis)")
    # plt.show()

    ######## SCATTER PLOT ########

    # COL_1, COL_2, COL_3 = "SE.PRM.ENRR", "SE.SEC.ENRR", "Year" ##Scatter Plot "Gross enrolment ratio, primary, both sexes (%)" vs "Gross enrolment ratio, secondary, both sexes (%)" over time
    # new_df = df[[COL_1, COL_2, COL_3]]
    # print(new_df[[COL_1, COL_2]].corr(method='pearson', min_periods=1000))
    # print(new_df.describe())
    # sb.scatterplot(y=new_df[COL_1], x=new_df[COL_2])

    # label_offset = 0.5  # Change this offset value as needed
    # for idx, row in new_df.iterrows():
    #     plt.text(row[COL_2] + label_offset, row[COL_1] + label_offset, row[COL_3])
    #
    # plt.xlabel(COL_2)
    # plt.ylabel(COL_1)
    # plt.show()

    ######## BOX PLOT ########
    COL_1, COL_2, COL_3 = "SE.PRM.ENRR", "SE.SEC.ENRR", "SE.TER.ENRR" ## Scatter Plot "Gross enrolment ratio, primary, both sexes (%)" vs "Gross enrolment ratio, secondary, both sexes (%)"

    new_df = df[[COL_1, COL_2, COL_3]]
    data = [new_df[COL_1].dropna().values, new_df[COL_2].dropna().values, new_df[COL_3].dropna().values]
    plt.figure(figsize=(10, 6))
    plt.boxplot(data, labels=['Primary', 'Secondary', 'Tertiary'])
    plt.xlabel('Education Levels')
    plt.ylabel('Enrollment Rate')
    plt.title('Comparison of Enrollment Rates in Different Education Levels')
    plt.grid(True)
    plt.tight_layout()
    plt.show()