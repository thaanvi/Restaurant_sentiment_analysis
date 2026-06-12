import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np

def initialize_model():
    model_dir = 'model'
    model_path = os.path.join(model_dir, 'model.joblib')
    
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    if os.path.exists(model_path):
        print(f"Model already exists at {model_path}")
        print("Delete model/model.joblib to retrain with new data")
        return
    
    print("Initializing sentiment analysis model with enhanced training data...")
    
    reviews = [
        "The food was absolutely amazing and delicious! Best meal ever!",
        "Excellent service, wonderful atmosphere, highly recommend!",
        "Outstanding restaurant! The chef is incredible, loved everything!",
        "Fantastic experience! Fresh ingredients, perfect seasoning!",
        "Superb quality! Will definitely come back, worth every penny!",
        "Brilliant restaurant! Amazing flavors, great presentation!",
        "Loved it! The staff was friendly and food was exceptional!",
        "Perfect dining experience! Everything was cooked to perfection!",
        "Highly recommend! Delicious food, great ambiance!",
        "Best restaurant in town! Amazing service and quality!",
        "Wonderful meal! The taste was incredible, so fresh!",
        "Absolutely fantastic! Great portions, excellent value!",
        "Top-notch quality! Loved the menu, will return soon!",
        "Incredible restaurant! Beautiful presentation, tasty food!",
        "Five stars! Everything was perfect, highly satisfied!",
        "Amazing place! Great food, friendly staff, clean environment!",
        "Excellent choice! Delicious dishes, reasonable prices!",
        "Loved every bite! The flavors were outstanding!",
        "Great restaurant! Fresh ingredients, well-prepared meals!",
        "Highly impressed! Quality service and amazing food!",
        "Terrible food, very disappointing and unpleasant!",
        "Worst restaurant ever! Horrible service, awful food!",
        "Disgusting meal! Poor quality, would not recommend!",
        "Awful experience! Cold food, rude staff, never again!",
        "Very bad! Overpriced, tasteless, complete waste of money!",
        "Horrible place! Dirty, slow service, bad food!",
        "Disappointing! Undercooked food, unfriendly waiters!",
        "Not good at all! Poor hygiene, terrible taste!",
        "Waste of time and money! Awful service!",
        "Never coming back! Bad quality, unpleasant atmosphere!",
        "Terrible service! Food was cold and stale!",
        "Worst meal I've had! Horrible taste, poor presentation!",
        "Awful restaurant! Rude staff, bad management!",
        "Very disappointing! Overpriced for such poor quality!",
        "Bad experience! Long wait, mediocre food!",
        "Not recommended! Terrible food, dirty tables!",
        "Horrible! Unfriendly service, tasteless dishes!",
        "Complete disaster! Everything was wrong!",
        "Very poor! Bad ingredients, terrible cooking!",
        "Worst dining experience! Avoid this place!",
        "The food was okay, nothing special really.",
        "Average restaurant, meets basic expectations.",
        "It was fine, neither impressive nor bad.",
        "Decent place, acceptable quality and service.",
        "Normal experience, nothing to complain about.",
        "Alright restaurant, standard food and atmosphere.",
        "Fair enough, moderate portions and taste.",
        "So-so dining experience, pretty average overall.",
        "Not bad, but nothing extraordinary either.",
        "Mediocre food, acceptable but not memorable.",
        "Regular restaurant, met my basic needs.",
        "Standard quality, nothing remarkable or terrible.",
        "Okay meal, could be better but acceptable.",
        "Moderate experience, neither good nor poor.",
        "Acceptable service, average food quality.",
        "Fair restaurant, nothing stands out particularly.",
        "Decent enough, met minimum expectations.",
        "Average all around, typical restaurant experience.",
        "It was alright, nothing special to mention.",
        "Passable quality, neither recommend nor discourage.",
        "Love this place! The pasta is amazing!",
        "Great pizza! Fresh toppings and crispy crust!",
        "Excellent sushi! Very fresh fish!",
        "Delicious burgers! Juicy and flavorful!",
        "Wonderful steak! Cooked exactly right!",
        "Tasty tacos! Authentic Mexican flavors!",
        "Amazing desserts! The cake was heavenly!",
        "Great breakfast! Fluffy pancakes and crispy bacon!",
        "Fantastic seafood! Lobster was perfect!",
        "Delicious soup! Warm and comforting!",
        "Awful pizza! Burnt and tasteless!",
        "Terrible pasta! Overcooked and mushy!",
        "Bad sushi! Not fresh at all!",
        "Horrible burger! Dry and flavorless!",
        "Terrible steak! Tough and overcooked!",
        "Disgusting tacos! Old ingredients!",
        "Bad dessert! Too sweet and artificial!",
        "Awful breakfast! Cold eggs and burnt toast!",
        "Poor seafood! Fishy smell, not fresh!",
        "Terrible soup! Watery and bland!",
        "The salmon was okay, nothing amazing.",
        "Average pizza, standard quality.",
        "Decent burger, met expectations.",
        "Fair pasta, nothing special.",
        "Okay steak, acceptable taste.",
        "Regular tacos, normal flavors.",
        "Standard dessert, typical sweetness.",
        "Acceptable breakfast, basic quality.",
        "Moderate seafood, average freshness.",
        "Fair soup, standard ingredients."
    ]
    
    labels = [
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",
        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "positive", "positive", "positive", "positive", "positive",
        "positive", "positive", "positive", "positive", "positive",
        "negative", "negative", "negative", "negative", "negative",
        "negative", "negative", "negative", "negative", "negative",
        "neutral", "neutral", "neutral", "neutral", "neutral",
        "neutral", "neutral", "neutral", "neutral", "neutral"
    ]
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=2000, ngram_range=(1, 3), min_df=1)),
        ('classifier', LogisticRegression(max_iter=2000, C=1.0, random_state=42, class_weight='balanced'))
    ])
    
    print(f"Training model on {len(reviews)} restaurant reviews...")
    print(f"  - Positive examples: {labels.count('positive')}")
    print(f"  - Negative examples: {labels.count('negative')}")
    print(f"  - Neutral examples: {labels.count('neutral')}")
    
    pipeline.fit(reviews, labels)
    
    joblib.dump(pipeline, model_path)
    print(f"\n✓ Model successfully trained and saved to {model_path}")
    print("Setup complete! You can now run 'python app.py' to start the application.")

if __name__ == "__main__":
    initialize_model()
