# load packages
import os as os                   # directory management
import pandas as pd               # data wrangling
import xlwt                       # writing to Excel, used with '.to_excel()'
import numpy as np                # data wrangling
import matplotlib.pyplot as plt   # data viz
import seaborn as sns             # data viz
import re                         # regular expressions, 

# check current working directory
os.getcwd()

# change working directory
os.chdir(os.getcwd())


# list items in current working directory
os.listdir()

# import data
STIdata1 = pd.read_csv("Data/STIData.csv")
# STIdata2 = pd.read_excel("Data/STIData.xls")  # requires xlrd module
# STIdata3 = pd.read_excel("Data/STIData.xlsx") # requires xlrd module

# check datatypes
type(STIdata1)
type(STIdata1.CaseStatus)
type(STIdata1["Date"])

STIdata1.dtypes
STIdata1["Date"].dtypes

# sorting
STIdata1 = STIdata1.sort_values(by = ["IdNumber"])

# reset index
STIdata1.reset_index(drop = True, inplace = True)

# handle duplicates
STIdata1.duplicated(subset = ["IdNumber"])

# identify duplicated rows
dup_rows1 = STIdata1[STIdata1.duplicated(subset = ["IdNumber"])]

dup_rows2 = STIdata1[STIdata1.IdNumber == 51]

last_id = STIdata1.IdNumber[len(STIdata1.IdNumber)-1]

# STIdata1[(STIdata1.IdNumber == 51) & (STIdata1.A1Age == 21)]

STIdata1.loc[(STIdata1["IdNumber"] == 51) & (STIdata1["A1Age"] == 21), "IdNumber"]

STIdata1.loc[(STIdata1["IdNumber"] == 51) & (STIdata1["A1Age"] == 21), "IdNumber"] = last_id + 1

# rename columns
STIdata1.rename(
    columns = {"IdNumber": "ID", 
               "CaseStatus": "Case_Status", 
               "A1Age": "Age",
               "A2Occupation": "Occupation",
               "A3Church": "Church",
               "A4LevelOfEducation": "Education_Level",
               "A5MaritalStatus": "Marital_Status"},
    inplace = True)

# drop unwanted columns
list(STIdata1.columns)

UnwantedCols = ['C3StiYesno', 'D1BurialSociety', 'D1religiousgrp', 
                'D1savingsClub', 'D1tradersAssoc', 'D2Group1', 'D2Group2', 
                'D3Education', 'Education', 'D3FuneralAssistance', 'D3HealthServices', 
                'DurationOfillness', 'E8WhyhaveSTI', 'N10givereceiveforsex',
                'N11Usedcondom', 'N12UseCondom', 'N13TakenAlcohol', 
                'N14DoYouHave', 'N15LivingTogether', 'N16HowOldIs',
                'D3receivecredit', 'Typeofsti', 'N2SexDebut', 'N3HadAnSti',
                'N9Relationship', 'HabitationStatus','SexPartner1year',
                'SexPartner3month', 'LastPartnerSpouse', 'Belong', 
                'ReceiveHelp', 'SexPartnerLife3', 'Sex.1']


STIdata1.drop(columns = UnwantedCols, inplace = True)

# clean cat variables

# clean Case_Status
STIdata1['Case_Status'].value_counts()

# replace 2 and 3 with 0
STIdata1.loc[STIdata1["Case_Status"] == 2, "Case_Status"] = 0
STIdata1.loc[STIdata1["Case_Status"] == 3, "Case_Status"] = 0

Case_Status_recode = {0:'Negative',
                      1:'Positive'}

STIdata1 = STIdata1.assign(Case_Status = STIdata1.Case_Status.map(Case_Status_recode))

# clean Unemployed
STIdata1['Unemployed'].value_counts()

Unemployed_recode = {1:'Yes',
                     2:'No'}

STIdata1 = STIdata1.assign(Unemployed = STIdata1.Unemployed.map(Unemployed_recode))

# clean AlcoholUse
STIdata1['AlcoholUse'].value_counts()

AlcoholUse_recode = {1:'Primary',
                     2:'Secondary'}

STIdata1 = STIdata1.assign(AlcoholUse = STIdata1.AlcoholUse.map(AlcoholUse_recode))

# fun to remove nums and spaces in a cat var
def clean_cat(data_frame, cat_var):
    data_frame[cat_var] = data_frame[cat_var].str.replace(r'[0-9]',"")
    data_frame[cat_var] = data_frame[cat_var].replace(r"^ +| +$", r"", regex = True)
    data_frame[cat_var] = data_frame[cat_var].str.title()
    return data_frame
    
# clean Occupation
STIdata1 = clean_cat(data_frame = STIdata1, cat_var = "Occupation")

# clean Church
STIdata1 = clean_cat(data_frame = STIdata1, cat_var = "Church")

# clean Education_Level
STIdata1 = clean_cat(data_frame = STIdata1, cat_var = "Education_Level")

# clean Marital_Status
STIdata1 = clean_cat(data_frame = STIdata1, cat_var = "Marital_Status")

# export clean data
STIdata1.to_csv(path_or_buf = "Data/Clean_STIData.csv", index = False)
STIdata1.to_excel(excel_writer = "Data/Clean_STIData.xls", index = False)

# append
STIdata2 = STIdata1.iloc[0:100, :]
STIdata3 = STIdata1.iloc[100:, :]

STIdata4 = STIdata2.append(STIdata3, ignore_index = True)

# merge
STIdata2 = STIdata1.iloc[:, 0:7]
STIdata3 = STIdata1.loc[:, STIdata1.columns[np.r_[0, 7:14]]]

