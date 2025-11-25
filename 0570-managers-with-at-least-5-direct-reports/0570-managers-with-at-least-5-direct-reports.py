import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df=employee.merge(employee,left_on='id',right_on='managerId')
    count_df=df.groupby('id_x').size().reset_index(name='count')
    managers=count_df[count_df['count']>=5]
    return employee[employee['id'].isin(managers['id_x'])][['name']]