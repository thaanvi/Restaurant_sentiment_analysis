# Restaurant Review Sentiment Analysis System

## Overview
A Flask-based web application that analyzes restaurant reviews and classifies them as positive, negative, or neutral using machine learning (scikit-learn LogisticRegression with TfidfVectorizer).

**Current State**: Fully functional MVP with web interface, batch processing, and model retraining capabilities.

## Recent Changes
- **November 21, 2025**: Enhanced model training and initial setup
  - Created complete Flask application with sentiment analysis
  - Implemented web UI with teal gradient header and result pages
  - Added batch prediction and model retraining CLI tools
  - Configured workflow to run on port 5000
  - Enhanced model with 90 diverse training examples (30 positive, 30 negative, 30 neutral)
  - Improved TF-IDF parameters (2000 features, trigrams, balanced class weights)
  - Verified accurate predictions across all sentiment categories

## Project Architecture

### Backend Structure
- **app.py**: Main Flask application
  - Routes: `/` (home), `/predict` (POST for predictions), 404 handler
  - Loads pre-trained model from `model/model.joblib`
  - Runs on port 5000 with host 0.0.0.0
  
- **setup.py**: Model initialization script
  - Creates and trains LogisticRegression model with enhanced parameters
  - Uses 90 diverse restaurant reviews (30 positive, 30 negative, 30 neutral)
  - Improved feature extraction: 2000 TF-IDF features with trigrams
  - Balanced class weights for better accuracy
  - Saves model to `model/model.joblib`
  
- **batch_predict.py**: CLI tool for bulk predictions
  - Usage: `python batch_predict.py --input reviews.csv --output results.csv`
  - Processes CSV files with 'review' column
  
- **retrain.py**: CLI tool for model updates
  - Usage: `python retrain.py --data new_data.csv`
  - Expects CSV with 'review' and 'label' columns

### Frontend Structure
- **templates/**: Jinja2 HTML templates
  - `index.html`: Main input page with teal gradient header
  - `result_good.html`: Positive sentiment result with thumbs-up emoji
  - `result_bad.html`: Negative sentiment result with sad emoji
  - `result_neutral.html`: Neutral sentiment result with neutral emoji
  - `404.html`: Custom error page
  
- **static/css/style.css**: All application styling
  - Teal-to-blue gradient header for index page
  - Dark green (#556B2F) headers for result pages
  - Responsive design with mobile breakpoints

### Machine Learning
- **Pipeline**: TfidfVectorizer + LogisticRegression
- **Features**: TF-IDF with max 1000 features, bigrams (1,2)
- **Classes**: positive, negative, neutral
- **Storage**: Joblib serialization in `model/model.joblib`

## Dependencies
- Flask 3.0.0 (web framework)
- scikit-learn 1.3.2 (ML pipeline)
- pandas 2.1.3 (CSV processing)
- joblib 1.3.2 (model serialization)
- numpy 1.26.2 (numerical operations)

## User Preferences
None specified yet.

## Quick Start
1. Run `python setup.py` (if model doesn't exist)
2. Run `python app.py` or use the Flask App workflow
3. Access at http://localhost:5000

## Notes
- Model must be initialized before running the app
- Port 5000 is required for Replit webview
- SESSION_SECRET environment variable is used for Flask sessions
