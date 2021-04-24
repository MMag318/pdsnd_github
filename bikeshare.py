import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= ' '
    month= ' '
    day= ' '
    while city.lower() not in ['chicago','new york city','washington']:
        city = input("What city do you want tot analyze? Please choose between 'chicago', 'new york city' and 'washington':").lower()

    # Get user input for month (all, january, february, ... , june)
    while month.lower() not in ['all','january','february',',march','april','may','june']:
        month = input("What month do you want analyze? Select 'january' to 'june' or 'all':").lower()

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while day.lower() not in ['all','monday','tuesday','wdnesday','thursday','friday','saturday','sunday']:
        day = input("What day do you want analyze? Select 'monday' to 'sunday' or 'all':").lower()

    print('-'*40)
    return city, month, day

# Function to load the data
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data file into a dataframe
    if city == 'chicago':
        df = pd.read_csv('chicago.csv')
    elif city == 'new york city':
        df = pd.read_csv('new_york_city.csv')
    else:
        df = pd.read_csv('washington.csv')


    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print('\nMost Common Month: ', most_common_month)


    # Display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nMost Common Day of Week: ', most_common_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('\nMost commonly used start station:', most_common_start)

    # Display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('\nMost commonly used end station:', most_common_end)

    # Display most frequent combination of start station and end station trip
    df['Combination'] = "From " + df['Start Station'] + " to " + df['End Station']
    most_common_combination = df['Combination'].mode()[0]
    print('\nMost common combination of start and end station:', most_common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print('Total travel time in minutes', df['Trip Duration'].sum()/60)

    # Display mean travel time
    print('Mean travel time in minutes', df['Trip Duration'].mean()/60)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCount of User types:', user_types)


    # Display counts of gender
    if city in ['chicago','new york city']:
        gender = df['Gender'].value_counts()
        print('\nCount of Gender:', gender)
    else:
        print('\nno data available on gender')

    # Display earliest, most recent, and most common year of birth
    if city in ['chicago','new york city']:
        age_early = df['Birth Year'].min()
        age_recent = df['Birth Year'].max()
        age_common = df['Birth Year'].mode()[0]
        print('\nEarliest year of birth:', age_early)
        print('\nMost recent year of birth:', age_recent)
        print('\nMost common year of birth:', age_common)
    else:
        print('\nno data available on age')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Function for output 5 lines of raw data
def rawdata(df):
    begin= 0
    end= 5
    raw= ' '
    while raw not in ['yes','no']:
        raw = input("Do you want to see raw data? Please indicate by 'yes' or 'no:").lower()

        if raw == 'yes':
            raw_next = ' '
            print(df.iloc[begin:end])
            while raw_next not in ['no']:
                raw_next = input("Do you want to see more raw data? Please indicate by 'yes' or 'no':").lower()

                if raw_next == 'yes':
                 begin += 5
                 end += 5
                 print(df.iloc[begin:end])

                else:
                    break






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
