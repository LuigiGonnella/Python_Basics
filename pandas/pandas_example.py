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

#rinominare series
pd.Series([1, 2, 3, 4, 5], index=['Luka', 'James', 'Lebron', 'Rafa', 'Ginobili'], name='goats')

#!READING DATA FILES (read_csv)
wine_reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv') #ritorna DataFrame
print(wine_reviews.shape) #considers only data, not the first row
print(wine_reviews.head()) #all content, included first row

#pd.read_csv has so many optional parameters, for example, if the file has a column that has the indexes of the records, we can tell to the funziton to pick up this column instead of creating a new one when calling data.head()
# --> wine_reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv', index_col=0), diciamo che la prima colonna e quella che sta indicizzando i records

#!WRITING DATA FILES (to_csv)
wine_reviews.to_csv('pandas\input\winemag-data-130k-v2.csv')


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
#reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv')
#print(reviews.set_index('username')) #here index is username
print(reviews) #here indexes are incremental numbers from 0

#!CONDITIONAL SELECT
#print(reviews['Product A'] > 30) #prints true/false for each record
#print(reviews.loc[reviews['Product A'] > 30]) #prints entire record that respect the condition

#ISIN BUILT-IN METHOD
#print(reviews.loc[reviews['Product A'].isin([0, 30, 35, 32])]) #prints entire record that respect the condition

#others built-in methods
#reviews.loc[reviews['Product A'].isnull()]
#reviews.loc[reviews['Product A'].notnull()]
#...

#!ASSIGNING DATA TO DATAFRAME
#reviews['Product A'] = 0 #constant value to all records at the column 'Product A'
print(reviews)
#reviews['Product A'] = range(len(reviews), 0, -1) #decreasing value
print(reviews)




#EXERCISE
#Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:
#df = reviews.iloc[[0, 1, 10, 100]].loc[:,['country', 'province', 'region_1', 'region_2']]

#!SYNTAX OF MULTIPLE LOGICAL OPERATORS
#top_oceania_wines = reviews.loc[((reviews['country'] == 'Australia') | (reviews['country'] == 'New Zealand')) & (reviews['points'] >=95) & (reviews['points'] <=100)]
#ALWAYS use |, & ecc instead of native pthon commands and ALWAYS enclose the operand between round brackets () | () & () and so on ...

#!SUMMARY FUNCTIONS AND MAPS (apply and maps)
#FUNCTIONS
reviews = pd.read_csv('pandas\input\winemag-data-130k-v2.csv')
print(reviews['points'].describe()) #describes statistics on this column
print(reviews['points'].mean()) #mean
print(reviews['points'].median()) #median

print(reviews['taster_name'].unique()) #takes an array with all the unique occurrences
print(reviews['taster_name'].value_counts()) #takes all UNIQUE values and how often they appear in the dataframe

#MAP, like we seen in python before

points_mean = reviews['points'].mean()
reviews['points'].map(lambda x: x - points_mean) #transform each value, but takes in input a single value --> x cannot be an enitre dataframe, but just a value in one record, and with map, we transform that value for each record
#retuurns a NEW Series (datafram entry, corresponfing to 'points') doesn't modify the original dataframe. Non cambia nulla anche con -=

def remean_ponts(row):
    row['points'] = row['points'] - points_mean
    return row

reviews.apply(remean_ponts, axis = 'columns') #pass to the function each ROW, returning a NEW dataframe without modifying the original one
#reviews.apply(..., axis = 'index') pass to the function each COLUMN

#a faster way is
reviews['points'] - points_mean

#fast way of combining values of different column for each record
reviews['country'] + ' ' + reviews['region_1'] #returns a Series in which we have this concatenation for each record

#!IDXMAX() FUNCTION
#takes the index (of record) with the max value passsed as a parameter
bargain_indx = (reviews['points']/reviews['price']).idxmax()
bargain_wine = reviews.loc[bargain_indx, 'title'] #title of the wine with the highest ratio point/price
print(bargain_wine)

#TROVARE NUMERO DI DESCRIZIONI CON ALMENO UNA VOLTA 'tropical' e quelle con almeno una volta 'fruity' e tornare una series
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum() #num_desc con tropical
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum() #num_desc con fruity
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity']) #series

