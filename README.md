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

## Project 3: Heart Disease Prediction System using Machine Learning

This project aims to develop an intelligent system that predicts the likelihood of a person having a heart disease based on various health-related features. The system utilizes machine learning algorithms to analyze historical health data and make predictions, contributing to early disease detection and proactive healthcare management.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Models and Evaluation](#models-and-evaluation)
- [Procedure](#Procedure)
- [Results](#results)
- [Cross-Validation and Hyperparameter Tuning](Cross-Validation-and-Hyperparameter-Tuning)
- [Validation and Testing](Validation-and-Testing)
- [Visualization](#visualization)

## Project Overview
The main objectives of this project are:
1. Data Collection: Gather a diverse dataset containing relevant health features.
2. Data Preprocessing: Perform data cleaning, handle missing values, and ensure data quality.
3. Feature Selection: Identify the most influential variables for disease prediction.
4. Model Development: Implement various machine learning algorithms for disease prediction.
5. Cross-Validation: Assess the generalization performance of the models.
6. Hyperparameter Tuning: Optimize the performance of selected machine learning models.
7. Validation and Testing: Ensure the accuracy, reliability, and robustness of the disease prediction system.

## Dataset
The dataset used in this project is the "Heart Disease Health Indicators Dataset" from Kaggle, which can be found [here](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset).

## Features
The dataset includes the following features:
- HighBP
- HighChol
- CholCheck
- BMI
- Smoker
- Stroke
- Diabetes
- PhysActivity
- Fruits
- Veggies
- HvyAlcoholConsump
- AnyHealthcare
- NoDocbcCost
- GenHlth
- MentHlth
- PhysHlth
- DiffWalk
- Sex
- Age

The target variable is:
- HeartDiseaseorAttack


## Models and Evaluation

The following machine learning models are implemented and evaluated in this project:

- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

The models are evaluated using the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score

## Procedure

- Data preprocessing and normalization
- Feature selection using Recursive Feature Elimination (RFE)
- Model training with various classifiers (Logistic Regression, Decision Tree, Random Forest, SVM)
- Model evaluation using accuracy, precision, recall, and F1 score
- Cross-validation and hyperparameter tuning for Random Forest
- Correlation heatmap for feature visualization

## Results
The selected features using RFE are printed in the console. The performance metrics for each model (Logistic Regression, Decision Tree, Random Forest, SVM) are displayed in a tabular format.

## Cross-Validation and Hyperparameter Tuning
GridSearchCV is used to perform cross-validation and hyperparameter tuning for the Random Forest model. The best parameters are printed in the console.

## Validation and Testing
The best model (Random Forest with tuned hyperparameters) is validated on the test set. The accuracy, precision, recall, and F1 score are printed in the console.

## Correlation Heatmap
A correlation heatmap of the features and the target variable is displayed to visualize the relationships between variables.
