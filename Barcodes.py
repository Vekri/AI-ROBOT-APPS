import streamlit as st
from PIL import Image
import os

# Define image folder
barcode_folder = r"https://github.com/Vekri/AI-ROBOT-APPS"

# Map of filenames to (label, link)
barcode_info = {
    "https://github.com/Vekri/AI-ROBOT-APPS/EDA_APP.png": ("EDA APP", "https://edaappsingareddy-y7axy22nl4rtagozreekiw.streamlit.app/"),
    "visualizationapp.png": ("visualizationapp", "https://github.com/Vekri/AI-ROBOT-APPS/blob/main/visualizationapp.png"),
    "Search_Engine.png": ("Search_Engine", "https://github.com/Vekri/AI-ROBOT-APPS/blob/main/Search_Engine.png"),
    "Classificationapp.png": ("Classificationapp", "https://github.com/Vekri/AI-ROBOT-APPS/blob/main/Classificationapp.png")
        }

# Show AI robot image at the top with smaller size
st.image(
    "https://cdn.pixabay.com/photo/2023/05/24/17/49/ai-generated-8015425_1280.jpg",
    caption="AI Robot (Singareddy AI Labs)",
    width=180
)

# Layout
st.title("AI Apps Collections")

cols = st.columns(4)

for idx, (filename, (label, link)) in enumerate(barcode_info.items()):
    image_path = os.path.join(barcode_folder, filename)
    if not os.path.exists(image_path):
        continue  # skip if file not found
    image = Image.open(image_path)
    with cols[idx % 3]:
        st.image(image, caption=label, use_container_width=True)
        st.markdown(f"[🔗 Open Link]({link})", unsafe_allow_html=True)
        with open(image_path, "rb") as img_file:
            st.download_button(
                label="📥 Download",
                data=img_file,
                file_name=filename,
                mime="image/png"
            )
