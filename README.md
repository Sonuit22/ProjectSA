Twitter Sentiment Analysis using ML & Transformers
 Project Overview

This project performs Sentiment Analysis on Twitter Airline Dataset using both traditional Machine Learning and modern Transformer-based models.

The goal is to classify tweets into:

Positive 😊

Negative 😡

We implement and compare:

Logistic Regression (Baseline)

BERT (Transformer)

RoBERTa (Advanced Transformer)

🚀 Features

Text preprocessing (cleaning, normalization)

TF-IDF feature extraction

Machine Learning model (Logistic Regression)

Transformer models:

BERT

RoBERTa

Model comparison

Confusion Matrix visualization

Classification report (Precision, Recall, F1-score)

WordCloud visualization

📂 Dataset

We use the Twitter Airline Sentiment Dataset from Kaggle.

Tweets related to airline services

Labeled as positive or negative

🧠 Technologies Used

Python 🐍

Pandas

NumPy

Scikit-learn

PyTorch

Hugging Face Transformers

Matplotlib / Seaborn

WordCloud

🏗️ Project Architecture
Dataset (Twitter Tweets)
        ↓
Text Cleaning
        ↓
Model 1 → TF-IDF + Logistic Regression
Model 2 → BERT
Model 3 → RoBERTa
        ↓
Evaluation (Accuracy, F1-score)
        ↓
Visualization (Confusion Matrix, WordCloud)
📊 Model Performance (Approx)
Model	Accuracy
Logistic Regression	~80–88%
BERT	~88–92%
RoBERTa	~90–95%
⚙️ Installation
pip install pandas numpy scikit-learn transformers datasets torch seaborn matplotlib wordcloud
▶️ How to Run

Open the notebook in Google Colab or Jupyter

Upload dataset (Tweets.csv)

Run all cells step by step

📈 Results

Transformer models outperform traditional ML

RoBERTa achieves the highest accuracy

Visualization helps understand prediction quality

🧪 Example Prediction
Input: "The airline service was terrible"
Output: Negative
📌 Future Work

Add real-time Twitter API integration

Build web app using Streamlit

Use advanced models like FinBERT

Add Explainable AI (SHAP)

👨‍💻 Author
SKR

📄 License

This project is for academic and educational purposes.
