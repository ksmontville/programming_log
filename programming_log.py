import datetime as dt
import pandas as pd

filepath = 'c:/users/montv/python_work/programming_log/programming_log.csv'
pro_log_df = pd.read_csv(filepath, index_col=0)

time_start = input("Time start (hh:mm) ")
time_end = input("Time end (hh:mm) ")

date = dt.date.today()

time_start_calc = dt.timedelta(hours=int(time_start[0:2]), minutes=int(time_start[3:5]))
time_end_calc = dt.timedelta(hours=int(time_end[0:2]), minutes=int(time_end[3:5]))
time = str(time_end_calc - time_start_calc)[:-3]

task = input("Task: ")

entry_dict = {
    'date': [date],
    'time': [time],
    'task': [task],
}

entry_df = pd.DataFrame(entry_dict)

pro_log_df = pd.concat([pro_log_df, entry_df], ignore_index=True)
pro_log_df.to_csv(filepath)
