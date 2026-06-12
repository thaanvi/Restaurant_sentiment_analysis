# Restaurant Review Sentiment Analysis System

A Flask-based web application that analyzes restaurant reviews and classifies them as positive, negative, or neutral using machine learning.

## System Requirements

- **Operating System**: macOS Monterey+, Ubuntu 20.04+, or Windows 10+
- **RAM**: 8GB minimum, 16GB recommended
- **Python**: Python 3.9 or higher
- **Web Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)
- **GPU**: Optional (not required for this application)

## Installation

Follow these steps to set up and run the application:

### 1. Install Python 3.9+

Make sure you have Python 3.9 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```

### 2. Install Dependencies

Install all required packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Initialize the Model

Run the setup script to create and train the initial sentiment analysis model:

```bash
python setup.py
```

This will create a `model/model.joblib` file with a pre-trained model using demo restaurant review data.

### 4. Start the Application

Launch the Flask web server:

```bash
python app.py
```

### 5. Open in Browser

Open your web browser and navigate to:

```
http://localhost:5000
```

## How to Use

### Single Review Prediction

1. Open the application in your web browser
2. Enter a restaurant review in the text area
3. Click the "Predict" button
4. View the sentiment analysis result (Positive, Negative, or Neutral)
5. Click "Try another review" to analyze another review

### Batch Prediction (Multiple Reviews)

To analyze multiple reviews at once from a CSV file:

```bash
python batch_predict.py --input reviews.csv --output results.csv
```

**Input CSV Format:**
- Must contain a column named `review` with the review text

**Output:**
- Creates a new CSV file with the original reviews and predicted sentiments

### Model Retraining

To retrain the model with your own labeled data:

```bash
python retrain.py --data new_data.csv
```

**Training CSV Format:**
- Must contain two columns: `review` and `label`
- Labels should be: `positive`, `negative`, or `neutral`

After retraining, restart the application to use the new model.

## Stopping the Application

To stop the Flask server, press `Ctrl + C` in the terminal where it's running.

## Project Structure

```
.
├── app.py                 # Main Flask application
├── setup.py               # Model initialization script
├── batch_predict.py       # Batch prediction CLI tool
├── retrain.py             # Model retraining CLI tool
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── index.html         # Main input page
│   ├── result_good.html   # Positive result page
│   ├── result_bad.html    # Negative result page
│   ├── result_neutral.html # Neutral result page
│   └── 404.html           # Error page
├── static/                # Static assets
│   └── css/
│       └── style.css      # Application styles
└── model/                 # Machine learning model
    └── model.joblib       # Saved model file
```

## Features

- **Real-time Sentiment Analysis**: Instant classification of restaurant reviews
- **Three Sentiment Categories**: Positive, negative, and neutral classifications
- **Interactive Web Interface**: Clean, user-friendly design
- **Batch Processing**: Analyze multiple reviews from CSV files
- **Model Retraining**: Update the model with new data
- **Custom Error Pages**: Friendly 404 error handling

## Technologies Used

- **Flask**: Web framework
- **scikit-learn**: Machine learning (TfidfVectorizer, LogisticRegression)
- **pandas**: Data processing
- **joblib**: Model serialization
- **numpy**: Numerical operations

## Configuration

### Debug Mode

By default, the application runs in production mode with debug disabled for security. To enable debug mode for local development, set the `FLASK_DEBUG` environment variable:

```bash
export FLASK_DEBUG=true
python app.py
```

**Important**: Never enable debug mode in production environments as it exposes security vulnerabilities.

## Troubleshooting

### Model Not Found Error

If you see "Model not found" error, run:

```bash
python setup.py
```

### Port Already in Use

If port 5000 is already in use, you can modify the port in `app.py`:

```python
app.run(host='0.0.0.0', port=8000, debug=debug_mode)
```

### CSV Format Issues

Ensure your CSV files have the correct column names:
- Batch prediction: `review` column
- Retraining: `review` and `label` columns

## License

This project is provided as-is for educational and demonstration purposes.
