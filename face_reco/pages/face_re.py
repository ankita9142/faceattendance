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
def compare_faces():

    # ================= SAVE LIVE IMAGE =================

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    temp_file.write(web_cam.getvalue())

    live_image_path = temp_file.name

    # ================= CHECK REGISTERED IMAGE =================

    if registered_img_path == "":

        st.error("No Registered Image Found")

        return

    try:

        # ================= FACE VERIFY =================

        result = DeepFace.verify(

            img1_path=registered_img_path,
            img2_path=live_image_path,

            enforce_detection=False

        )

        # ================= MATCHED =================

        if result["verified"]:

            st.success("✅ Face Matched Successfully")

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

                st.balloons()

        # ================= NOT MATCHED =================

        else:

            st.error("❌ Face Not Matched")

    except Exception as e:
        
        st.error(f"Error : {e}")
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
