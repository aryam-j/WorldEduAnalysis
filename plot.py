import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import preprocessing


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
    #
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

    COL_1, COL_2, COL_3, COL_4, COL_5= "SE.XPD.TOTL.GB.ZS", "SE.XPD.PRIM.ZS", "SE.XPD.SECO.ZS", "SE.XPD.SECO.ZS", "Year"
    new_df = df[[COL_1, COL_2, COL_3, COL_4, COL_5]]
    plt.bar(df[COL_5], df[COL_1],
            width=0.4,)
    plt.bar(df[COL_5], df[COL_2],
            width=0.4, bottom=COL_1)
    plt.bar(df[COL_5], df[COL_3],
            width=0.4, bottom=COL_2)
    plt.bar(df[COL_5], df[COL_4],
            width=0.4, bottom=COL_3)
    plt.xlabel("Year")
    plt.ylabel("% of expenditure")
    plt.title("Government expenditure on education as % of GDP (%) and others")
    plt.show()
    ######## LINE CHART ########

    # COL_1, COL_2 = "SE.SEC.ENRL.FE.ZS", "Year"
    # plt.plot(df[COL_2], df[COL_1])
    # plt.xlabel("Year")
    # plt.ylabel("Percentage of students in secondary education who are female (%)")
    # plt.title("Plotting {} vs {}".format(COL_1, COL_2))
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

    # plt.xlabel(COL_2)
    # plt.ylabel(COL_1)
    # plt.show()
