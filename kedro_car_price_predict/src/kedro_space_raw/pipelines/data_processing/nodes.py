

import pandas as pd



def preprocessed_hyundai(hyundai: pd.DataFrame) -> pd.DataFrame:
    hyundai = hyundai.rename({'tax(Â£)': 'tax'}, axis=1)

    return hyundai


def preprocessed_mercedes(mercedes: pd.DataFrame) -> pd.DataFrame:
    mercedes['engineSize'] = mercedes['engineSize'].str[:-1]

    return mercedes

def create_car_input_table(
    audi: pd.DataFrame, hyundai: pd.DataFrame, mercedes: pd.DataFrame) -> pd.DataFrame:

    car_input_table = pd.concat([audi, hyundai, mercedes])
    return car_input_table