import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s start to have fun with US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = (input("\nChoose the city you would like your results to be filtered by? New York ,Washington  or Chicago ?\n").lower().title())
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Ammmmm. Your choice is not precise. Kindly, Try again please.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = (input("\nChoose the month you would like your results to be filtered by? January, February, March, April, May, June. You can write 'Random' if you want to get results without preferences?\n").lower().title())
      if month not in ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'Random'):
        print("Ammmmm. Your choice is not precise. Kindly, Try again.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = (input("\nDo you want to choose a specific day of the week? If you want, Write the day Precisely: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday.You can write  'Random' if you do not have any preference.\n").lower().title())
      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Random'):
        print("Ammmmm. Your choice is not precise. Kindly, Try again.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


print('Let us print again :)' + '-'*40)
    return city, month, day

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'Random':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 2

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nLet\'s know The Most common Times of hiring bikes to travel in america...\n')
    start_time = time.time()



# TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('The most common Month in bike hiring is:', common_month)


    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('The most common day in bike hiring is:', common_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common Hour in bike hiring is:', common_hour)


    print("\nThis pretty process was so fast.\nIt took only %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nNow we will know The Most common Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    Starting_Station = df['Start Station'].value_counts().idxmax()
    print('Most frequently used start station:', Starting_Station)


    # TO DO: display most commonly used end station

    Arrival_Station = df['End Station'].value_counts().idxmax()
    print('\nMost frequently used Arrival station:', Arrival_Station)


    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nmost frequent combination of starting station and Arrival station trip:', Starting_Station, " & ", Arrival_Station)


    print("\nThis pretty fast process took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration please wait little...\n')
    start_time = time.time()

    # TO DO: display total travel time

    Total_Time = sum(df['Trip Duration'])
    print('Total  time of the trip you want to know:', Total_Time/86400, " Days")


    # TO DO: display mean travel time

    Mean_Time = df['Trip Duration'].mean()
    print('Mean travel time you want to know :', Mean_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User statistics ...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('Counts of user Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nCounts of Gender Types:\n', gender_types)
    except KeyError:
      print("\nCounts of Gender Types:\nNo data can be shown.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year of birth :', Earliest_Year)
    except KeyError:
      print("\nEarliest Year of birth:\nNo data can be shown.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year of birth:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data can be shown.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year of birth:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data can be shown.")

    print("\nThis pretty fast process took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
#   I have tried here but i can not do it please advise me hot to make this works  
    next = 0
    while True:
        view_raw_data = input('\nWould you like to see the next rows of raw data? Say yes! Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5]) 
    
    
    
    
    
    
    

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to try our  fast data analysis program again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()