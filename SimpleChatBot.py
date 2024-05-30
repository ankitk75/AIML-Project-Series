import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import time
from streamlit_chat import message as st_message

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Function to get the current time
def get_current_time():
    current_time = time.localtime()
    return f"{current_time.tm_hour} : {current_time.tm_min}"

# Function to get the current date
def get_current_date():
    current_date = time.localtime()
    return f"{current_date.tm_year} / {current_date.tm_mon} / {current_date.tm_mday}"

# Define a dictionary for questions and answers
qa_dict = {
    "what is your name?": "I am BrainyBot, an Anthropic chatbot.",
    "how are you feeling?": "I'm doing well, thanks for asking!",
    "what can you do?": "I can provide information, answer questions, tell jokes, and more! Feel free to ask.",
    "where are you from?": "I exist in the digital realm, but I'm here to help you wherever you are!",
    "what languages do you speak?": "I can converse with you in multiple languages, including English, Spanish, French, and more!",
    "can you tell me the weather?": "I don't have access to real-time weather information.",
    "what time is it?": f"The current time is {get_current_time()}.",
    "what is today's date?": f"Today's date is {get_current_date()}.",
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?"
}

# Function to preprocess the questions for matching
def preprocess_text(text):
    stop_words_set = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return ' '.join([stemmer.stem(word) for word in text.lower().split() if word not in stop_words_set])

# Preprocess the qa_dict keys for efficient matching
processed_qa_dict = {preprocess_text(key): value for key, value in qa_dict.items()}

# Function to handle user queries
def get_response(user_query):
    processed_query = preprocess_text(user_query)
    return processed_qa_dict.get(processed_query, "Sorry, I couldn't find an answer to your question.")

# Main function for the Streamlit app
def main():
    st.title("BrainyBot")
    st.write("Hello! I'm here to help with your questions.")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    user_input = st.chat_input("Ask me anything:")
    if user_input:
        response = get_response(user_input)
        st.session_state.conversation.append({"user": user_input, "bot": response})

    for chat in st.session_state.conversation:
        st_message(chat['user'], is_user=True, key=f"user_{chat['user']}")
        st_message(chat['bot'], is_user=False, key=f"bot_{chat['bot']}")

if __name__ == "__main__":
    main()
