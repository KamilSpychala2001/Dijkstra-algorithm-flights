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


def get_datetime_in_city(city, result):
    city_data = result[result['city'] == city]
    return city_data['end_datetime'].iloc[0]


def get_all_cities(flights):
    all_cities = pd.unique(flights[['Departure city', 'Arrival city']].values.ravel())
    return sorted(all_cities)
    # return sorted(flights['Departure city'].unique())
    # return sorted(flights[['Departure city', 'Arrival city']].unique())


def fastest_connection_to_not_visited(visited, flights, result):
    visited_list = list(visited)

    # initializing with big data
    fastest_flight_datetime = datetime(2033, 3, 1, 9, 30, 00)
    fastest_flight = None

    for visited_city in visited_list:

        # getting the time in which we will be in the city
        current_datetime_in_city = get_datetime_in_city(visited_city, result)
        possible_destination_from_city = get_cities_to_which_we_can_fly(visited_city, flights)

        for destination_city in possible_destination_from_city:
            # checking if the city is visited
            if destination_city in visited_list:
                # if it is already visited then continue
                continue
            else:
                temp = fastest_connection_between_cities(visited_city, destination_city, current_datetime_in_city, flights)

                # if no connection is found then continue, could happen in the "late" range
                if temp is None:
                    continue

                # faster flight
                if temp['Departure datetime'] < fastest_flight_datetime:
                    fastest_flight_datetime = temp['Departure datetime']
                    fastest_flight = temp
    # returning the fastest flights to a non-visited city
    return fastest_flight


def init_result(start_city, start_datetime, flights):
    # adding the beginning city as a visited city:
    visited_cities = set()
    visited_cities.add(start_city)

    results_df = pd.DataFrame(columns=['city', 'start_datetime', 'end_datetime', 'previous_city', 'cost'])
    # all_cities = sorted(flights['Departure city'].unique())
    all_cities = get_all_cities(flights)
    for city in all_cities:
        if city == start_city:
            dict_flight = {'city': city, "start_datetime": start_datetime, "end_datetime": start_datetime,
                           "previous_city": start_city, "cost": 0}
            new_row = pd.DataFrame([dict_flight])
        else:
            # 2030-11-01 09:00:00 as "infinity"
            dict_flight = {'city': city, "start_datetime": "2030-11-01 09:00:00", "end_datetime": "2030-11-01 09:00:00",
                           "previous_city": "empty", "cost": 99999}
            new_row = pd.DataFrame([dict_flight])

        results_df = pd.concat([results_df, new_row], ignore_index=True)

    results_df['start_datetime'] = pd.to_datetime(results_df['start_datetime'])
    results_df['end_datetime'] = pd.to_datetime(results_df['end_datetime'])

    return results_df, visited_cities


def end_criterion(all_cities):
    set_cities = set(all_cities)
    if set_cities == visited_cities:
        return True
    else:
        return False