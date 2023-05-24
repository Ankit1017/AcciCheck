from flask import Flask, render_template, request
import numpy as np
from anmol import inp

app=Flask(__name__)

@app.route('/')
def art():
    return render_template('home.html')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/index/pred', methods=['POST','GET'])
def pred():
    input = dict(request.form)
    # int_features=[double(x) for x in request.form.values()]
    # final=[np.array(int_features)]
    day = input['day'][0]
    time_zone =input['time'][0]
    weather = input['weather'][0]
    data =np.array([weather,time_zone,day])
    lat= input['lat'][0]
    print(data)
    if(lat <=str(27)):
        a=inp(data,'city1.csv.xls')
        print('1')
    elif(lat <=str(28)):
        a=inp(data,'city2.csv.xls')
        print('2')
    else:
        a=inp(data,'city3.csv.xls')
        print('3')
    
    print(a)
    # print(data)
    
    # print(request.form)
    return render_template('index.html',pred1=a)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)
