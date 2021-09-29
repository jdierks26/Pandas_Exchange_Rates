import pandas as pd

# Here we are loading in our erate.txt file that contains our Countries, their Currencies, and their Exchange Rates, and storing it into a Pandas Dataframe for 
# easy accessibility of information. 
# Since the .txt file does not contain headers, we will have to declare them here
df1 = pd.read_csv('erate.txt', names= ['Country', 'Currency', 'Exchange_Rate'])

# A
# Write a program that requests the name of a county as input and then displays the name of its currency
# and its exchange rate.

# Here we are collecting the user's input
country_input = str(input("Enter in a country: "))

# Here we are scanning through our Dataframe until we find the index of our Country input using .loc, then finding the
# country's Currency and Exchange Rate using our newfound index. (There is likely a more elegant solution, but this is
# what we came up with)
for i in df1.index:
    if df1.loc[i, 'Country'] == country_input:
        print(str(country_input) + "'s currency is the " + str(df1.loc[i, 'Currency']) + " and its exchange rate is " + str(df1.loc[i, 'Exchange_Rate']))

# B
# Write a program that displays the names of the countries in ascending order determined by the number of units that
# can be purchased for one American dollar

# Here we can use .sort_values to sort our Dataframe by the columns we specify
df1 = df1.sort_values(by=['Exchange_Rate', 'Country'])

# C
# Write a program that requests the names of two countries and an amount of money, and then converts the amount from
# the first country’s currency to the equivalent amount in the second country’s currency

# Here we are gathering the necessary inputs
c1 = input("Enter a country: ")
c2 = input("Enter another country: ")
money = float(input("Enter an amount of money: "))

# Here we are finding the Exchange rate and Currency for the two country inputs using a similar approach in A, and
# storing them into variables to use for our calculation and print statement.
for i in df1.index:
    if df1.loc[i, 'Country'] == c1:
        c1_rate = df1.loc[i, 'Exchange_Rate']
        c1_cur = df1.loc[i, 'Currency']
    if df1.loc[i, 'Country'] == c2:
        c2_rate = df1.loc[i, 'Exchange_Rate']
        c2_cur = df1.loc[i, 'Currency']

print(str(money) + " " + str(c1_cur) + "s from " + str(c1) + " " + "is equal to " + str((c1_rate * money) * c2_rate) + " " + str(c2_cur) + "s from " +str(c2))
