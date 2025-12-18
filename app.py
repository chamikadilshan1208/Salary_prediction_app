import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #243047, #152b52);
}

/* Title text */
h1, h2, h3 {
    color: #ffffff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Buttons */
.stButton>button {
    background-color: #778eed;
    color: black;
    border-radius: 12px;
    font-size: 16px;
    padding: 10px 24px;
}

/* Selectbox */
.stSelectbox, .stSlider {
    background-color: #02274f;
    border-radius: 10px;
}

/* Metric cards */
.metric-container {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

st.sidebar.markdown("## 🧭 Navigation")
page = st.sidebar.radio(
    "",
    ("💸 Predict Salary", "📊 Explore Data")
)

