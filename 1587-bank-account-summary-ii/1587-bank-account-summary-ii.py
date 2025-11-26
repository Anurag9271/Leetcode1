import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    res = users.merge(transactions,on="account")
    res['balance']=res.groupby('account')['amount'].transform('sum')
    return res[res['balance']>10000][['name','balance']].drop_duplicates()