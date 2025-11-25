import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res=customers.merge(orders,how="left",left_on='id',right_on='customerId')
    return (res[res.customerId.isna()].rename(columns={'name':'Customers'}).iloc[:,[1]])
    