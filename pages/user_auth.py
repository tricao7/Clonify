import streamlit as st
import pymongo
from pymongo.server_api import ServerApi

# Connect to the DB.
@st.cache_resource
def connect_db():
    client = pymongo.MongoClient(
      st.secrets["mongo"]["connection_url"], 
      server_api=ServerApi('1'))
    db = client.get_database('main')
    return db.users

user_db = connect_db()

# Initialize Session States.
if 'username' not in st.session_state:
       st.session_state.username = ''
if 'form' not in st.session_state:
       st.session_state.form = ''

# Sign up form.
def signup():
    st.title('Sign up')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Sign up'):
        if user_db.find_one({'username': username}):
            st.error('User already exists')
        else:
            user_db.insert_one({'username': username, 'password': password})
            st.success('User created')
            st.session_state.username = username
            st.session_state.form = 'app'


if __name__ == "__main__":
    signup()
