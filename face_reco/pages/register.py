import streamlit as st
import random
import pymongo
import os
import uuid


myclient = pymongo.MongoClient("mongodb+srv://Ankita_9241:<db_password>@cluster0.hngpsnl.mongodb.net/?appName=Cluster0")
mydb = myclient["face"]
my=mydb["user_info"]




st.header("Register")
name=st.text_input("UserName")
email=st.text_input("Email")
password=st.text_input("Password", type="password")
con_password=st.text_input("Confirm Password", type="password")

g=st.radio("Gender",['M','F'])
dept=st.selectbox("🏢 Department",["Select", "BCA", "MCA", "B.Tech", "MBA"])

# Create images folder
if not os.path.exists("images"):
    os.makedirs("images")

# Default Image Path
str1 = ""

# Camera
web_cam = st.camera_input("Take a picture")

if web_cam is not None and name != "":

    str1 = f"images/{name}.png"
   
    # Save Image
    with open(str1, "wb") as f:
        f.write(web_cam.getvalue())

    st.success("Image Saved Successfully")

    st.image(web_cam)

b1=st.button("SAVE")
def get_data():
       my.insert_one({"name":name,"email":email,"password":password, "gender":g,"dept":dept,"photo":str1})
       st.success("Your data are saved!!")
       
if b1:
       
        
       if password != con_password:
              st.error("Passwords do not match")
       elif my.find_one({"name": name}):
              st.error("Username already exists")
       else:
              my.insert_one({"name":name,"email":email,"password":password, "gender":g,"dept":dept,"photo":str1})
              st.success("Your data are saved!!")
              str=my.find({"name":name})
              for data in str:
                     st.session_state["name"]=data['name']
                     st.switch_page("pages/profile.py")



