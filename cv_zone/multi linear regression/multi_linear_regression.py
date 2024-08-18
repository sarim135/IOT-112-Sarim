import pandas as pd
from sklearn import preprocessing,linear_model
import numpy as np
import sklearn
#### LOAD DATA ####
print('-'*30);print("IMPORTING DATA");print('-'*30)
data = pd.read_csv('houses_to_rent.csv', sep = ',')
data = data [['city','rooms','bathroom', 'parking spaces','fire insurance',
'furniture','rent amount']]
print(data.head())

#### PROCESS DATA ####
data['rent amount'] = data['rent amount'].map(lambda i: int(i[2:].replace(',','')))
data['fire insurance'] = data['fire insurance'].map(lambda i: int(i[2:].replace(',','')))
le = preprocessing.LabelEncoder()
data['furniture'] = le.fit_transform((data['furniture']))
print(data.head())

print('-'*30);print("CHECKING NULL DATA ");print('-'*30)
print(data.isnull().sum())
#data = data.dropna()
print('-'*30);print(" HEAD ");print('-'*30)
print(data.head())

#### SPLT DATA ####
print('-'*30);print(" SPLIT DATA ");print('-'*30)
x = np.array(data.drop(['rent amount'],axis=1))
y = np.array(data['rent amount'])
print('X',x.shape)
print('Y',y.shape)
xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x,y,
                                                                        test_size=0.2,
                                                                        random_state=10)
                                                                            

print('XTrain',xTrain.shape)
print('XTest',xTest.shape)

#### TRAINING ####
print('-'*30);print(" TRAINING ");print('-'*30)
model = linear_model.LinearRegression()
model.fit(xTrain,yTrain)
accuracy = model.score(xTest,yTest)
print('Cofficients: ',model.coef_)
print('Intercept: ', model.intercept_)
print('Accuracy:',round(accuracy*100,3),'%')

#### EVALUATION ####
print('-'*30);print(" MANUAL TESTING ");print('-'*30)
testVals = model.predict(xTest)
print(testVals.shape)
error = []
for i,testVal in enumerate(testVals):
    error.append(yTest[i]-testVal)
    print(f'Acutal:{yTest[i]} Prediction:{int(testVal)} Error: {int(error[i])}')