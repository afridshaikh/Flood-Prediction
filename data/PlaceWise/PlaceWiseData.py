import pandas as pd
import csv
import datetime
import glob
maindf = pd.DataFrame()

def getdate(date):
    date = datetime.datetime.strptime(date, '%d%m%Y').strftime('%d/%m/%Y')
    return date

filepaths = glob.glob('E:\Projects\Flood-Prediction\data\RainFallData\*\*.csv')

for filepath in filepaths:
    date = getdate(filepath[-12:-4])
    df = pd.read_csv(filepath, index_col=0)
    if any(df['0'] == 'Hyderabad'):
        df1 = df.loc[df['0'] == 'Hyderabad', '0':]
        df1.loc[df['0'] == 'Hyderabad', 12] = date
        maindf = maindf.append(df1)

maindf.to_csv('E:\Projects\Flood-Prediction\data\PlaceWise\Hyderabad.csv')
