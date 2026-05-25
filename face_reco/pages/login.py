import streamlit as st
import pymongo
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb = myclient["face"]
my=mydb["user_info"]


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
}

</style>
""", unsafe_allow_html=True)



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
