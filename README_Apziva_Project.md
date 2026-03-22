# Term Deposit Subscription Prediction

An end-to-end machine learning project focused on predicting whether a bank customer will subscribe to a term deposit, using historical direct marketing campaign data and deploying the solution as an interactive application.

---

## Project Summary

This project was completed as part of an Apziva engagement and demonstrates a full machine learning workflow from business understanding to deployment.

The objective was to help a banking-focused business improve outbound marketing performance by identifying customers who are more likely to subscribe to a term deposit. Beyond building a predictive classifier, the project also explored customer segmentation so business teams can prioritize higher-value prospects and better understand the characteristics of likely subscribers.

The repository shows work across:
- exploratory data analysis
- preprocessing and class imbalance handling
- model training and comparison
- threshold optimization
- customer clustering for segmentation
- backend and frontend deployment assets

---

## Business Problem

Banks spend significant time and resources contacting customers during marketing campaigns. A poor targeting strategy increases operational cost, wastes call-center effort, and lowers campaign efficiency.

This project addresses that challenge by building a classification system that predicts subscription likelihood before outreach decisions are made. The end goal is to help business teams:
- target customers more effectively
- improve campaign conversion rates
- reduce wasted outreach
- understand the attributes associated with stronger purchase intent

---

## Objective

Build a robust and interpretable machine learning solution that predicts whether a customer will subscribe to a term deposit and surfaces actionable business insights about the customer segments most worth prioritizing.

---

## Repository Structure

```text
.
├── backend_files/
│   ├── app.py
│   ├── Dockerfile
│   ├── final_subscription_model.joblib
│   ├── final_subscription_model.json
│   ├── preprocessor.joblib
│   └── requirements.txt
├── data/
├── frontend_files/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── note
├── models/
│   └── XGBClassifier_best_model_threshold.joblib
├── notebooks/
│   ├── Clustering.ipynb
│   ├── Deployment.ipynb
│   ├── EDA.ipynb
│   ├── Modelling.ipynb
│   └── Preprocessing.ipynb
└── README.md
```

---

## Dataset and Prediction Target

The model uses anonymized direct marketing campaign data from a European banking institution.

### Input features include
- demographic attributes such as age, job, marital status, and education
- financial indicators such as balance, housing loan, and personal loan
- campaign interaction details such as contact type, day, month, duration, and number of contacts

### Target variable
- `y`: whether the customer subscribed to a term deposit

This is a binary classification problem.

---

## Step-by-Step Project Flow

### 1. Problem Framing and Success Criteria
The project started with translating the business question into a machine learning task: predict whether a customer will subscribe to a term deposit. The original benchmark was to exceed 81% accuracy while still producing a practically useful model for business decision-making.

### 2. Exploratory Data Analysis
The dataset was examined to understand feature distributions, class balance, and campaign behavior. This stage helped identify:
- dominant job categories and customer demographics
- strong imbalance in the target variable
- campaign timing patterns by month
- opportunities to derive business insight from both customer and contact features

### 3. Data Preprocessing
The raw data was prepared for modeling through a structured preprocessing workflow. This included:
- separating predictors from the target
- transforming categorical features into machine-readable form
- scaling numeric variables
- preparing a reusable preprocessing object for deployment
- handling class imbalance through resampling so the model could better learn the minority subscription class

### 4. Model Development and Comparison
Multiple classification algorithms were evaluated to determine the best-performing approach. The experimentation included:
- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- XGBoost

This comparison stage demonstrates a thoughtful modeling process rather than jumping directly to a single algorithm.

### 5. Hyperparameter Tuning
The stronger candidate models were tuned to improve generalization and business usefulness. Cross-validation and parameter search were used to refine performance.

### 6. Threshold Optimization
Instead of stopping at the default decision threshold, the project explicitly optimized the classification threshold using F1-score. This is important because the business problem involves balancing false positives and false negatives, not just maximizing raw accuracy.

### 7. Customer Segmentation with Clustering
The work extended beyond prediction into segmentation. Customers who subscribed were grouped into clusters to identify meaningful business segments. This makes the solution more actionable for marketing teams by highlighting which customer profiles are most promising.

### 8. Model Packaging and Deployment
The trained artifacts were serialized and prepared for serving. The repository includes:
- a Flask backend API for inference
- a Streamlit frontend for interactive prediction
- Dockerfiles for containerized deployment
- model and preprocessing artifacts for reproducible inference

