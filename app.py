import streamlit as st
import auth as stauth
import yaml
from yaml.loader import SafeLoader
from home import *

st.set_page_config(
    page_title='Martorelli - Calculadora',  # Change to your desired title
    page_icon="favicon.png",  # Change to your desired icon
    layout="wide",  # You can customize the layout here
    initial_sidebar_state="expanded")

logo_path = "logo.png"  # Replace with the actual file path
st.sidebar.image(logo_path, width=250) 
st.sidebar.write("")
st.sidebar.write("")

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#render_home()

name, authentication_status, username = authenticator.login('Login')

if st.session_state["authentication_status"]:
    render_home()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')