import argparse
import pandas as pd
import joblib
import os
import sys

def batch_predict(input_file, output_file):
    model_path = 'model/model.joblib'
    
    if not os.path.exists(model_path):
        print(f"ERROR: Model not found at {model_path}")
        print("Please run 'python setup.py' first to initialize the model.")
        sys.exit(1)
    
    if not os.path.exists(input_file):
        print(f"ERROR: Input file '{input_file}' not found.")
        sys.exit(1)
    
    print(f"Loading model from {model_path}...")
    model = joblib.load(model_path)
    
    print(f"Reading reviews from {input_file}...")
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"ERROR: Failed to read CSV file: {e}")
        sys.exit(1)
    
    if 'review' not in df.columns:
        print("ERROR: Input CSV must contain a 'review' column.")
        sys.exit(1)
    
    print(f"Predicting sentiment for {len(df)} reviews...")
    predictions = model.predict(df['review'])
    
    df['predicted_sentiment'] = predictions
    
    df.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")
    print(f"Successfully processed {len(df)} reviews!")
    
    print("\nSentiment distribution:")
    print(df['predicted_sentiment'].value_counts())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Batch predict sentiment for restaurant reviews')
    parser.add_argument('--input', required=True, help='Input CSV file with review column')
    parser.add_argument('--output', required=True, help='Output CSV file for predictions')
    
    args = parser.parse_args()
    
    batch_predict(args.input, args.output)
