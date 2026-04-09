import streamlit as st
import os

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Port Capacity Dashboard", layout="wide")

# =========================
# CSS (PELINDO STYLE)
# =========================
st.markdown("""
<style>

/* Background */
body {
    background-color: #F5F7FA;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0B3C5D;
}

/* Sidebar text putih */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}

/* Result box */
.result-box {
    background: linear-gradient(135deg, #0B3C5D, #1E81B0);
    color: white;
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

/* Title */
h1, h2, h3 {
    color: #0B3C5D;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (LOGO + TITLE)
# =========================
col1, col2 = st.columns([1, 6])

with col1:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=90)

with col2:
    st.markdown("## Port Capacity Dashboard")
    st.caption("Simulasi kapasitas terminal petikemas")

# =========================
# SIDEBAR
# =========================
if os.path.exists("logo.jpg"):
    st.sidebar.image("logo.jpg", width=120)

st.sidebar.title("Menu Navigasi")

menu = st.sidebar.radio(
    "",
    ["Dashboard", "Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"]
)

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.subheader("📊 Overview Capacity")

    c1, c2, c3 = st.columns(3)

    c1.markdown('<div class="card">Berth Capacity<br><b>501,720</b></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card">Yard Capacity<br><b>15,943</b></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card">QC Capacity<br><b>9,549,372</b></div>', unsafe_allow_html=True)

# =========================
# BERTH
# =========================
elif menu == "Berth":
    st.subheader("🔵 Berth Capacity")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        length = st.number_input("Length of Berth", 0)
        loa = st.number_input("Avg LOA", 0)
        dl = st.number_input("Avg D/L per Call", 0)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        bch = st.number_input("BCH", 0)
        crane_ratio = st.number_input("Crane Ratio", 0.0)
        teus = st.number_input("TEUs Ratio", 1.13)
        st.markdown('</div>', unsafe_allow_html=True)

    # HITUNGAN (sementara)
    bsh = bch * crane_ratio
    bt = (dl / bsh) if bsh > 0 else 0

    st.write("BSH =", bsh)
    st.write("BT per Call =", bt)

    st.markdown(f"""
    <div class="result-box">
        Berth Capacity<br>
        {501720:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# YARD
# =========================
elif menu == "Yard":
    st.subheader("🟢 Yard Capacity")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    row = st.number_input("Row", 0)
    slot = st.number_input("Slot", 0)
    tier = st.number_input("Tier", 0)
    dwell = st.number_input("Dwelling Time", 0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-box">
        Yard Capacity<br>
        {15943:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# QUAY CRANE
# =========================
elif menu == "Quay Crane":
    st.subheader("🟣 Quay Crane Capacity")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    total_qcc = st.number_input("Total QCC", 0)
    bch_qcc = st.number_input("BCH QCC", 0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-box">
        QC Capacity<br>
        {9549372:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# YARD CRANE
# =========================
elif menu == "Yard Crane":
    st.subheader("🟤 Yard Crane Capacity")
    st.info("Silakan tambahkan rumus nanti")

# =========================
# GATE
# =========================
elif menu == "Gate":
    st.subheader("🟠 Gate Capacity")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    lane = st.number_input("Total Lane", 0)
    service = st.number_input("Service Time", 0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="result-box">
        Gate Capacity<br>
        465,133 TEU / Hari
    </div>
    """, unsafe_allow_html=True)
