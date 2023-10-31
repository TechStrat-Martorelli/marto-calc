import streamlit as st
import auth as stauth
import yaml
from yaml.loader import SafeLoader
from home import *

st.set_page_config(layout='wide')

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login')

if st.session_state["authentication_status"]:
    render_home()

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')