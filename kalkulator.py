import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="Port Capacity", layout="wide")
st.markdown("""
<style>

/* ===== BACKGROUND ===== */
.stApp {
    background-color: #D9E1F1;
}

/* ===== CONTAINER ===== */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 0rem;
}

/* ===== CARD ===== */
.card {
    background: linear-gradient(135deg, #1E2E4F, #31487A);
    padding: 1.2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
    color: white;
}

/* ===== TITLE ===== */
.card-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    color: #8FB3E2;
}

/* ===== METRIC VALUE ===== */
[data-testid="stMetricValue"] {
    font-size: 1.6rem;
    font-weight: bold;
    color: #ffffff;
}

/* ===== METRIC LABEL ===== */
[data-testid="stMetricLabel"] {
    color: #D9E1F1;
}

/* ===== INPUT LABEL ===== */
label {
    color: #D9E1F1 !important;
}

/* ===== INPUT BOX ===== */
input {
    background-color: #192338 !important;
    color: white !important;
    border-radius: 6px !important;
    border: 1px solid #31487A !important;
}

/* ===== TAB ===== */
button[data-baseweb="tab"] {
    color: #1E2E4F;
    font-weight: 600;
}

/* ACTIVE TAB */
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #31487A !important;
    color: white !important;
    border-radius: 8px;
}

/* ===== WARNING BOX ===== */
.stAlert {
    background-color: #8FB3E2 !important;
    color: #192338 !important;
    border-radius: 8px;
}

/* ===== SMALL GAP ===== */
.small-gap {
    margin-top: 0.5rem;
}

</style>
""", unsafe_allow_html=True)
