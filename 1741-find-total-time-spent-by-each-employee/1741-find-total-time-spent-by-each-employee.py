import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = (employees['in_time'] - employees['out_time']).abs()
    employees = employees.drop(['in_time','out_time'],axis = 1)
    employees = employees.groupby(['event_day','emp_id'],as_index=False)['total_time'].sum()
    employees = employees.rename(columns={'event_day':'day'})
    return employees.sort_values('emp_id')
    
    