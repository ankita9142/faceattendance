import streamlit as st
import pymongo


# MongoDB Connection
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")

mydb = myclient["face"]
my = mydb["user_info"]


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
}

</style>
""", unsafe_allow_html=True)



c1, c2, c3, c4 = st.columns(4)

if 'name' not in st.session_state:

    st.warning("Please Login First")

    st.switch_page("pages/login.py")



# Session State
if 'name' not in st.session_state:
    st.session_state['name'] = ""


    
st.title("Welcome...")
name = st.session_state['name']

st.success(f"Welcome : {name}")




@st.dialog("User Profile")
def profile_popup():

    res = my.find({"name": name})

    for data in res:
        st.success(f"🧑 Name : {data['name']}")
        st.success(f"🔒 Password : {data['password']}")
        st.success(f"⚧ Gender : {data['gender']}")
        st.success(f"📧 Email : {data['email']}")
        st.success(f"📚 Department : {data['dept']}")
        img1=data['photo']
        st.image(img1)





@st.dialog("Change Password")
def password_popup():

    t1 = st.text_input("Old Password", type="password")
    t2 = st.text_input("New Password", type="password")

    if st.button("Update Password"):

        result = my.update_one({"name": name,"password": t1},{"$set": {"password": t2}})

        if result.modified_count > 0:
            st.success("Password Changed Successfully!")
        else:
            st.error("Old Password Incorrect!")



# Buttons
if c1.button("See Profile"):
    profile_popup()

if c2.button("Change Password"):
    password_popup()

if c3.button("Face recognition"):
    st.write("Opening Detecting System...")
    st.switch_page("pages/face_re.py")

if c4.button("📤 Logout"):

    st.session_state.clear()

    st.switch_page("main.py")

