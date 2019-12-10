import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import cross_val_score


dataset = pd.read_csv('taxi.csv', header=None)


X = dataset.iloc[:, 0:5].values
# 这里注意：1:2其实只有第一列，与1 的区别是这表示的是一个matrix矩阵，而非单一向量。
y = dataset.iloc[:, 5].values

# array.reshape(1, -1) if it contains a single sample.
y = np.reshape(y, (-1, 1))

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.05)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
# standardization
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

svr = SVR(kernel = 'rbf')
svr.fit(x_train, y_train)
y_predict = svr.predict(x_test)
result = np.hstack((y_test.reshape(-1, 1), y_predict.reshape(-1, 1)))

print('train')
print(r2_score(y_train.reshape((1,-1))[0], svr.predict(x_train).reshape((1,-1))[0]))

print('test')
print(r2_score(y_test, y_predict))

plt.scatter(y_train, svr.predict(x_train), color = 'green')
plt.show()

plt.scatter(y_test, y_predict, color = 'red')
plt.show()

scores = cross_val_score(svr, x_train, y_train, scoring='r2')
print(scores)
print(scores.mean())
