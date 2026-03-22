# 🚀 Term Deposit Subscription Prediction (Portfolio Project)

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![ML](https://img.shields.io/badge/Machine%20Learning-XGBoost-green)
![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Deployment-Docker-blue?logo=docker)

---

## 🌟 Project Snapshot

An end-to-end machine learning system that predicts whether a customer will subscribe to a term deposit, built with a strong focus on **business impact and deployment**.

---

## 🖥️ Live App Preview

### 📊 Streamlit Interface
![App Screenshot](images/streamlit_app.png)

### 🔮 Prediction Output
![Prediction Screenshot](images/prediction_output.png)

> 📌 *Replace the images above with actual screenshots from your app (store them in an `images/` folder in your repo).*

---

## 🧠 Problem

Banks need to identify high-probability customers to:
- Improve conversion rates
- Reduce marketing costs
- Optimize outreach strategies

---

## ⚙️ Solution

✔ Built a classification model using **XGBoost**  
✔ Handled class imbalance  
✔ Tuned decision threshold for business performance  
✔ Deployed via **Flask API + Streamlit UI**

---

## 🔄 Workflow Overview

```mermaid
flowchart LR
    A[Raw Data] --> B[EDA]
    B --> C[Preprocessing]
    C --> D[Modeling]
    D --> E[Evaluation]
    E --> F[Optimization]
    F --> G[Deployment]
```

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    User --> UI[Streamlit App]
    UI --> API[Flask API]
    API --> Model[XGBoost Model]
    API --> Preprocessor
    Model --> Result[Prediction]
```

---

## 📊 Results

| Metric     | Score |
|-----------|------|
| Accuracy  | 0.89 |
| Precision | 0.86 |
| Recall    | 0.93 |
| F1 Score  | 0.89 |

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- XGBoost
- Flask
- Streamlit
- Docker

---

## 🚀 Run Locally

```bash
git clone https://github.com/samuelmugisha/ttYINgpDAx5aUBwk.git
cd ttYINgpDAx5aUBwk
```

Backend:
```bash
cd backend_files
pip install -r requirements.txt
python app.py
```

Frontend:
```bash
cd frontend_files
pip install -r requirements.txt
streamlit run app.py
```

---

## 💼 Why This Project Stands Out

- End-to-end ML pipeline (not just notebooks)
- Business-driven model decisions
- Real deployment architecture
- Clean, modular, production-style structure

---

## 🎯 For Recruiters

This project highlights my ability to:
- Build ML systems from scratch
- Think in terms of business impact
- Deploy models into usable applications
- Communicate insights clearly

---

## ⭐ Final Note

This is the kind of work I aim to bring into real-world teams:  
**practical, scalable, and impact-driven machine learning.**
