import sklearn.feature_selection
import sklearn.model_selection


def select_kbest(X, y, k):
    '''
    Description: Runs a SelectKBest through provided features 
    to determine which features (x) will most accuractly predict 
    the target feature (y).
    Takes:
        X - df: Features used to predict
        y - df or np.array: target feature is being predicted
        k - number of features to keep
    Returns:
        A list of the features that were kept
    '''

    kbest = sklearn.feature_selection.SelectKBest(sklearn.feature_selection.f_regression, k)
    kbest.fit(X, y)
    return X.columns[kbest.get_support()]

def select_rfe(X, y, k):
    '''
    Description: Runs a Recursive Feature Elimination through provided 
    features to determine which features (x) will most accuractly predict 
    the target feature (y).
    Takes:
        X - df: Features used to predict
        y - df or np.array: target feature is being predicted
        k - number of features to keep
    Returns:
        A list of the features that were kept
    '''

    lm = sklearn.linear_model.LinearRegression()
    rfe = sklearn.feature_selection.RFE(lm, k)
    rfe.fit(X, y)
    return X.columns[rfe.support_]