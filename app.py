from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

#Load the ML model
model = pickle.load(open('./models/phishing.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template('index.html')

    
@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('urlInput')
    
    prediction = model.predict([url])
    prediction_text = 'This is good url' if prediction[0] == 'good' else 'This is bad url'
    
    return render_template('index.html', prediction_text=prediction_text)


if __name__ == '__main__':
    app.run(debug=True)
