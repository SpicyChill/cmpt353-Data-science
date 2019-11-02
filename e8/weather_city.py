import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import sys

def main():
    label_data = pd.read_csv(sys.argv[1])
    x = label_data.drop('city', axis='columns')
    y = label_data['city']
    X_train, X_test, y_train, y_test = train_test_split(x, y)
    model = make_pipeline(
    	StandardScaler(),
    	SVC(kernel='linear', C=0.1)
    )
    model.fit(X_train, y_train)
    print(model.score(X_test,y_test))
    unlabel = pd.read_csv(sys.argv[2])
    new_x = unlabel.drop('city',axis='columns')
    predictions = model.predict(new_x)
    pd.Series(predictions).to_csv(sys.argv[3], index=False, header=False)
    df = pd.DataFrame({'truth': y_train, 'prediction': model.predict(X_train)})
    print(df[df['truth'] != df['prediction']])
    
if __name__ == '__main__':
    main()