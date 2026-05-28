import streamlit as st
import pymongo
import cv2
import numpy as np
import pandas as pd
from datetime import datetime
from deepface import DeepFace
import tempfile

# ================= MONGODB =================
myclient = pymongo.MongoClient("mongodb+srv://Ankita_9241:Ankita@cluster0.hngpsnl.mongodb.net/?appName=Cluster0")

mydb = myclient["face"]

user_col = mydb["user_info"]
attendance_col = mydb["attendance"]

# ================= LOGIN CHECK =================
if 'name' not in st.session_state:

    st.warning("Please Login First")

    st.switch_page("pages/login.py")

# ================= TITLE =================
st.title("📸 Face Recognition Attendance")

name = st.session_state["name"]

st.success(f"Welcome : {name}")

st.info("""
Capture your live photo.

The system checks whether the registered face
and live face are same or not.

If matched successfully,
attendance will be marked Present ✅
""")

# ================= CASCADE =================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# ================= GET USER =================
user = user_col.find_one({"name": name})

# ================= REGISTERED IMAGE =================
registered_img_path = user["photo"]

# ================= CAMERA =================
web_cam = st.camera_input("Take Attendance Photo")

# ================= MATCH FUNCTION =================
    x, y, w, h = live_faces[0]

    x2, y2, w2, h2 = reg_faces[0]

def compare_faces():

    file_bytes = np.asarray(
        bytearray(web_cam.read()),
        dtype=np.uint8
    )

    live_img = cv2.imdecode(file_bytes, 1)

    gray_live = cv2.cvtColor(
        live_img,
        cv2.COLOR_BGR2GRAY
    )

    live_faces = face_cascade.detectMultiScale(
        gray_live,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100,100)
    )

    reg_img = cv2.imread(registered_img_path)

    gray_reg = cv2.cvtColor(
        reg_img,
        cv2.COLOR_BGR2GRAY
    )

    reg_faces = face_cascade.detectMultiScale(
        gray_reg,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100,100)
    )

    if len(live_faces) > 0 and len(reg_faces) > 0:

        st.success("✅ Face Detected Successfully")

        # MARK ATTENDANCE
        now = datetime.now()

        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        already = attendance_col.find_one({
            "name": name,
            "date": date
        })

        if already:

            st.warning("Attendance Already Marked")

        else:

            attendance_col.insert_one({

                "name": name,
                "date": date,
                "time": time,
                "status": "Present"

            })

            st.success("✅ Attendance Marked Successfully")

    else:

        st.error("❌ No Face Detected")

# ================= BUTTON =================
if st.button("MARK ATTENDANCE"):

    if web_cam is not None:

        compare_faces()

    else:

        st.warning("Please Capture Image")

# ================= SHOW ATTENDANCE =================
st.markdown("---")

st.subheader("📋 Attendance Records")

data = list(
    attendance_col.find(
        {"name": name},
        {"_id": 0}
    )
)

if len(data) > 0:

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.warning("No Attendance Found")

