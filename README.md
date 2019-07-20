# US Bikeshare Project

This script is written to explore data related to bike sharing system in US cities: Chicago, New York and Washington. Data is imported from a csv file and several useful statistics are then calculated from the data. It takes in input from the users for custom filters to show the data according to certain criteria. This provides an interactive experience to the script when run the in the terminal.

## How to run

This script uses Python 3.x. This can be run with any python IDE such as Spyder. Spyder is available with Anaconda which can be downloaded from [here](https://www.anaconda.com/download/). Install he application and run the Anaconda Navigator to find Spyder. Alternatively, you can also search for Spyder under Anaconda folder in Start menu on Windows, or use spotlight on MacOS.

Alternatively, you can also run this in IDLE that comes by default with python installation on Windows. Just type the following commands to run the script:

`python bikeshare.py`

After running the above command, just provide the info the script asks for to generate useful statitics.

## Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time
- End Time
- Trip Duration (in seconds)
- Start Station
- End Station
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year

## Statistics

The script provides the following statistics from the bike share data:

### 1 Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

### 2 Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

### 3 Trip duration

- total travel time
- average travel time

### 4 User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Future scopes

Currently, the following new features are being considered:

- More custom filters
- A GUI: This can make the script much more user friendly.
- Convertion to a web based application.
