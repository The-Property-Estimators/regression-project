import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

from acquire_kwame import get_zillow_data

def prepare_zillow():
    df = get_zillow_data()

    # Drop features to create an MVP (first iteration)
    df = df.drop(columns=['calculatedbathnbr', 'fips', 'latitude', 'longitude', 'regionidcounty', 'roomcnt', 'yearbuilt', 'assessmentyear', 'propertycountylandusecode', 'propertylandusetypeid'])
    # Drop rows with NaNs
    df = df.dropna()

    #Split the data
    train_validate, test = train_test_split(df, test_size=.2, random_state=666)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=666)

    X_train = train.drop(columns='taxvaluedollarcnt')
    X_validate = validate.drop(columns='taxvaluedollarcnt')
    X_test = test.drop(columns='taxvaluedollarcnt')

    y_train = train['taxvaluedollarcnt']
    y_validate = validate['taxvaluedollarcnt']
    y_test = test['taxvaluedollarcnt']

    return df, train, validate, test, X_train, X_validate, X_test, y_train, y_validate, y_test