#ASSEGNARE STELLE SECONDO ALCUNI CRITERI, AD OGNI RECORD
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(stars, axis='columns')


#!GROUPING AND SORTING
#classic group by, cio che mettiamo dentro groupby(...) diventa l'indice della series/dataframe ritornata (non la colonna), la colonna invece e specificata da cio che scriviamo dopo groupby
reviews.groupby('points')['points'].count() #di fatto una value_counts() su points, il parametro in groupby ci dice di raggruppare per la colonna 'points', la second aparte conta effettivamente quante volte il numero nella colonna compare
reviews.groupby('points')['price'].min() #raggruppo per punti e prendo il minimo prezzo per ogni numero di punteggio, quindi, per ogni valore di punteggio, conto il prezzo minimo

#CHAIN con apply
reviews.groupby('winery').apply(lambda df: df['title'].iloc[0]) #nel dataframe ora ci sara solo una series per winery, in cui il titolo sara il primo vino recensito

#groupby su piu colonne (multi-index)
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df['points'].idxmax()]) #record con i punti massimi per ogni coppia country, provincia

#eseguire operazioni simultanee sul dataframe con agg
reviews.groupby('country')['price'].agg([len, min, max]) #per ogni country mostro il prezzo minimo, massimo e il numero di prezzi (len conta il numero di record in cui price non e nullo e esiste)

#MULTI-INDEXES
countries_reviwed = reviews.groupby(['country', 'province'])['description'].agg([len]) #multi-index = groupby su piu colonne, ora l'indice non epiu 0, 1, 2, ecc ma e la coppia country-province, quindi queste non sono colonne, ma indici
#mantenere lo stesso  dataframe, ma con gli indici numerici (0, 1, 2, ecc) e con country e province come colonne
#se scrivo .agg[len] ottengo un dataframe con colonna 'len' e rispettivo valore, se invece scrivo .agg(len) ottengo una series con indice multiplo (gia detto) e valore la lunghezza della descrizione
countries_reviwed.reset_index()

#SORTING
countries_reviwed.reset_index()
#singolo by, by si usa SOLO sui dataframe (hanno piu colonne), le series invece ne hanno solo 1, quindi accettano come unico parametro ascendig=True/False
countries_reviwed.sort_values(by='len', ascending=False) #ordini per la colonna (dalla piu grande) lunghezza tutti i record nel df
#multipli by
countries_reviwed.sort_values(by=['country', 'len'], ascending=False) #ordini per molteplici colonne, prima 'country' e poi 'len'

#country	province	len
#1	Argentina	Other	536
#0	Argentina	Mendoza Province	3264
#...	...	...	...
#424	Uruguay	Uruguay	24
#419	Uruguay	Canelones	43

countries_reviwed.sort_index() #ripristina l'ordine originale da indice 0 all'ultimo

#EXERCISES
print(reviews.groupby('taster_twitter_handle').apply(lambda df: len(df))) #numero review per ogni reviewer, deprecato
reviews_written = reviews.groupby('taster_twitter_handle').size() #equivalente

#What is the best wine I can buy for a given amount of money? 
# Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. 
# Sort the values by price, ascending (so that 4.0 dollars is at the top and 3300.0 dollars is at the bottom).
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index() #gli indici sono i prezzi

#What are the minimum and maximum prices for each `variety` of wine? Create a `DataFrame` whose index is the `variety` category from the dataset and whose values are the `min` and `max` values thereof.
price_extremes = reviews.groupby('variety')['price'].agg([min, max])

#What are the most expensive wine varieties? 
# Create a variable `sorted_varieties` containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

#Create a `Series` whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the `taster_name` and `points` columns.

df = reviews.groupby('taster_name')['points'].agg([sum, len])
reviewer_mean_ratings = df.apply(lambda row: row['sum']/row['len'], axis='columns')

#or, better
reviewer_mean_ratings = reviews.groupby('taster_name')['points'].mean()

#!DATA TYPES AND MISSING VALUES
#DATA TYPES
reviews['price'].dtype # --? dtype('float64)

reviews.dtypes #return dtype of every column of the dataframe

reviews['points'].astype('float64') #casting della colonna

reviews.index.dtype #ci dice il tipo dell'indice di una series o un dataframe

#MISSING DATA
reviews[pd.isnull(reviews['country'])] #ritorna tutti i record che hanno la colonna 'country'=NaN

