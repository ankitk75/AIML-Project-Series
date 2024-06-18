# Disease Prediction System using Machine Learning

This project aims to develop an intelligent system that predicts the likelihood of a person having a particular disease based on various health-related features. The system utilizes machine learning algorithms to analyze historical health data and make predictions, contributing to early disease detection and proactive healthcare management.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Models and Evaluation](#models-and-evaluation)
- [Results](#results)
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

## Installation
To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using the following command:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Features

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

