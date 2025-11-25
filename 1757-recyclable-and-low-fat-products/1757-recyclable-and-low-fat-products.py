import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    res=products[(products['low_fats']=='Y')&(products['recyclable']=='Y')]['product_id']
    return res.to_frame()


    # res=products.loc[
    #     (products['low_fats']=='Y') &
    #     (products['recyclable']=='Y'),
    #     'product_id'
    # ]
    # return res.to_frame()



    # res=products.query("low_fats=='Y' and recyclable == 'Y' ")['product_id']
    # return res.to_frame()


    # f1 = products[products["low_fats"] == "Y"]
    # f2 = f1[f1["recyclable"] == "Y"]
    # res = f2["product_id"]
    # return res.to_frame()



    

    