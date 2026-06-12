from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')

model_path = 'model/model.joblib'
model = None

def load_model():
    global model
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}")
    else:
        print(f"ERROR: Model not found at {model_path}")
        print("Please run 'python setup.py' first to initialize the model.")
        exit(1)

load_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    review_text = request.form.get('review', '').strip()
    
    if not review_text or len(review_text) < 3:
        flash('Please enter a valid review (at least 3 characters)', 'error')
        return redirect(url_for('index'))
    
    prediction = model.predict([review_text])[0]
    
    if prediction == 'positive':
        return render_template('result_good.html', review=review_text)
    elif prediction == 'negative':
        return render_template('result_bad.html', review=review_text)
    else:
        return render_template('result_neutral.html', review=review_text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
