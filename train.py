import pandas as pd 
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import pickle
 

data_path = "train.csv"
df = pd.read_csv(data_path)

scaler = StandardScaler()
scaler.fit(df.ix[1:30000,1:785])

X_train =scaler.transform(df.ix[1:30000,1:785])
y_train =df.ix[1:30000,0:1]

print('using support vector machines : ')
SVM = SVC().fit(X_train , y_train)
print('accuracy on training set : ',SVM.score(X_train,y_train))


data_path = "test.csv"
test = pd.read_csv(data_path)

scaler = StandardScaler()
scaler.fit(test.ix[:,:])

ans = []
index =[]
i= 0
while i<28000:
	X_test = scaler.transform(test.ix[i:i,0:784])
	predicted_value = SVM.predict(X_test)
	ans.append(predicted_value[0])
	print('predicted value: ',predicted_value[0])
	index.append(i+1)
	i = i +1
df = DataFrame({'ImageId': index, 'Label': ans})
df.to_excel('submit.xlsx', sheet_name='sheet1', index=False)
