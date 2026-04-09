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
body {
    background-color: #F5F7FA;
}

[data-testid="stSidebar"] {
    background-color: #0B3C5D;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.result-box {
    background: linear-gradient(135deg, #0B3C5D, #1E81B0);
    color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}

h1, h2, h3 {
    color: #0B3C5D;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
col1, col2 = st.columns([1,6])

with col1:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=80)

with col2:
    st.markdown("## Port Capacity Dashboard")
    st.caption("Simulasi kapasitas terminal petikemas")

# =========================
# SIDEBAR
# =========================
if os.path.exists("logo.jpg"):
    st.sidebar.image("logo.jpg", width=120)

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Berth", "Yard", "Quay Crane", "Gate"]
)

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.subheader("📊 Overview")

    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="card">Berth<br><b>501,720</b></div>', unsafe_allow_html=True)
    c2.markdown('<div class="card">Yard<br><b>15,943</b></div>', unsafe_allow_html=True)
    c3.markdown('<div class="card">QC<br><b>9,549,372</b></div>', unsafe_allow_html=True)

# =========================
# BERTH
# =========================
elif menu == "Berth":
    st.subheader("🔵 Berth Capacity")

    col1, col2, col3 = st.columns(3)

    with col1:
        length = st.number_input("Length Berth", 0)
        num_berth = st.number_input("Number Berth", 0)
        loa = st.number_input("Avg LOA", 0)

    with col2:
        dl = st.number_input("Avg D/L", 0)
        bch = st.number_input("BCH", 0)
        crane_ratio = st.number_input("Crane Ratio", 0.0)

    with col3:
        bor = st.number_input("BOR", 0.65)
        teus = st.number_input("TEUs Ratio", 1.13)
        safety = st.number_input("Safety Distance", 0.1)

    # HITUNGAN
    bsh = bch * crane_ratio
    bt = (dl / bsh) if bsh > 0 else 0
    hours = 8760
    ship_call = (hours / bt) if bt > 0 else 0
    berth_capacity = ship_call * dl * teus

    st.markdown("### 📊 Hasil")

    r1, r2, r3 = st.columns(3)
    r1.metric("BSH", f"{bsh:.2f}")
    r2.metric("BT", f"{bt:.2f}")
    r3.metric("Ship Call", f"{ship_call:.0f}")

    st.markdown(f"""
    <div class="result-box">
        {berth_capacity:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# YARD
# =========================
elif menu == "Yard":
    st.subheader("🟢 Yard Capacity")

    col1, col2, col3 = st.columns(3)

    with col1:
        row = st.number_input("Row", 0)
        slot = st.number_input("Slot", 0)

    with col2:
        tier = st.number_input("Tier", 0)
        dwell = st.number_input("Dwelling Time", 0)

    with col3:
        yor = st.number_input("YOR (%)", 0)
        days = 365

    yard_capacity = row * slot * tier * (days / (dwell if dwell > 0 else 1))

    st.markdown(f"""
    <div class="result-box">
        {yard_capacity:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# QUAY CRANE
# =========================
elif menu == "Quay Crane":
    st.subheader("🟣 Quay Crane Capacity")

    col1, col2, col3 = st.columns(3)

    with col1:
        total_qcc = st.number_input("Total QCC", 0)
        bch_qcc = st.number_input("BCH QCC", 0)

    with col2:
        hours = 24
        days = 365

    with col3:
        util = st.number_input("Utilization (%)", 0)

    qc_capacity = total_qcc * bch_qcc * hours * days * (util/100)

    st.markdown(f"""
    <div class="result-box">
        {qc_capacity:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# =========================
# GATE
# =========================
elif menu == "Gate":
    st.subheader("🟠 Gate Capacity")

    col1, col2, col3 = st.columns(3)

    with col1:
        lane = st.number_input("Total Lane", 0)

    with col2:
        service = st.number_input("Service Time (detik)", 0)

    with col3:
        hours = 86400

    gate_capacity = (lane * hours / service) if service > 0 else 0

    st.markdown(f"""
    <div class="result-box">
        {gate_capacity:,.0f} TEU / Hari
    </div>
    """, unsafe_allow_html=True)
