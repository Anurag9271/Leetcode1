import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    df = employee.merge(department, left_on="departmentId", right_on="id")
    df = df.rename(columns={"name_x": "Employee", "name_y": "Department"})
    
    max_sal = df.groupby("Department")["salary"].max().reset_index()
    merge = df.merge(max_sal, on=["Department", "salary"])
    
    return merge[["Department", "Employee", "salary"]].rename(columns={"salary": "Salary"})
    