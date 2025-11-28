import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # condition = (employees['employee_id']%2==1)&(~employees['name'].str.startswith('M'))
    # employees['bonus'] = employees['salary'].where(condition,0)
    # employeees = employees.sort_values('employee_id',ascending=True)
    # return employees[['employee_id','bonus']]

    condition = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    
    employees['bonus'] = employees['salary'].where(condition, 0)

    employees = employees.sort_values('employee_id', ascending=True)
    
    return employees[['employee_id', 'bonus']]

    