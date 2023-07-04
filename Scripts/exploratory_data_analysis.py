# load packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os as os

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

# clean cat variables


# write functions

# append

# merge

# filtering

# summary stats by group

# visualisation


