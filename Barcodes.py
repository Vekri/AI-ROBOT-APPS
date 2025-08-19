import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# GitHub raw content base URL
barcode_folder = "https://raw.githubusercontent.com/Vekri/AI-ROBOT-APPS/main/"

# Map of filenames to (label, link)
barcode_info = {
    "EDA_APP.png": ("Deploy your EDA APP", "https://edaappsingareddy-y7axy22nl4rtagozreekiw.streamlit.app/"),
    "visualizationapp.png": ("Deploy your Visualization App", "https://visualizationapp-8y3wkb2met6wwjx5nrxomw.streamlit.app/"),
    "Search_Engine.png": ("Deploy your Search Engine", "https://search-engine-llm-kdm4wsfq5kghq6htq9tue7.streamlit.app/"),
    "Chat With SQLDB.png": ("Deploy your Chat With SQLDB", "https://chat-with-sql-db-diz4xugyhpvhbzhyrpxuxd.streamlit.app/"),
    "Classificationapp.png": ("Deploy your Classification App", "https://classification-model-wqcgqhwihsg76npktrrbn5.streamlit.app/"),
    "NLP SUPER APP.png": ("Deploy your NLP SUPER App", "https://nlpsuperapp-cyqpap2cad7os2h9krzvjf.streamlit.app/"),
    "Chart Insights with LLM.png": ("Deploy your Chart Insights App", "https://chart-insights-with-groq-vision-lkndvhyjgpajlynrseq9xb.streamlit.app/")
}

# Show AI robot image at the top
cols_intro = st.columns([2, 10])
with cols_intro[0]:
    st.image(
        "https://cdn.pixabay.com/photo/2023/05/24/17/49/ai-generated-8015425_1280.jpg",
        caption="AI Robot (Singareddy AI Labs)",
        width=90
    )

with cols_intro[1]:
    st.markdown("""
    <div style='min-height: 180px; display: flex; flex-direction: column; justify-content: flex-start; margin-left: 0; padding-left: 20px;'>
    <h2 style='margin-bottom: 0; margin-top: 0; word-break: break-word;'>SingaReddy – Marketing Analytics Consultant | Data Science | AI/LLM Apps | Python | Cloud</h2>
    <p style='margin-top: 0;'>
    Over 17 years of experience driving business growth through data science, predictive modeling, and AI applications. Skilled in Python (pandas, scikit-learn, Hugging Face), SQL, SAS, and cloud deployment. Builds end-to-end solutions using Streamlit, LangChain, and LLMs for marketing, personalization, and automation. Proven leader in developing and deploying scalable, real-time analytics systems.
    </p>
    <b>Contact:</b> <a href='mailto:btsinga999@gmail.com'>btsinga999@gmail.com</a><br>
    <b>LinkedIn:</b> <a href='https://www.linkedin.com/in/rajeswar-reddy-44152450' target='_blank'>https://www.linkedin.com/in/rajeswar-reddy-44152450</a><br>
    <b>AI Projects:</b> <a href='https://ai-robot-apps-a8d78utapcoszwhfqmkiyt.streamlit.app' target='_blank'>AI Robot Apps</a>
    </div>
    """, unsafe_allow_html=True)

# Layout for app previews
st.title("🚀 AI Apps Collections")

cols = st.columns(5)

for idx, (filename, (label, link)) in enumerate(barcode_info.items()):
    image_url = f"{barcode_folder}{filename}"
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))

        with cols[idx % 5]:
            st.image(image, caption=label, use_container_width=True)
            st.markdown(f"[🔗 Deploy Link]({link})", unsafe_allow_html=True)
            st.download_button(
                label="📥 Download",
                data=response.content,
                file_name=filename,
                mime="image/png"
            )
    except Exception as e:
        st.warning(f"⚠️ Could not load image: {filename}")



