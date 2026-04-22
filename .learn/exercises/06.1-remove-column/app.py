import pandas as pd

data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')

#print(data_frame)

data = pd.Series([23,45,7,34,6,63,36,78,54,34])

#print(data)

datatime = pd.date_range(start='2021-05-01', end='2021-05-12')
#print(datatime)

my_series = pd.Series([2, 4, 6, 8, 10])

resultado = my_series.apply(lambda x: x/2)

#print(resultado)

#exercise 5 DataFrames
data2 = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]

dt = pd.DataFrame(data2, columns= ['Brand', 'Model', 'Color'])

#print(dt)

#exercise 5.1 DataFrame Dict
data3 = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]

dt2 = pd.DataFrame(data3, columns= ['brand', 'model', 'color'])

#print(dt2)

#exercise 5.2 DataFrame iLoc
#print(data_frame.iloc[133,6])

#exercise 5.3 DataFrame head
#print(data_frame.head(3))

#exercise 5.4 DataFrame Tail
#print(data_frame.tail(3))

#exercise 05.5 Print Columns
#print(data_frame[['Name','Type 1']][0:10])

#exercise 05.6 Loc Function
#print(data_frame.loc[data_frame['Attack']>80])

#exercise 05.7 Filter and Count
#print(len(data_frame.loc[data_frame['Legendary']==True]))

#exercise 06 Clean Datasets
data_frame2 = pd.read_csv('.learn/assets/us_baby_names_right.csv')

#print(data_frame2.head(5))

data_frame2.drop(data_frame2.columns[0], axis=1, inplace=True)
#print(data_frame2.head())

