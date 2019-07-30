from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd 

data=pd.read_csv('Housing.csv')
print(data)

x_train, x_test, y_train, y_test=train_test_split(data['lotsize'],data['price'],test_size=0.3, random_state=1)

#create linear regression object
model=LinearRegression()

#reshaping the data
x_train=x_train.values.reshape(-1,1)
y_train=y_train.values.reshape(-1,1)
x_test=x_test.values.reshape(-1,1)

#train the model using training sets
model.fit(x_train,y_train)

#make predictions using testing set
y_pred=model.predict(x_test)

#printing predictions
print(y_pred)


