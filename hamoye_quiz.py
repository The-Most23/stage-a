import pandas as pd
csv = r'C:\Users\user\Desktop\HAMOYE FILES\FoodBalanceSheets_E_Africa_NOFLAG.csv'
df = pd.read_csv(csv, encoding='latin-1')
#print(df.head())


#Question 11
sum_of_Animal_Fat = df.groupby("Item")[["Y2014","Y2017"]].sum().loc["Fat supply quantity (g/capita/day)"]
print(sum_of_Animal_Fat)

#Question 12
#Sum of Y2015 to three decimal places
total = df["Y2015"].mean()
#calculating the standard devition
s_deviation = df["Y2015"].std()
print("The mean is ", round(total,3) ,"and the standard deviation is ", round(s_deviation,3))

#Question 13
#calculating the sum and percentage of missing data in Y2016
sum_of_missing = df["Y2016"].isna().sum()
percentage = df[["Y2014","Y2015","Y2016","Y2017","Y2018"]].isna().sum().sum()
p = (sum_of_missing/percentage) * 100
#print(sum_of_missing,percentage)
print("The sum of missing data is ", sum_of_missing , " and the percentage is ", p)

#Question 14
print(df.groupby("Element Code")[["Y2014","Y2015","Y2016","Y2017","Y2018"]].sum().sum())
#Answer is Y2017

#Question 15
highest = df.groupby("Element")[["Y2014","Y2015","Y2016","Y2017","Y2018"]].sum().loc["Import Quantity"]
print(highest, " has the highest import quantity")
#Answer is Y2017

#Question 16
sum_of_Production_2014 = df.groupby("Element")["Y2014"].sum().loc["Production"].sum()
print(sum_of_Production_2014," is the sum of 2014 production")

#Question 17
highest_2018_sum = df.groupby("Element")["Y2018"].sum()
print(highest_2018_sum)
#Answer is Domestic supply quantity

#Question 18
highest_2018_sum = df.groupby("Element")["Y2018"].sum()
print(highest_2018_sum)
#Answer is Protein supply quantity(g/capita/day)

#Question 19
total_import_Algeria = df.groupby(["Element","Area"])["Y2018"].sum().loc["Import Quantity","Algeria"]
print(total_import_Algeria, "for total import quantity in ALgeria")
#Answer is 36328.29

#Question 20
unique_countries = df["Area"].describe()
print(unique_countries, " for unique countries in the dataset")
