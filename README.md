# 🏠 House Rent Prediction Pipeline

An end-to-end Machine Learning application for predicting monthly house rent across multiple Indian cities. This project demonstrates the complete ML workflow, including data preprocessing, hyperparameter optimization, experiment tracking, model evaluation, Docker containerization, and deployment using Streamlit and Hugging Face Spaces.

---

## 🚀 Live Demo

🔗 **Hugging Face:** *(Add your deployed Hugging Face Space URL here after deployment)*

---

## 📌 Project Overview

This project predicts house rent for residential properties in four Indian cities:

- Mumbai
- Pune
- Delhi
- Hisar

The objective is to build a production-ready machine learning pipeline by comparing multiple hyperparameter optimization techniques, tracking experiments, deploying an interactive web application, and containerizing the solution for easy deployment.

---

## ✨ Features

- Data preprocessing and feature encoding
- House rent prediction using Machine Learning
- Hyperparameter optimization using:
  - Grid Search
  - Random Search
  - Bayesian Optimization (Optuna)
- Experiment tracking with Trackio
- Interactive Streamlit web application
- Docker containerization
- Deployment on Hugging Face Spaces

---

# 📂 Project Structure

```text
house-rent-prediction-pipeline
│
├── app.py                  # Streamlit application
├── train.ipynb             # Model training notebook
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── README.md
│
├── dataset/
│
├── models/
│   ├── trained_model.pkl
│   ├── label_encoders.pkl
│   └── feature_columns.pkl
│
├── plots/
│
└── screenshots/
```

---

# ⚙️ Machine Learning Pipeline

The project follows the complete machine learning workflow:

```text
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Encoding
    │
    ▼
Model Training
    │
    ▼
Hyperparameter Optimization
(Grid Search • Random Search • Bayesian Optimization)
    │
    ▼
Experiment Tracking
    │
    ▼
Model Evaluation (MAE)
    │
    ▼
Save Best Model
    │
    ▼
Streamlit Application
    │
    ▼
Docker Container
    │
    ▼
Hugging Face Deployment
```

---

# 📊 Model Training

Model development is implemented in **train.ipynb**.

The training pipeline includes:

- Data preprocessing
- Label Encoding for categorical features
- Train-test split
- Cross-validation
- Hyperparameter tuning
- Model evaluation using Mean Absolute Error (MAE)

Three optimization techniques were compared:

- Grid Search
- Random Search
- Bayesian Optimization (Optuna)

The best-performing model is selected and saved for inference.

---

# 📈 Experiment Tracking

Experiments are tracked using **Trackio**, allowing comparison of:

- Hyperparameters
- Cross-validation scores
- Model performance
- Best experiment

---

# 🌐 Streamlit Application

The project includes an interactive Streamlit web application where users can:

- Enter property details
- Predict monthly house rent
- View prediction results instantly

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

# 🐳 Docker Support

The application is fully containerized using Docker.

### Build the Docker image

```bash
docker build -t house-rent-prediction .
```

### Run the container

```bash
docker run -p 7860:7860 house-rent-prediction
```

Access the application at:

```
http://localhost:7860
```

---

# 🤗 Deployment

The application is deployed on **Hugging Face Spaces** using Docker.

**Live Demo:**

👉 *(Add your Hugging Face Space link here after deployment.)*

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/house-rent-prediction-pipeline.git
```

Navigate to the project directory:

```bash
cd house-rent-prediction-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the application:

```bash
streamlit run app.py
```

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Optuna
- Trackio
- Streamlit
- Docker
- Hugging Face Spaces
- Matplotlib

---

# 📸 Screenshots

The `screenshots/` folder contains:

- Streamlit User Interface
- Docker Build Process
- Running Docker Container
- Model Optimization Results

---

# 📄 License

This project is developed for educational and portfolio purposes.

---

## 👤 Author

**Divya Sidda**

B.Tech Artificial Intelligence  
Indian Institute of Technology Gandhinagar