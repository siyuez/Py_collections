import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('taxi.csv')

X = dataset.iloc[:, 1:2].values
# 这里注意：1:2其实只有第一列，与1 的区别是这表示的是一个matrix矩阵，而非单一向量。
y = dataset.iloc[:, 5].values


# array.reshape(1, -1) if it contains a single sample.
X = np.reshape(X, (-1, 1))
y = np.reshape(y, (-1, 1))


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)
 
# Predicting a new result
y_pred = regressor.predict(sc_X.transform(np.array([[58]])))
# 转换回正常预测值
y_pred = sc_y.inverse_transform(y_pred)

print(y_pred)

# plt.scatter(X, y, color = 'red')
# plt.plot(X, regressor.predict(X), color = 'blue')
# plt.title('Truth or Bluff (SVR)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()

X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
