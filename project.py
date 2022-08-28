import pandas as pd

df = pd.read_csv(r"C:\Users\Tanu Singh\Desktop\Project\a.csv") #'r' converts normal string to raw string 
df.shape
df.keys()
df.drop(['Profile Name','Attributes', 
       'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark',
       'Country'],axis=1)   #axis=1  ;for dropping the column
df.dtypes
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df.dtypes
df.head(1)
# change the Start Time column into the dataframe's index
df = df.set_index('Start Time')

# convert from UTC timezone to indian time
df.index = df.index.tz_convert('Asia/kolkata')

# reset the index so that Start Time becomes a column again
df = df.reset_index()
df.head(1)
# measures the time
df['Duration']=pd.to_timedelta(df['Duration'])
df.head(1)
office = df[df['Title'].str.contains('The Office (U.S.)', regex=False)]  #filtering string (title)
office.shape
office=office[(office['Duration']> "0 days 00:01:00")]
office.shape
office['Duration'].sum()
office['weekday'] = office['Start Time'].dt.weekday
office['hour'] = office['Start Time'].dt.hour

# check to make sure the columns were added correctly
office.head(1)
%matplotlib inline
import matplotlib
# set our categorical and define the order so the days are plotted Monday-Sunday
# set our categorical and define the order so the days are plotted Monday-Sunday
office['weekday'] = pd.Categorical(office['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)

# create office_by_day and count the rows for each weekday, assigning the result to that variable
office_by_day = office['weekday'].value_counts()

# sort the index using our categorical, so that Monday (0) is first, Tuesday (1) is second, etc.
office_by_day = office_by_day.sort_index()


# plot office_by_day as a bar chart with the listed size and title
office_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')

# set our categorical and define the order so the hours are plotted 0-23
office['hour'] = pd.Categorical(office['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)

# create office_by_hour and count the rows for each hour, assigning the result to that variable
office_by_hour = office['hour'].value_counts()

# sort the index using our categorical, so that midnight (0) is first, 1 a.m. (1) is second, etc.
office_by_hour = office_by_hour.sort_index()

# plot office_by_hour as a bar chart with the listed size and title
office_by_hour.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Hour')
