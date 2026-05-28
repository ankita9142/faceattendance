import streamlit as st
import time


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
}

</style>
""", unsafe_allow_html=True)


st.title("🧑 Face Recognition System")


st.image("image/img1.jpeg")

st.header("📌 Introduction")

st.write("""
The Face Recognition System is an AI-based application developed using Python,
OpenCV, and Streamlit. This system can detect and recognize human faces from
images, videos, or live webcam feeds.

Face recognition technology is widely used in security systems, attendance
management, mobile authentication, and smart surveillance systems.
""")


# ---------------- OBJECTIVE ----------------
st.markdown("---")
st.header("🎯 Objective")

st.write("""
The main objective of this project is to build a smart and secure face
recognition system that can:

✔ Detect human faces accurately  
✔ Recognize authorized users  
✔ Improve security and monitoring  
✔ Reduce manual verification work  
✔ Provide real-time face authentication  
""")


# ---------------- FEATURES ----------------
st.markdown("---")
st.header("✨ Features")

st.write("""
🔹 Real-Time Face Detection  
🔹 AI-Based Face Recognition  
🔹 Webcam Support  
🔹 Upload Image Detection  
🔹 Fast and Accurate Results  
🔹 User Friendly Interface  
🔹 Secure Authentication System  
🔹 Smart Attendance & Monitoring  
""")


# ---------------- HOW IT WORKS ----------------
st.markdown("---")
st.header("⚙ How It Works")

st.write("""
### Step 1: Image Input
The system captures an image from webcam or uploaded file.

### Step 2: Face Detection
OpenCV detects the human face from the image.

### Step 3: Face Processing
The detected face is converted into facial features and patterns.

### Step 4: Recognition
The system compares the face with stored database images.

### Step 5: Result Display
If the face matches, the user is recognized successfully.
Otherwise, it shows an unknown user.
""")