STIdata4 = pd.merge(STIdata2, STIdata3, on = 'ID')

# filtering
# the following return the same 
Filtered_STIdata1 = STIdata1[(STIdata1.Case_Status == "Negative") & (STIdata1.Age <= 20)]
Filtered_STIdata1 = STIdata1.query('Case_Status == "Negative" & Age <= 20')
Filtered_STIdata1 = STIdata1.loc[(STIdata1.Case_Status == "Negative") & (STIdata1.Age <= 20)]

# in the below code, '.isin()' is similar to '%in%' in R and 'in' in SAS
Filtered_STIdata2 = STIdata1[STIdata1.Church.isin(["Roman Catholic", "Pentecostal"])]

# negating filtering
Filtered_STIdata3 = STIdata1[(STIdata1.Case_Status != "Negative") & (STIdata1.Age <= 20)]

# negating whole condtion
Filtered_STIdata4 = STIdata1[~((STIdata1.Case_Status == "Negative") | (STIdata1.Age <= 20))]

# missing records by var
Filtered_STIdata5 = STIdata1[pd.isnull(STIdata1['AgeFirstSex'])]

# non-missing records by var
Filtered_STIdata6 = STIdata1[STIdata1.AgeFirstSex.notnull()]
Filtered_STIdata6 = STIdata1[~pd.isnull(STIdata1['AgeFirstSex'])]

# using list comprehension
Filtered_STIdata7 = STIdata1[[x in ['Negative'] for x in STIdata1.Case_Status.values]]

# summary stats
STIdata1[["Age", "Weight", "Height"]].median()
STIdata1[["Age", "Weight", "Height"]].mean(skipna = True)
STIdata1[["Age", "Weight", "Height"]].mean(skipna = False)
STIdata1[["Age", "Weight", "Height"]].describe()

STIdata1.agg(
    {
     "Age": ["min", "max", "median", "skew"],
     "Weight": ["min", "max", "median", "mean"],
     }
    )

# summary stats by group
STIdata1[["Sex", "Age"]].groupby("Sex").mean()
STIdata1[["Sex", "Age", "Weight", "Height"]].groupby("Sex").mean()
STIdata1[["Occupation", "Age", "Weight", "Height"]].groupby("Occupation").mean().round(2)
STIdata1[["Occupation", "Age", "Weight", "Height"]].groupby("Occupation").describe()

# contigency tables (without totals)
pd.crosstab(index = STIdata1['Case_Status'], 
            columns =STIdata1['Occupation'])

# contigency tables (with totals)
pd.crosstab(index = STIdata1['Case_Status'], 
            columns =STIdata1['Occupation'], 
            margins = True)

# contigency tables (with total percent)
pd.crosstab(index = STIdata1['Case_Status'], 
            columns =STIdata1['Occupation'], 
            margins = True,
            margins_name = 'Total',
            normalize = 'all').round(4)*100

# contigency tables (with row percent)
pd.crosstab(index = STIdata1['Case_Status'], 
            columns =STIdata1['Occupation'], 
            margins = True,
            margins_name = 'Total',
            normalize = 'index').round(4)*100

# contigency tables (with col percent)
pd.crosstab(index = STIdata1['Case_Status'], 
            columns =STIdata1['Occupation'], 
            margins = True,
            margins_name = 'Total',
            normalize = 'columns').round(4)*100

# visualisation
# simple bar graph
sns.barplot(x = 'Occupation',
            y = 'Age', 
            data = STIdata1,
            estimator = 'mean')
plt.show()

# two-way bar graph
sns.barplot(x = 'Occupation',
            y = 'Age', 
            hue = 'Sex',
            data = STIdata1,
            estimator = 'median')
plt.show()

# two-way bar graph
ax = sns.barplot(
    x = 'Occupation',
    y = 'Age',
    hue = 'Sex',
    data = STIdata1,
    estimator = 'mean',
    orient = 'v',
    capsize = 0.1,
    dodge = True,
    errwidth = 0.5,
    palette = 'Set2'
    )
ax.legend(loc = 'upper left', ncols = 3)
plt.title("Occupation by Average Age and Sex")
plt.show()

# count bar graph
sns.countplot(x = STIdata1["Church"])
plt.show()

ax = sns.countplot(
    y = "Church",
    hue = "Case_Status",
    data = STIdata1,
    order = STIdata1['Church'].value_counts().index,
    palette='Set2'
    )
for label in ax.containers:
    ax.bar_label(label,
                 fontsize = 8)
plt.title("Church by Case Status")
plt.show()

# scatter plot
sns.scatterplot(
    data = STIdata1, 
    x = "Height", 
    y = "Weight", 
    hue = "Sex"
    )
plt.title("Weight by Height and Sex")
plt.legend(loc = 'upper left', ncols = 1)
plt.show()

sns.scatterplot(
    data = STIdata1, 
    x = "Height", 
    y = "Weight", 
    size = "Age",
    hue = "Age",
    style = "Sex"
    )
plt.title("Weight by Height, Sex, and Age")
plt.legend(loc = 'upper left', ncols = 1)
plt.show()

# line plot
sns.lineplot(
    data = STIdata1, 
    x = "Height", 
    y = "Weight",
    hue = "Occupation"
    )
plt.title("Weight by Height and Occupation")
plt.legend(loc = 'upper left', ncols = 1)
plt.show()

sns.lineplot(
    data = STIdata1, 
    x = "Height", 
    y = "Weight",
    hue = "AgeFirstSex"
    )
plt.title("Weight by Height and Age at First Sex")
plt.legend(loc = 'upper left', ncols = 1)
plt.show()
