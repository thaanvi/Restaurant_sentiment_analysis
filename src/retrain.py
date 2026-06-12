import argparse
import pandas as pd
import joblib
import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

def retrain_model(data_file):
    model_path = 'model/model.joblib'
    
    if not os.path.exists(data_file):
        print(f"ERROR: Training data file '{data_file}' not found.")
        sys.exit(1)
    
    print(f"Loading training data from {data_file}...")
    try:
        df = pd.read_csv(data_file)
    except Exception as e:
        print(f"ERROR: Failed to read CSV file: {e}")
        sys.exit(1)
    
    if 'review' not in df.columns or 'label' not in df.columns:
        print("ERROR: Training CSV must contain 'review' and 'label' columns.")
        sys.exit(1)
    
    print(f"Training new model on {len(df)} samples...")
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, ngram_range=(1, 2))),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ])
    
    pipeline.fit(df['review'], df['label'])
    
    model_dir = 'model'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    joblib.dump(pipeline, model_path)
    print(f"Model retrained and saved to {model_path}")
    print("Retraining complete. Restart the app to use the new model.")
    
    print("\nTraining data distribution:")
    print(df['label'].value_counts())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrain sentiment analysis model')
    parser.add_argument('--data', required=True, help='CSV file with review and label columns')
    
    args = parser.parse_args()
    
    retrain_model(args.data)
