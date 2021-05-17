import numpy as np
import pickle
from flask import Flask, render_template, request, redirect, url_for

from sklearn import preprocessing

app = Flask(__name__)

model = pickle.load(open('finalized_model_xgb.pkl', 'rb'))

#print(model.predict(np.array([[1, 2, 34, 45, 333333, 2, 3, 4]])))

@app.route('/')
def home():
    return render_template('index_2.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])


## Predicting with the model
def predict():

    int_features = [[float(x) for x in request.form.values()]]
    print(int_features)
    final_features = np.array(int_features)
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)


    base_score = 600
    pdo = 120
    good_bads = 10

    factor = pdo / np.log(2)
    offset = base_score - factor * np.log(good_bads)
    score_ = offset - factor * np.log(output)
    score_ = round(score_,2)



    return render_template('index_2.html', prediction_text='Your Application Score is :{}'.format(score_))

if __name__ == "__main__":
    app.run(debug=True)