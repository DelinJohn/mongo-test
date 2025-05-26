import streamlit as st
from pymongo import MongoClient
client_uri=st.secrets['uri']
print(client_uri)
client = MongoClient(client_uri)
db=client['Pwani_llm_Output']
st.write(db.list_collection_names())