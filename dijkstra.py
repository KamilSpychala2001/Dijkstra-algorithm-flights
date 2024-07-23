from datetime import datetime
import pandas as pd

pd.set_option('display.max_columns', 1000)
pd.set_option('max_colwidth', 150)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)


# flights = pd.read_csv('./flights.csv')
# flights = pd.read_csv('./flights_2.csv')
# flights = pd.read_csv('flights_3.csv')
flights = pd.read_csv('flights_4.csv')