This shows the project was taken beyond notebook experimentation into deployable application form.

---

## Modeling Approach

A major strength of this project is that it does not treat model building as a purely academic exercise. The workflow reflects real-world machine learning practice:

- start with business understanding
- inspect and clean the data
- address target imbalance
- compare several models
- optimize the decision threshold
- package the solution for use by others

The final modeling direction centered on **XGBoost**, with additional threshold tuning to improve the precision-recall tradeoff.

---

## Performance Snapshot

From the modeling notebook, the final tuned threshold delivered results around:

- **Accuracy:** 89.13%
- **Precision:** 86.00%
- **Recall:** 92.80%
- **F1-score:** 89.27%
- **Optimal threshold:** 0.52

These results exceeded the original success benchmark and show a balanced classifier that performs well on both precision and recall, which is especially important in an imbalanced campaign-response setting.

---

## Business Insights and Segment Interpretation

The project was not limited to answering *who might subscribe*; it also explored *why* and *which groups should be prioritized*.

The clustering work suggests that likely subscribers can be organized into distinguishable segments based on features such as:
- age
- balance
- job type
- education level
- loan profile
- home ownership or housing-loan behavior

This makes the project valuable from both an analytics and strategy perspective. Instead of giving business stakeholders only a prediction score, it also provides a basis for segment-driven marketing decisions.

---

## Deployment Architecture

### Backend
The backend is implemented with **Flask** and loads:
- the trained XGBoost model
- a serialized preprocessing pipeline

It exposes a prediction endpoint that receives customer input, transforms it through the preprocessing pipeline, and returns a subscription prediction.

### Frontend
The frontend is implemented with **Streamlit** and provides a lightweight user interface for testing predictions interactively.

### Containerization
Both frontend and backend include **Dockerfiles**, which indicates deployment readiness and a clear separation between model serving and user interface concerns.

---

## Tools and Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Imbalanced-learn
- Joblib
- Flask
- Streamlit
- Docker

---

## What This Project Demonstrates

This project highlights several strengths that are relevant to hiring managers and recruiters:

### End-to-end ownership
The work spans problem definition, analysis, feature preparation, model experimentation, evaluation, threshold tuning, segmentation, and deployment.

### Business alignment
The project connects technical modeling choices to business outcomes such as campaign efficiency, better prospect targeting, and improved decision support.

### Practical ML engineering
The inclusion of serialized artifacts, API logic, frontend integration, and Docker support shows an ability to move beyond notebooks into usable systems.

### Analytical depth
The addition of clustering and threshold optimization shows maturity in thinking about machine learning as both a predictive and decision-support tool.

---

## My Contribution

Based on the repository structure and deliverables, this project reflects my contribution across the full machine learning lifecycle:

- analyzed a real business dataset for a customer-subscription prediction use case
- performed preprocessing and class-imbalance handling
- evaluated multiple classification models and selected a strong final approach
- tuned the model and optimized the classification threshold
- explored customer segmentation to support business prioritization
- packaged the solution into backend and frontend components for deployment
- prepared the project in a form that can be reviewed, demonstrated, and extended

---

## How to Review This Project

For a quick technical review, the best order is:

1. `notebooks/EDA.ipynb` – understand the business problem and data landscape
2. `notebooks/Preprocessing.ipynb` – review data preparation and imbalance handling
3. `notebooks/Modelling.ipynb` – see model comparison, tuning, and final performance
4. `notebooks/Clustering.ipynb` – examine customer segmentation work
5. `notebooks/Deployment.ipynb` – review model packaging
6. `backend_files/` and `frontend_files/` – inspect deployable application components

---

## Conclusion for Hiring Managers and Recruiters

This project represents more than building a classifier.

It demonstrates the ability to take a business problem, convert it into a data science workflow, evaluate multiple modeling strategies, optimize the solution for decision-making, and package the result into a deployable application. It also shows an understanding that machine learning projects create the most value when they combine predictive accuracy with operational usability and business insight.

In practical terms, this work shows readiness for roles involving:
- machine learning
- applied data science
- predictive analytics
- ML product development
- deployment-oriented data projects

If you are reviewing my work as a recruiter, hiring manager, or collaborator, this repository is a strong example of how I approach real-world ML problems: with structure, business context, experimentation, and delivery in mind.