reviews['region_2'].fillna('Unknown') #rimpiazza ogni NaN della colonna 'region_2' con Unknown, per ogni record

reviews['taster_twitter_handle'].replace('@kerinokeefe', '@kerino') #rimpiazza tutte le occorrenze, per ogni record, nella colonna specificata, con il nuovo valore


#EXERCISES

#Sometimes the price column is null. How many reviews in the dataset are missing a price?

missing_price_reviews = reviews[reviews.price.isnull()] #!DATAFRAME
n_missing_prices = len(missing_price_reviews) #!numero di records
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum() #!SERIES con True/False come values
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum() #!SERIES con True/False come values

#What are the most common wine-producing regions? 
# Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. 
# Sort in descending order. Your output should look something like this:
reviews['region_1']=reviews['region_1'].fillna('Unknown') #!fillna si puo eseguire solo su una series (non su dataframe)
reviews_per_region = reviews.groupby('region_1').size().sort_values(ascending=False) #di fatto sto facendo un value_counts() di 'region_1'
#non posso mettere .fillna dopo .size() perche dopo size() io ho una series con gli indici a NaN per color che non hanno il region_1
#Nel caso (groupby + size) ottengo una series per cui i NaN sono nell’indice se esistono record con region_1 mancante.
#Nel caso reviews['region_1' ottengo una series per cui i NaN sono nei valori della Series, non nell’indice.
#or
reviews_per_region = reviews['region_1'].fillna('Unknown').value_counts().sort_values(ascending=False) #agisco direttamnete sulla singola colonna (series)


#!RENAMING AND COMBINING
#RENAMING
reviews.rename(columns={'points': 'score'}) #rinomino colonna

reviews.rename(index={0 : 'firstEntry', 1: 'secondEntry'}) #analogo, ma per le righe (indici)

reviews.rename_axis('wines', axis='rows').rename_axis('fields', axis='columns') #rinominare assi

#COMBINING different dataframes and/or series --? .concat(), .join() and .merge() (not so useful, replaceble with join() most of the times)

canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

#CONCAT
pd.concat([canadian_youtube, british_youtube]) #mergiamo due dataframe in uno unico, si puo fare anche se non hanno le stesse colonne. Il dataframe risultante avra come colonne la sommatoria delle colonne e in quelle non comuni ci saranno dei nan

#JOIN, si usa quando due dataframe hanno l'indice in comune
left = canadian_youtube.set_index(['title', 'trending_date']) #settiamo lo stesso indice per entrambi (la coppia ['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK') #cosi per ogni coppia title, trending_date, per entrambi i dataframe, se ne forma uno unico, con i dati di entrami sulle colonne, differenziati dagli appositi suffissi scelti
#non per forza devono avere le stesse colonne

#		video_id_CAN	channel_title_CAN	category_id_CAN	publish_time_CAN	tags_CAN	views_CAN	likes_CAN	dislikes_CAN	comment_count_CAN	thumbnail_link_CAN	...	tags_UK	views_UK	likes_UK	dislikes_UK	comment_count_UK	thumbnail_link_UK	comments_disabled_UK	ratings_disabled_UK	video_error_or_removed_UK	description_UK
#title	trending_date																					
#_!! THIS VIDEO IS NOTHING BUT PAIN !! | Getting Over It - Part 7	18.04.01	PNn8sECd7io	Markiplier	20	2018-01-03T19:33:53.000Z	getting over it|"markiplier"|"funny moments"|"...	835930	47058	1023	8250	https://i.ytimg.com/vi/PNn8sECd7io/default.jpg	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
#1 Fortnite World Rank - 2,323 Solo Wins!	18.09.03	DvPW66IFhMI	AlexRamiGaming	20	2018-03-09T07:15:52.000Z	PS4 Battle Royale|"PS4 Pro Battle Royale"|"Bat...	212838	5199	542	11	https://i.ytimg.com/vi/DvPW66IFhMI/default.jpg	...	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
#...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
#🚨 BREAKING NEWS 🔴 Raja Live all Slot Channels Welcome 🎰	18.07.05	Wt9Gkpmbt44	TheBigJackpot	24	2018-05-07T06:58:59.000Z	Slot Machine|"win"|"Gambling"|"Big Win"|"raja"...
