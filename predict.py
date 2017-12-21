import pandas as pd 
from pandas import DataFrame
import pickle
from sklearn.preprocessing import StandardScaler

pickle_in = open("model.pickle","rb")
SVM = pickle.load(pickle_in)

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