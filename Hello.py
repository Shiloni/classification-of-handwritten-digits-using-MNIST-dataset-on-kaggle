from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import pandas as pd 
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import logging
import logging.handlers
import joblib 

app = Flask(__name__)

def savepickle(data, filename):
    """Saves the data into pickle format"""
   #  save_documents = open(filename +'.pickle', 'wb')
    joblib.dump(data, filename)
   #  save_documents.close()

def loadpickle(data_filepath):
    #Loads up the pickled dataset for further parsing and preprocessing
   #  documents_f = open(data_filepath+'.pickle', 'rb')
    data = joblib.load(data_filepath)
   #  documents_f.close()
    
    return data

def train():
   
   data_path = "train.csv"
   df = pd.read_csv(data_path)

   scaler = StandardScaler()
   scaler.fit(df.ix[1:30000,1:785])

   X_train =scaler.transform(df.ix[1:30000,1:785])
   y_train =df.ix[1:30000,0:1]

   print('using support vector machines : ')
   SVM = SVC().fit(X_train , y_train)
   print('accuracy on training set : ',SVM.score(X_train,y_train))
   savepickle(SVM,'model.pkl')


def test(SVM):
   data_path = "test.csv"
   test = pd.read_csv(data_path)

   scaler = StandardScaler()
   scaler.fit(test.ix[:,:])

   ans = []
   index =[]
   i= 0
   while i<280:
      X_test = scaler.transform(test.ix[i:i,0:784])
      predicted_value = SVM.predict(X_test)
      ans.append(predicted_value[0])
      print('predicted value: ',predicted_value[0])
      index.append(i+1)
      i = i +1
   df = pd.DataFrame({'ImageId': index, 'Label': ans})
   df.to_excel('submit.xlsx', sheet_name='sheet1', index=False)

@app.route('/')
def form():
   return render_template('hello.html')

@app.route('/',methods=['POST'])
def form_post():
   text= request.form['text']
   tt = text.upper()
   if (tt=='YES'):
      return redirect(url_for('upload_file'))  
   elif (tt=='NO'):
      return redirect(url_for('upload_file1'))   

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
@app.route('/test')
def upload_file1():
   return render_template('upload1.html')	

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      print(f.filename)
      f.filename = 'train.csv'
      f.save(secure_filename(f.filename))
      train()
      
      return render_template('upload1.html')	

@app.route('/uploader1', methods = ['GET', 'POST'])
def upload_file3():
   if request.method == 'POST':
      f = request.files['file']
      f.filename = 'test.csv'
      f.save(secure_filename(f.filename))
      #train()
      mod = loadpickle('model.pkl')
      test(mod)
      return ("file uploaded successfully")


if __name__ == '__main__':
   handler = logging.handlers.RotatingFileHandler('log.txt',maxBytes=1024 * 1024)
   #handler.setFormatter(formatter)
   logging.getLogger('werkzeug').setLevel(logging.DEBUG)
   logging.getLogger('werkzeug').addHandler(handler)
   app.logger.setLevel(logging.WARNING)
   app.logger.addHandler(handler)
   app.run(debug=True)