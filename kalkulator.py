import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Port Capacity Dashboard", layout="wide")

# =========================
# CSS (BIAR KEREN)
# =========================
st.markdown("""
<style>
body {
    background-color: #0E1117;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Card */
.card {
    background: #1F2937;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* Result */
.result-box {
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: white;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

/* Title */
h1, h2, h3 {
    color: #F9FAFB;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR MENU
# =========================
st.sidebar.title("🚢 Port Dashboard")
menu = st.sidebar.radio(
    "Pilih Menu",
    ["Dashboard", "Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"]
)

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.title("📊 Overview Capacity")

    col1, col2, col3 = st.columns(3)

    col1.markdown('<div class="card">Berth<br><b>501,720</b></div>', unsafe_allow_html=True)
    col2.markdown('<div class="card">Yard<br><b>15,943</b></div>', unsafe_allow_html=True)
    col3.markdown('<div class="card">QC<br><b>9,549,372</b></div>', unsafe_allow_html=True)

# =========================
# BERTH
# =========================
elif menu == "Berth":
    st.title("🔵 Berth Capacity")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        length = st.number_input("Length of Berth", 0)
        loa = st.number_input("Avg LOA", 0)
        dl = st.number_input("Avg D/L", 0)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        bch = st.number_input("BCH", 0)
        crane_ratio = st.number_input("Crane Ratio", 0.0)
        teus = st.number_input("TEUs Ratio", 1.13)
        st.markdown('</div>', unsafe_allow_html=True)

    # HITUNGAN
    bsh = bch * crane_ratio
    bt = (dl / bsh) if bsh > 0 else 0

    st.write("BSH =", bsh)
    st.write("BT =", bt)

    # OUTPUT
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
    st.title("🟢 Yard Capacity")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    row = st.number_input("Row", 0)
    slot = st.number_input("Slot", 0)
    tier = st.number_input("Tier", 0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-box">
        Yard Capacity<br>
        {15943:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# QC
# =========================
elif menu == "Quay Crane":
    st.title("🟣 Quay Crane Capacity")

    total_qcc = st.number_input("Total QCC", 0)
    bch_qcc = st.number_input("BCH QCC", 0)

    st.markdown(f"""
    <div class="result-box">
        QC Capacity<br>
        {9549372:,.0f}
    </div>
    """, unsafe_allow_html=True)

# =========================
# YARD CRANE
# =========================
elif menu == "Yard Crane":
    st.title("🟤 Yard Crane")
    st.info("Masih bisa kamu isi nanti")

# =========================
# GATE
# =========================
elif menu == "Gate":
    st.title("🟠 Gate Capacity")

    lane = st.number_input("Lane", 0)
    service = st.number_input("Service Time", 0)

    st.markdown("""
    <div class="result-box">
        Gate Capacity<br>
        465,133 TEU
    </div>
    """, unsafe_allow_html=True)
