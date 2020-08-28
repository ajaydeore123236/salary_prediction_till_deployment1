from flask import Flask,render_template,request

import pickle
#from flask_sqlalchemy import SQLAlchemy

app1=Flask(__name__)
@app1.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')
@app1.route('/process',methods=['POST','GET'])
def process1():
    if(request.method=='POST'):
        year_of_exp=request.form['year_of_exp']
        year_of_exp=float(year_of_exp)
        file_name='source_file.pickle'
        load_model=pickle.load(open(file_name,'rb'))
        result=load_model.predict([[year_of_exp]])
        return render_template('result.html', result=result)

if __name__=='__main__':

    app1.run(debug=True)