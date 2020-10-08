import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.linear_model import LinearRegression, TweedieRegressor
from sklearn.feature_selection import RFE
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

from acquire_kwame import get_zillow_data
from prepare_kwame import prepare_zillow

def model()
    df, train, validate, test, X_train, X_validate, X_test, y_train, y_validate, y_test = prepare_zillow()

    sns.distplot(y_train)
    plt.title('Distribution of y_train data (by the Million)')
    plt.xlabel('Assessed value of the property (in Millions USD)')
    plt.xlim(right=1.006124e+07)
    plt.xlim(left=0.001124e+07)

    sns.distplot(y_train)
    plt.title('Distribution of y_train data (by the Million), continued')
    plt.xlabel('Assessed value of the property (in Millions USD)')
    plt.xlim(right=4.996124e+07)
    plt.xlim(left=4.401124e+07)

    baseline = y_train.mean()

    baseline_rmse_train = mean_squared_error(y_train, np.full(len(y_train), baseline))**1/2
    print('RMSE (Root Mean Square Error) of Baseline on train data:\n', baseline_rmse_train)
    baseline_rmse_validate = mean_squared_error(y_validate, np.full(len(y_validate), baseline))**1/2
    print('RMSE (Root Mean Square Error) of Baseline on validate data:\n', baseline_rmse_validate)

    train['bathbedcnt'] = X_train.bathroomcnt + X_train.bedroomcnt
    validate['bathbedcnt'] = X_validate.bathroomcnt + X_validate.bedroomcnt
    test['bathbedcnt'] = X_test.bathroomcnt + X_test.bedroomcnt

    X_train['bathbedcnt'] = X_train.bathroomcnt + X_train.bedroomcnt
    X_validate['bathbedcnt'] = X_validate.bathroomcnt + X_validate.bedroomcnt
    X_test['bathbedcnt'] = X_test.bathroomcnt + X_test.bedroomcnt

    y_train['bathbedcnt'] = X_train.bathroomcnt + X_train.bedroomcnt
    y_validate['bathbedcnt'] = X_validate.bathroomcnt + X_validate.bedroomcnt
    y_test['bathbedcnt'] = X_test.bathroomcnt + X_test.bedroomcnt

    # prep data

    df, train, validate, test, X_train, X_validate, X_test, y_train, y_validate, y_test = prepare_zillow()
    train.head(3)

    train_validate, test = train_test_split(df, test_size=.2, random_state=666)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=666)

    x_cols = ['bathroomcnt', 'bedroomcnt',
        'calculatedfinishedsquarefeet', 'bathbedcnt']

    train['bathbedcnt'] = train.bathroomcnt + train.bedroomcnt
    validate['bathbedcnt'] = validate.bathroomcnt + validate.bedroomcnt

    X_train['bathbedcnt'] = train.bathroomcnt + train.bedroomcnt
    X_validate['bathbedcnt'] = validate.bathroomcnt + validate.bedroomcnt

    y_train['bathbedcnt'] = train.bathroomcnt + train.bedroomcnt
    y_validate['bathbedcnt'] = validate.bathroomcnt + validate.bedroomcnt

    X_train = train[x_cols]
    y_train = train.taxvaluedollarcnt

    X_validate = validate[x_cols]
    y_validate = validate.taxvaluedollarcnt

    train = train.dropna()
    validate = validate.dropna()
    test = train.dropna()

    X_train = X_train.dropna()
    X_validate = X_validate.dropna()
    X_test = X_test.dropna()

    y_train = y_train.dropna()
    y_validate = y_validate.dropna()
    y_test = y_test.dropna()

    k = 2

    # create and fit linear regression object
    lm = LinearRegression(normalize = True)
    lm.fit(X_train, y_train)
    # create and fit the rfe object
    rfe = RFE(lm, k)
    rfe.fit(X_train, y_train)
    X_train.columns[rfe.support_]

    print('RFE Selected Features:\n', X_train.columns[rfe.support_])

    # prep data

    train_validate, test = train_test_split(df, test_size=.2, random_state=666)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=666)

    x_cols = ['bathroomcnt', 'bedroomcnt',
        'calculatedfinishedsquarefeet', 'bathbedcnt']

    train['bathbedcnt'] = train.bathroomcnt + train.bedroomcnt
    validate['bathbedcnt'] = validate.bathroomcnt + validate.bedroomcnt

    X_train['bathbedcnt'] = train.bathroomcnt + train.bedroomcnt
    X_validate['bathbedcnt'] = validate.bathroomcnt + validate.bedroomcnt

    y_train['bathbedcnt'] = train.bathroomcnt + train.bedroomcnt
    y_validate['bathbedcnt'] = validate.bathroomcnt + validate.bedroomcnt

    X_train = train[x_cols]
    y_train = train.taxvaluedollarcnt

    X_validate = validate[x_cols]
    y_validate = validate.taxvaluedollarcnt

    train = train.dropna()
    validate = validate.dropna()
    test = train.dropna()

    X_train = X_train.dropna()
    X_validate = X_validate.dropna()
    X_test = X_test.dropna()

    y_train = y_train.dropna()
    y_validate = y_validate.dropna()
    y_test = y_test.dropna()

    # create the model object
    lm = LinearRegression(normalize=True)

    # fit the model to our training data.
    lm.fit(X_train, y_train.taxvaluedollarcnt)

    # predict train
    y_train.taxvaluedollarcnt = lm.predict(X_train)

    # evaluate: rmse
    rmse_train = mean_squared_error(y_train.taxvaluedollarcnt, y_train.taxvaluedollarcnt_pred_lm)**1/2

    # predict validate
    y_validate['taxvaluedollarcnt_pred_lm'] = lm.predict(X_validate)

    # evaluate: rmse
    rmse_validate = mean_squared_error(y_validate.taxvaluedollarcnt, y_validate.taxvaluedollarcnt_pred_lm)**1/2

    print("RMSE for OLS using LinearRegression on train data:\n", rmse_train, '\n\n', 
        "On test data:\n", rmse_validate)