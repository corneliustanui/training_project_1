# load packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os
import re

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

# clean Occupation
STIdata1.Occupation = STIdata1.Occupation.str.replace(r'[0-9]',"")
STIdata1.Occupation = STIdata1.Occupation.replace(r"^ +| +$", r"", regex = True)
STIdata1.Occupation = STIdata1.Occupation.str.title()

# clean Church
STIdata1.Church = STIdata1.Church.str.replace(r'[0-9]',"")
STIdata1.Church = STIdata1.Church.replace(r"^ +| +$", r"", regex = True)
STIdata1.Church = STIdata1.Church.str.title()

# clean Education_Level
STIdata1.Education_Level = STIdata1.Education_Level.str.replace(r'[0-9]',"")
STIdata1.Education_Level = STIdata1.Education_Level.replace(r"^ +| +$", r"", regex = True)
STIdata1.Education_Level = STIdata1.Education_Level.str.title()

# clean Marital_Status
STIdata1.Marital_Status = STIdata1.Marital_Status.str.replace(r'[0-9]',"")
STIdata1.Marital_Status = STIdata1.Marital_Status.replace(r"^ +| +$", r"", regex = True)
STIdata1.Marital_Status = STIdata1.Marital_Status.str.title()

# write functions

# append

# merge

# filtering

# summary stats by group

# visualisation



