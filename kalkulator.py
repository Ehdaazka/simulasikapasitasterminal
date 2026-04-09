import streamlit as st
import os

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Port Capacity", layout="wide")

# =========================
# CSS (CUSTOM PALETTE)
# =========================
st.markdown("""
<style>

/* Background */
body {
    background-color: #192338;
    color: #D9E1F1;
}

/* Container */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 0rem;
}

/* Card */
.card {
    background: #1E2E4F;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}

/* Result box */
.result-box {
    background: linear-gradient(135deg, #31487A, #8FB3E2);
    color: #192338;
    padding: 22px;
    border-radius: 14px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

/* Title */
h1, h2, h3 {
    color: #8FB3E2;
}

/* Metric */
[data-testid="stMetricValue"] {
    font-size: 1.5rem;
}

/* Input */
input, .stNumberInput input {
    background-color: #192338 !important;
    color: #D9E1F1 !important;
    border-radius: 8px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    color: #D9E1F1;
    font-weight: 500;
}
.stTabs [aria-selected="true"] {
    color: #8FB3E2;
    border-bottom: 2px solid #8FB3E2;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (TITLE + LOGO KANAN)
# =========================
col1, col2 = st.columns([6,1])

with col1:
    st.markdown("## 🚢 Port Operational Capacity")
    st.caption("Terminal Capacity Simulation Dashboard")

with col2:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=80)

# =========================
# TABS (ATAS)
# =========================
tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# =========================
# BERTH
# =========================
with tabs[0]:

    main, result = st.columns([3,1])

    with main:
        st.markdown("### 🔵 Input Parameter")

        c1, c2, c3, c4 = st.columns(4)
        length_berth = c1.number_input("Length Berth", 0)
        avg_loa = c2.number_input("Avg LOA", 0)
        bch = c3.number_input("BCH", 0)
        crane_ratio = c4.number_input("Crane Ratio", 0.0)

        c5, c6, c7, c8 = st.columns(4)
        avg_dl = c5.number_input("Avg D/L", 0)
        teus_ratio = c6.number_input("TEUs Ratio", 1.13)
        safety_dist = c7.number_input("Safety Dist", 1.1, disabled=True)
        bor = c8.number_input("BOR", 0.65, disabled=True)

        # CALCULATION
        num_berth = length_berth / (avg_loa * safety_dist) if avg_loa > 0 else 0
        bsh = bch * crane_ratio
        bt = avg_dl / bsh if bsh > 0 else 0
        hours = 8760
        ship_call = (hours / bt) * bor if bt > 0 else 0
        berth_cap = ship_call * avg_dl * teus_ratio

        st.markdown("### 📊 Metrics")

        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Berth", f"{num_berth:.2f}")
        r2.metric("BSH", f"{bsh:.2f}")
        r3.metric("BT/Call", f"{bt:.2f}")
        r4.metric("Ship Call", f"{ship_call:.0f}")

    with result:
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
            {berth_cap:,.0f}<br>
            TEU / Tahun
        </div>
        """, unsafe_allow_html=True)

# =========================
# YARD
# =========================
with tabs[1]:

    left, right = st.columns([3,1])

    with left:
        st.markdown("### 🟢 Yard Input")

        y1, y2, y3 = st.columns(3)
        row = y1.number_input("Row", 0)
        slot = y2.number_input("Slot", 0)
        tier = y3.number_input("Tier", 0)

        y4, y5, y6 = st.columns(3)
        eff_cap = y4.number_input("Effective Cap", 0)
        dwell = y5.number_input("Dwelling Time", 0)
        yor = y6.number_input("YOR (%)", 70)

        yard_cap = (slot * row * tier * 365 / (dwell if dwell > 0 else 1)) * (yor/100)

    with right:
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
            {yard_cap:,.0f}<br>
            TEU / Tahun
        </div>
        """, unsafe_allow_html=True)

# =========================
# QC
# =========================
with tabs[2]:
    st.info("Quay Crane - siap isi rumus")

# =========================
# YC
# =========================
with tabs[3]:
    st.info("Yard Crane - siap isi rumus")

# =========================
# GATE
# =========================
with tabs[4]:
    st.info("Gate - siap isi rumus")
