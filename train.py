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

pickle_out = open("model.pickle","wb")
pickle.dump(SVM, pickle_out)
print("model trained ")

