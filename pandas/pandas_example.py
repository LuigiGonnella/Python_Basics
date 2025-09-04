import pandas as pd

#!DATAFRAME
#is a table

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

pd.DataFrame({'Bob': ['I liked it', 'Not very much'], 'Alice': ['Pretty good', 'Very satisfying']})

#specifying indexes (label of the rows, or records)

pd.DataFrame({'Bob': ['I liked it', 'Not very much'], 'Alice': ['Pretty good', 'Very satisfying']}, index=['Person A', 'Person B'])
#                    Bob            Alice
#Person A     I liked it      Pretty good
#Person B  Not very much  Very satisfying

#!SERIES
#is a lists, displayed vertically, with the index on the left and the type of elemnts in the bottom

pd.Series([1, 2, 3, 4, 5]) #entry di dataframe di fatto

#specifying labels for entry isntead of indexes

pd.Series([1, 2, 3, 4, 5], index=['Luka', 'James', 'Lebron', 'Rafa', 'Ginobili'])

#!READING DATA FILES (csv)

wine_reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv')
print(wine_reviews.shape) #considers only data, not the first row
print(wine_reviews.head()) #all content, included first row

#pd.read_csv has so many optional parameters, for example, if the file has a column that has the indexes of the records, we can tell to the funziton to pick up this column instead of creating a new one when calling data.head()
# --> wine_reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv', index_col=0), diciamo che la prima colonna e quella che sta indicizzando i records


#!INDEXING, SELECTING, ASSIGNING

reviews = pd.DataFrame({'Bob': ['I liked it', 'Not very much'], 'Alice': ['Pretty good', 'Very satisfying']}, index=['Person A', 'Person B'])

print(reviews.Bob)
print(reviews['Bob']) #same

#picking a specific object
print(reviews['Bob'][0]) #like a dictionary, deprecated

#!INDEXING WITHOUT LABELS
print(reviews.iloc[0]) #modern, takes all first record (row) (reviews by Person A)

print(reviews.iloc[:,0]) #takes all first column (reviews to Bob)
print(reviews.iloc[:,0:-1]) #takes all but last column (reviews to Bob)

#!INDEXING LABEL BASED --> LOC instead of ILOC
print(reviews.loc['Person A', 'Bob']) #first element, equals to reviews.iloc[0, 0]
print(reviews.iloc[0, 0])

print(reviews.loc[:, 'Bob']) #all bob's reviews, equals to print(reviews.iloc[:,0]) 

#!DIFFERENCES BETWEEN ILOC and LOC
#it's the same despite the range syntax, so if we write loc[0:10] it will take records from 0 to 10 INCLUDED (if the entries are numbers) (useful for strings entries), while iloc[0:10] will take records from 0 to 9

#!SETTING INDEX
reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv')
print(reviews.set_index('username')) #here index is username
print(reviews) #here indexes are incremental numbers from 0

#!CONDITIONAL SELECT
print(reviews['Product A'] > 30) #prints true/false for each record
print(reviews.loc[reviews['Product A'] > 30]) #prints entire record that respect the condition

#ISIN BUILT-IN METHOD
print(reviews.loc[reviews['Product A'].isin([0, 30, 35, 32])]) #prints entire record that respect the condition

#others built-in methods
reviews.loc[reviews['Product A'].isnull()]
reviews.loc[reviews['Product A'].notnull()]
#...

#!ASSIGNING DATA TO DATAFRAME
reviews['Product A'] = 0 #constant value to all records at the column 'Product A'
print(reviews)
reviews['Product A'] = range(len(reviews), 0, -1) #decreasing value
print(reviews)




#EXERCISE
#Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:
#df = reviews.iloc[[0, 1, 10, 100]].loc[:,['country', 'province', 'region_1', 'region_2']]

#!SYNTAX OF MULTIPLE LOGICAL OPERATORS
#top_oceania_wines = reviews.loc[((reviews['country'] == 'Australia') | (reviews['country'] == 'New Zealand')) & (reviews['points'] >=95) & (reviews['points'] <=100)]
#ALWAYS use |, & ecc instead of native pthon commands and ALWAYS enclose the operand between round brackets () | () & () and so on ...

#!SUMMARY FUNCTIONS AND MAPS

