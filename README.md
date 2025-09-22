# Content-Monetization-Modeler

Predict YouTube Ad Revenue with Machine Learning

##Project Overview

The Content Monetization Modeler is a data-driven machine learning project designed to help YouTube creators, advertisers, and media companies estimate and optimize their ad revenue. As digital platforms increasingly rely on advertising for income, creators need predictive insights to guide their content strategy, financial planning, and audience engagement.

This project demonstrates the end-to-end machine learning pipeline, starting from raw data to deployment as an interactive Streamlit web app. It covers exploratory data analysis, data preprocessing, feature engineering, regression modeling, model evaluation, and visualization of insights.

As creators and media companies rely more on platforms like YouTube, predicting ad revenue is crucial for content strategy and business planning. This project builds a machine learning model to forecast revenue per video based on engagement, audience demographics, and content metadata — and delivers it through an interactive Streamlit dashboard.

##table of contents
project description
dataset insight
tech stack
key features
documentation
dashboard
project structure
faqs

##Goal
The primary goal of the Content Monetization Modeler is to predict YouTube ad revenue for individual videos using machine learning models, and make the results accessible via an interactive Streamlit app.

This enables content creators and media companies to:

Forecast expected ad revenue for upcoming videos.
Identify which content features (views, watch time, engagement, etc.) drive monetization.
Use data-driven insights to improve content strategy and revenue planning.

##📊 Dataset Insight
The dataset contains daily performance and contextual information for YouTube videos, including:

Video ID – Unique identifier for each video
Date – Upload/reporting date
Views – Number of video views
Likes & Comments – Engagement metrics from viewers
Watch Time (minutes) – Total time spent watching
Video Length (minutes) – Duration of the video
Subscribers – Channel’s subscriber count at the time
Category – Content category (e.g., Tech, Music, Gaming)
Device – Platform used (Mobile, Desktop, TV, etc.)
Country – Viewer’s geographical location
Ad Revenue (USD) – Target variable, representing daily ad revenue earned

##Tech Stack
Python – Core programming language for data analysis and modeling
Pandas – Data manipulation, cleaning, and wrangling
NumPy – Numerical computations and preprocessing
Scikit-learn – Machine learning models, preprocessing, and evaluation
XGBoost – Gradient boosting model for regression tasks
Matplotlib / Seaborn – Data visualization and statistical plots
Streamlit – Interactive web application for model deployment
Pickle – Model serialization and saving pipelines

##Key Features
Ad Revenue Prediction – Estimate YouTube video ad revenue based on performance & contextual metrics
Engagement Metrics Analysis – Study the effect of likes, comments, views, and watch-time on revenue
Feature Engineering – Create derived features such as engagement rate, revenue per view, etc.
Outlier Detection & Handling – Identify and treat anomalies in views, revenue, and engagement metrics
Categorical Encoding – Convert categorical features (category, device, country) into machine-readable format
Exploratory Data Analysis (EDA) – Revenue distribution plots, correlation heatmaps, and feature importance
Model Comparison – Evaluate multiple regression models (Linear, Ridge, Lasso, Random Forest, XGBoost)
Interactive Streamlit App – Input custom video metrics and instantly predict expected ad revenue
Visual Insights Dashboard – Revenue distribution, feature importance, and correlation visualizations inside the app

##Dashboard
The dashboard includes the following insights:

Input Controls – Users can enter video metrics (views, likes, comments, watch time, subscribers) along with metadata (upload date, category, device, country).
KPI Card – Displays the predicted revenue for the video in a highlighted box.
Summary Panel – Shows the entered metrics and metadata for easy verification.
Comparison Visuals (optional) – Feature importance plots and revenue distribution graphs from the training pipeline help understand model behavior.
Interactive Workflow – Real-time prediction powered by the trained XGBoost pipeline.

##Project Structure
📁 Youtube Project/
│
├── 📄 models.py # Full pipeline: EDA → Preprocessing → Modeling
├── 📄 app.py # Streamlit dashboard for revenue prediction
├── 📄 youtube_ad_revenue_dataset (1).csv # Dataset (synthetic YouTube video stats)
│
├── 📂 models/ # Saved ML pipelines & scalers
│ ├── pipe_xgb.pkl # Trained XGBoost pipeline
│ └── y_scaler.pkl # Target scaler for inverse transform
││
├── 📄 requirements.txt # Project dependencies
└── 📄 README.md # Documentation

##FAQs
What is this project about?
A machine learning project that predicts YouTube ad revenue for videos based on engagement and metadata features. It includes an end-to-end pipeline with EDA, preprocessing, model building, and a Streamlit app for deployment.

What insights are provided?

Feature importance for revenue prediction
Correlation between engagement metrics (views, likes, comments, watch-time) and ad revenue
Model comparison across ML algorithms (Linear Regression, Random Forest, XGBoost)
Prediction of expected ad revenue for new video data
What technologies are used?
Python – Core development
Pandas – Data cleaning & wrangling
NumPy – Numerical computations
Scikit-learn – Machine learning pipelines
XGBoost – Gradient boosting for accurate predictions
Matplotlib / Seaborn – Visualization
Streamlit – Interactive web app for predictions
How to run the project?
pip install -r requirements.txt
streamlit run app.py
Can I contribute? Yes! Fork the repo, make your changes, and raise a pull request. All contributions are welcome 🚀
