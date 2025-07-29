import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# GitHub raw content base URL
barcode_folder = "https://raw.githubusercontent.com/Vekri/AI-ROBOT-APPS/main/"

# Map of filenames to (label, link)
barcode_info = {
    "EDA_APP.png": ("EDA APP", "https://edaappsingareddy-y7axy22nl4rtagozreekiw.streamlit.app/"),
    "visualizationapp.png": ("Visualization App", "https://visualizationapp-8y3wkb2met6wwjx5nrxomw.streamlit.app/"),
    "Search_Engine.png": ("Search Engine", "https://search-engine-llm-kdm4wsfq5kghq6htq9tue7.streamlit.app/"),
    "Classificationapp.png": ("Classification App", "https://classification-model-wqcgqhwihsg76npktrrbn5.streamlit.app/")
}

# Show AI robot image at the top
st.image(
    "https://cdn.pixabay.com/photo/2023/05/24/17/49/ai-generated-8015425_1280.jpg",
    caption="AI Robot (Singareddy AI Labs)",
    width=180
)

st.title("AI Apps Collections")

cols = st.columns(4)

for idx, (filename, (label, link)) in enumerate(barcode_info.items()):
    image_url = barcode_folder + filename
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        with cols[idx % 4]:  # 4 columns
            st.image(image, caption=label, use_container_width=True)
            st.markdown(f"[🔗 Open Link]({link})", unsafe_allow_html=True)
            st.download_button(
                label="📥 Download",
                data=response.content,
                file_name=filename,
                mime="image/png"
            )
    except Exception as e:
        st.error(f"Failed to load {filename}: {e}")
