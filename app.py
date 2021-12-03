import streamlit as st
import pandas as pd
import pyodbc
import config


server = config.DB_HOST
database = config.DB_NAME 
username = config.DB_USER 
password = config.DB_PASS

# Query parameters 
security_role = "REPORT_CLIENT_RUN"
user_name = "NGUYEN-VU"

# Queries
query_one_param = "SELECT * FROM Report WHERE SecurityRole = ?"
query_two_params = "SELECT * FROM Report WHERE SecurityRole = ? AND CreatedByUserName = ?"

# Open connection to the database
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Query with one parameter marker
#df = pd.read_sql(query_one_param, cnxn, params=(security_role,)) # the comma in the tuple is very important when you only have one parameter!!!!

# Query with more than one parameter markers
df = pd.read_sql(query_two_params, cnxn, params=(security_role,user_name))


st.dataframe(df)





