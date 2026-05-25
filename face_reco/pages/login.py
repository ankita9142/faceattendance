import streamlit as st
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://Ankita_9241:<db_password>@cluster0.hngpsnl.mongodb.net/?appName=Cluster0")
mydb = myclient["face"]
my=mydb["user_info"]





st.header("Login into 🧑 Face Recognition System")
email=st.text_input("Email")
password=st.text_input("Password", type="password")

if st.button("SignIn"):
    str=my.find({"email":email,"password":password})
    d=0
    for data in str:
        st.success(f"Welcome:{data['name']}")
        d=d+1
        st.session_state["name"]=data['name']
        st.switch_page("pages/profile.py")
        
    if d==0:
        st.error("Invalid Login !!!")
