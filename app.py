import streamlit as st
from pymongo import MongoClient
client_uri=st.secrets['uri']
client = MongoClient(client_uri)
db=client['pwnai_output']