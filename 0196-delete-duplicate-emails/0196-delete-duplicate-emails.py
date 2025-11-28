import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id',ascending=True,inplace=True)
    person = person.drop_duplicates(subset='email',keep='first',inplace=True)
    return person