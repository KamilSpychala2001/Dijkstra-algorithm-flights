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


def preprocess_flights(flights):
    flights['Departure datetime'] = pd.to_datetime(flights['Departure date'] + ' ' + flights['Departure time'])
    flights['Arrival datetime'] = pd.to_datetime(flights['Arrival date'] + ' ' + flights['Arrival time'])

    flights = flights.drop(['Departure date', 'Departure time', 'Arrival date', 'Arrival time'], axis=1)
    return flights


def get_cities_to_which_we_can_fly(dep_city, flights):
    cities = set(flights['Arrival city'][flights["Departure city"] == dep_city])
    return sorted(cities)


def fastest_connection_between_cities(dep_city, arr_city, datetime_start, flights):
    connection = flights[(flights["Departure city"] == dep_city) & (flights["Arrival city"] == arr_city) & (
            flights['Departure datetime'] >= datetime_start)]
    if connection.empty:
        print("No connection")
        return None
    final_df = connection.sort_values(by=['Departure datetime'], ascending=True)
    return final_df.iloc[0]