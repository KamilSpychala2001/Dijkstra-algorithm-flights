# Flight Data Analysis Project

This project is designed to preprocess and analyze flight data. The main goal is to find the fastest connections between cities and provide various utilities for flight data manipulation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project preprocesses flight data to create a more usable format and provides functions to:
- Find cities to which we can fly from a given departure city.
- Determine the fastest connection between two cities.
- Identify the fastest connection to a city that hasn't been visited yet.
- Initialize and update results for Dijkstra's algorithm to find the shortest paths between cities.

## Features

- **Preprocessing flight data**: Convert flight dates and times into datetime objects.
- **Finding destinations**: Retrieve cities to which flights are available from a given departure city.
- **Fastest connections**: Determine the fastest connection between two cities based on departure and arrival times.
- **Dijkstra's algorithm**: Implement Dijkstra's algorithm to find the shortest paths (fastest connection) between cities.

## Requirements

- Python 3.x
- pandas

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Install the required packages:
    ```bash
    pip install pandas
    ```

3. Ensure you have your flight data in a CSV file (e.g., `flights_4.csv`).

## Usage

1. Load and preprocess flight data:
    ```python
    import pandas as pd
    from your_script_name import preprocess_flights

    flights = pd.read_csv('flights_4.csv')
    flights = preprocess_flights(flights)
    ```

2. Initialize the results for Dijkstra's algorithm:
    ```python
    from your_script_name import init_result

    city_beginning = "Bangkok"
    result, visited_cities = init_result(city_beginning, "2023-11-01 09:00:00", flights)
    ```

3. Run Dijkstra's algorithm to find the shortest paths:
    ```python
    from your_script_name import dijstra_algorithm

    end_result = dijstra_algorithm(visited_cities, flights, result)
    print(end_result)
    ```

## Functions

- `preprocess_flights(flights)`: Preprocess flight data by converting date and time columns into datetime objects.
- `get_cities_to_which_we_can_fly(dep_city, flights)`: Returns a sorted list of cities to which we can fly from the given departure city.
- `fastest_connection_between_cities(dep_city, arr_city, datetime_start, flights)`: Find the fastest connection between two cities.
- `get_datetime_in_city(city, result)`: Returns the datetime when we will be in the specified city.
- `get_all_cities(flights)`: Retrieve all unique cities from the flight data.
- `fastest_connection_to_not_visited(visited, flights, result)`: Find the fastest connection to a city that hasn't been visited yet.
- `init_result(start_city, start_datetime, flights)`: Initialize the results DataFrame and set of visited cities for Dijkstra's algorithm.
- `dijstra_algorithm(visited_cities, flights, result)`: Run Dijkstra's algorithm to find the shortest paths between cities.

