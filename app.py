from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('churn_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tenure = int(request.form['tenure'])

    # Create correct input shape (21 features)
    input_data = np.zeros((1, 21))
    input_data[0][0] = tenure

    prediction = model.predict(input_data)

    result = "Customer is likely to Churn" if prediction[0] == 1 else "Customer is likely to Stay"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)