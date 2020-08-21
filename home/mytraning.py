import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
clf = LogisticRegression()

if __name__ == "__main__":
    
    data=pd.read_csv("data.csv")
    np.random.seed(42)
    shuff = np.random.permutation(len(data))
    p =int(len(data)*0.8)
    train = shuff[:p]
    test = shuff[p:]
    test=data.iloc[test]
    train=data.iloc[train]
    train_label = train["inf prob"].to_numpy()
    test_label = test["inf prob"].to_numpy()
    train_features = train[['fever','body pain','age','runny nose','diff breath']].to_numpy()
    test_features = test[['fever','body pain','age','runny nose','diff breath']].to_numpy()
    clf.fit(train_features,train_label)

    file = open('model.pkl','wb')
    pickle.dump(clf,file)

    #pred
    clf.predict_proba([[100,1,12,1,1]])[0][1]