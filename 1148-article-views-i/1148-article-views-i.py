import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    auth_viewed_on_art=views[views['author_id']==views['viewer_id']]
    # return auth_viewed_on_art
    unique_authors = auth_viewed_on_art['author_id'].unique()
    # return unique_authors
    unique_authors = sorted(unique_authors)
    result_df = pd.DataFrame({'id':unique_authors})
    return result_df
    