import time
from datetime import datetime, timedelta
import pandas as pd


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nHi there! Let\'s explore some US bikeshare data!\nWhich city would you like to see data for? Chicago, New York, or Washington?\n').lower()
        if city == 'chicago':
            return './data/chicago.csv'
        if city == 'new york':
            return './data/new_york_city.csv'
        if city == 'washington':
            return './data/washington.csv'
        else:
            print('Oops! I didn\'t get that. Please input either Chicago, New York, or Washington.')


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (str) Time filter for the bikeshare data.
    '''
    time_period = ''
    while time_period.lower() not in ['month', 'day', 'none']:
        time_period = input('\nHow would you like to filter the data? By month, day, or without any filter? Type "none" to see the data without any time filter.\n').lower()
        if time_period not in ['month', 'day', 'none']:
            print('Oops! I didn\'t get that.')
    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of month for the bikeshare data.
    '''
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in months_dict.keys():
        month_input = input(
            '\nWhich month? January, February, March, April, May, or June?\n').lower()
        if month_input not in months_dict.keys():
            print('Oops! I didn\'t get that. Please type in a month between January and June')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))


def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    '''
    this_month = get_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:
        is_int = False
        day = input('\nWhich day? Please type your response as an integer.\n')
        while is_int == False:
            try:
                day = int(day)
                is_int = True
            except ValueError:
                print('Oops! I didn\'t get that. Please type your response as an integer.')
                day = input(
                    '\nWhich day? Please type your response as an integer.\n')
        try:
            start_date = datetime(2017, month, day)
            valid_date = True
        except ValueError as error:
            print(str(error).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))


def most_popular_month(df):
    '''Finds and prints the most popular month for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))


def most_popular_day(df):
    '''Finds and prints the most popular day of week (Monday, Tuesday, etc.) for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(
        most_pop_day))


def most_popular_hour(df):
    '''Finds and prints the most popular hour of day for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_hour = int(df['start_time'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format
          (pop_hour_readable, am_pm))


def total_trip_duration(df):
    '''Finds and prints the total trip duration and average trip duration in
       hours, minutes, and seconds.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {} seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {} seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(
            m, s))


def most_popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    pop_start = df['start_station'].mode().to_string(index=False)
    pop_end = df['end_station'].mode().to_string(index=False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))


def most_popular_trip(df):
    '''Finds and prints the most popular trip.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_trip = df['journey'].mode().to_string(index=False)
    print('The most popular trip is {}.'.format(most_pop_trip))


def get_users(df):
    '''Finds and prints the counts of each user type.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))


def get_gender(df):
    '''Finds and prints the counts of gender.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(
        male_count, female_count))


def get_birth_years(df):
    ''' Finds and prints the earliest (i.e. oldest user), most recent (i.e.
        youngest user), and most popular birth years.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.\nThe most popular birth year is {}.'.format(earliest, latest, mode))


def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.
    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        return bool(display.lower() in ['yes', 'no'])
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? Type \'yes\' or \'no\'.\n').lower()
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Oops! I didn\'t get that. Please type 'yes' or 'no'.")
    if display.lower() == 'yes':
        # prints every column except the 'journey' column created in statistics()
        print(df[df.columns[1:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Oops! I didn\'t get that. Please type 'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[1:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def get_statistics():
    '''Calculates and prints out the statistics about a particular city and
    time period specified by the user via input.
    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    print('Loading data...')
    df = pd.read_csv(city, parse_dates=['Start Time', 'End Time'])
    df.dropna(inplace = True)

    # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels

    # increases the column width so that the long strings in the 'journey'
    # column can be displayed fully
    pd.set_option('max_colwidth', 100)

    # creates a 'journey' column that concatenates 'start_station' with
    # 'end_station' for the use popular_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none':
        df_filtered = df
    elif time_period in ['month', 'day']:
        if time_period == 'month':
            filter_lower, filter_upper = get_month()
        elif time_period == 'day':
            filter_lower, filter_upper = get_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\nCalculating the first statistic...')

    if time_period == 'none':
        start_time = time.time()

        # What is the most popular month for start time?
        most_popular_month(df_filtered)
        print(
            "This took %s around seconds to calculate." % (time.time() - start_time))
        print("\nCalculating the next statistic...")

    if time_period in ['none', 'month']:
        start_time = time.time()

        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        most_popular_day(df_filtered)
        print(
            "This took %s around seconds to calculate." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    most_popular_hour(df_filtered)
    print("This took %s around seconds to calculate." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    total_trip_duration(df_filtered)
    print("This took %s around seconds to calculate." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    most_popular_stations(df_filtered)
    print("This took %s around seconds to calculate." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    most_popular_trip(df_filtered)
    print("This took %s around seconds to calculate." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    get_users(df_filtered)
    print("This took %s around seconds to calculate." % (time.time() - start_time))

    if city in ['chicago.csv', 'new_york_city.csv']:
        print("\nCalculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        get_gender(df_filtered)
        print(
            "This took %s around seconds to calculate." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

        # What are the earliest, most recent, and most popular birth years?
        get_birth_years(df_filtered)
        print(
            "This took %s around seconds to calculate." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(df_filtered)

    # Restart if user wants to..
    restart = input(
        '\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
    while restart not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input(
            '\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
    if restart == 'yes':
        get_statistics()
    else:
        print("Good Bye!")
        return


if __name__ == "__main__":
    get_statistics()
