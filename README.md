# AIML Project Series

Welcome to the AIML Project Series repository. This repository contains various projects focused on Artificial Intelligence and Machine Learning. Currently, it includes two projects: a Simple Chatbot and an Admission Chatbot.

## Table of Contents

- [Project 1: Simple Chatbot](#project-1-simple-chatbot)
  - [Overview](#overview)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Usage](#usage)
    
- [Project 2: Admission Chatbot](#project-2-admission-chatbot)
  - [Overview](#overview-1)
  - [Features](#features-1)
  - [Requirements](#requirements-1)
  - [Usage](#usage-1)
- [Installation](#installation)


## Project 1: Simple Chatbot

### Overview

The Simple Chatbot is a basic chatbot implementation that can answer predefined questions. It uses Natural Language Processing (NLP) techniques to preprocess the input questions and provide appropriate responses.

### Features

- Basic question and answer functionality.
- Predefined responses for specific questions.
- Uses NLTK for text preprocessing.
- Implemented using Streamlit for a simple web interface.

### Requirements

- Python 3.x
- Streamlit
- NLTK

### ScreenShots

<img width="1710" alt="Screenshot 2024-05-30 at 20 28 41" src="https://github.com/ankitk75/AIML-Project-Series/assets/116819905/71ca14b2-dd6d-4778-8d3d-a6db501e21e6">


### Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ankitk75/AIML-Project-Series
    ```

2. Navigate to the project directory:

    ```bash
    cd AIML-Project-Series
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run SimpleChatBot.py
    ```

5. Open your web browser and go to `http://localhost:8501` to interact with the chatbot.

## Project 2: Admission Chatbot

### Overview

The Admission Chatbot is designed to assist prospective students with questions related to college admissions. It uses a more sophisticated approach to handle a broader range of queries related to the admission process.

### Features

- Handles a variety of admission-related queries.
- Provides detailed responses based on the user's input.
- Uses advanced NLP techniques for better understanding and response generation.
- Implemented in a Jupyter Notebook for easy experimentation and modification.

### Requirements

- Python 3.x
- NLTK
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- HuggingFace Transformer

### Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ankitk75/AIML-Project-Series
    ```

2. Navigate to the project directory:

    ```bash
    cd AIML-Project-Series
    ```

3. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Open the Jupyter Notebook:

    ```bash
    jupyter notebook Admission_Chatbot.ipynb
    ```

5. Follow the instructions in the notebook to interact with the chatbot and test its functionalities.

## Installation

To install the required dependencies for both projects, you can use the `requirements.txt` file included in the repository:

```bash
pip install -r requirements.txt
```

## Project 3: Heart Disease Prediction

Disease Prediction System using Machine Learning

This repository contains the implementation of a Disease Prediction System using machine learning algorithms. The system predicts the likelihood of a person having heart disease based on various health-related features. The project utilizes multiple machine learning models to analyze historical health data and make predictions, contributing to early disease detection and proactive healthcare management.

Table of Contents

Project Description
Dataset
Features
Installation
Usage
Results
Visualization
Contributing
License
Acknowledgements
Project Description

The "Disease Prediction System using Machine Learning" project aims to develop an intelligent system that predicts the likelihood of heart disease based on various health-related features. The system utilizes machine learning algorithms to analyze historical health data, thereby contributing to early disease detection and proactive healthcare management.

Dataset

The dataset used in this project is the Heart Disease Health Indicators Dataset from Kaggle. It contains various health-related features of individuals, including blood pressure, cholesterol levels, BMI, and smoking status, among others.

Features

The dataset includes the following features:

HighBP
HighChol
CholCheck
BMI
Smoker
Stroke
Diabetes
PhysActivity
Fruits
Veggies
HvyAlcoholConsump
AnyHealthcare
NoDocbcCost
GenHlth
MentHlth
PhysHlth
DiffWalk
Sex
Age
The target variable is HeartDiseaseorAttack, which indicates whether the individual has heart disease or has experienced a heart attack.

Installation

To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using the following command:

bash
Copy code
pip install pandas numpy scikit-learn matplotlib seaborn
Usage

Clone this repository:
bash
Copy code
git clone https://github.com/your-username/disease-prediction-system.git
Navigate to the project directory:
bash
Copy code
cd disease-prediction-system
Run the Jupyter Notebook or Python script to train the models and make predictions.
Results

The system evaluates multiple machine learning models, including Logistic Regression, Decision Tree, Random Forest, and SVM. The performance of each model is measured using accuracy, precision, recall, and F1-score.

Model Performance
After training and evaluating the models, the results are displayed as follows:

Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	0.86	0.70	0.58	0.63
Decision Tree	0.85	0.65	0.64	0.64
Random Forest	0.88	0.72	0.60	0.66
SVM	0.87	0.68	0.59	0.63
Visualization

The project includes a correlation heatmap to visualize the relationship between the features and the target variable.




