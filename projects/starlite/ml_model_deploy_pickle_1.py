
# coding: utf-8

# # XOR Model | Pickle

import numpy as np
import sklearn
import pickle
import os
from sklearn.neural_network import MLPClassifier as mlpc

os.getcwd()
os.listdir()

xs = np.array([0,0,0,1,1,0,1,1]).reshape(4,2)
ys = np.array([0,1,1,0]).reshape(4,)

mdl = mlpc(activation='relu', max_iter=10000, hidden_layer_sizes=(4,2))
mdl.fit(xs, ys)

filename = 'XOR_model.pkl'

pickle.dump(mdl, open(filename, 'wb'))

os.listdir()


# #### 'XOR_model.pkl' 
# 
# Model has been saved into a 'pkl' file.

# help('modules')


filename = 'XOR_model.pkl'


from flask import Flask, jsonify, request

def xor_predictor(a, b):
    output = {'XOR': 0}
    x_input = np.array([a,b]).reshape(1,2)
    m1 = pickle.load(open(filename, 'rb'))
    output['XOR'] = int(m1.predict(x_input)[0])
    return output

app = Flask(__name__)


#### builtins.TypeError TypeError: Object of type 'int32' is not JSON serializable

#### To avoid this error - use int(m1.predict(x_input)[0])


@app.route("/")
def index():
    return "XOR Predictor!!"


# In[31]:


@app.route("/XOR", methods=['GET'])
def cal_xor_predictor():
    body = request.get_data()
    header = request.headers
    
    try:
        num1 = int(request.args['x1'])
        num2 = int(request.args['x2'])
        if (num1 != None) and (num2 != None) and ((num1 == 0) or (num1 == 1)) and ((num2 == 0) or (num2 == 1)):
            res = xor_predictor(num1, num2)
        else:
            res = {
                'success': False,
                'message': 'invalid inputs; 0 or 1 expected'
            }
    except:
        res = {
            'success': False,
            'message': 'Unknown error'
        }
        
    return jsonify(res)


# In[33]:


if __name__ == "__main__":
    app.run(debug=True, port=8808)

