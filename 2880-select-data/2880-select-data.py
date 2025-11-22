import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    return df[['name','age']][df['student_id']==101]