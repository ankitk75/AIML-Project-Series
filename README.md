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
- [Contributing](#contributing)

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
