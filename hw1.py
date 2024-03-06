import pandas as pd
import numpy as np

#making arrays for all data
emilyData = np.array(['emily', 2024, 'comstock'])
charlieData = np.array(['charlie', 2024, 'tyler'])
natalieData = np.array(['natalie', 2024, 'chapin'])
sadieData = np.array(['sadie', 2023, 'wilder'])
jessieData = np.array(['jessie', 2023, 'friedman'])

#making series based on arrays
emily = pd.Series(emilyData, index=['name', 'year', 'dorm'])
charlie = pd.Series(charlieData, index=['name', 'year', 'dorm'])
natalie = pd.Series(natalieData, index=['name', 'year', 'dorm'])
sadie = pd.Series(sadieData, index=['name', 'year', 'dorm'])
jessie = pd.Series(jessieData, index=['name', 'year', 'dorm'])

#makes a list of all series
friends = [emily, charlie, natalie, sadie, jessie]


#build data function
def builddata(list):
   #makes a new dataframe with name, year, dorm columns
  newdf = pd.DataFrame(list, columns = ['name', 'dorm', 'year'])
  #sets name column as index
  newdf.set_index('name', drop = True, inplace = True)
  #returns df
  return newdf

#smithdata function
def smithdata(list):
   #calling build data
   smithdf = builddata(list)
   #renames dorm to house
   smithdf.rename(columns = {'dorm' : 'house'}, inplace = True)
   smithdf.drop('year', inplace=True, axis=1)
   #return updated df
   return smithdf

#little print statements i ran to test
#testdf = builddata(friends)
#print("builddata", testdf)

newtestdf = smithdata(friends)
print(newtestdf)
print(newtestdf.shape)
#print("smithie data", newtestdf)

def make_change(cost, paid):   
   """ This function will make change for a transaction. If their is
   not enough funds, then it will say so."""    
   
   # Begin by computing the total change for the transaction
   total = round(paid - cost,2)   
   if total < 0:
      return "The customer has not fully paid for this transaction"    
      
   # Compute the amount for each type of change: 
   dollars = int(total)    
   change = round(total - dollars,2)   
   
   quarters = int(change / 0.25)
   change = round(change % 0.25,2)
   
   dimes = int(change / 0.10)
   change = round(change % 0.10,2)
   
   nickels = int(change / 0.05)
   change = round(change % 0.05,2)
   
   pennies = int(change / 0.01)
   
   return (total, dollars, quarters, dimes, nickels, pennies)

change = make_change(10, 17.39)
print(change)
print('me', make_change(10, 17.39)[5])
print(type(change))
print(len(change))
