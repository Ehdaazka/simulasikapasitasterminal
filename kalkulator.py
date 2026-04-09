import streamlit as st
import os

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Port Capacity", layout="wide")

# =========================
# CSS (PELINDO STYLE)
# =========================
st.markdown("""
<style>

/* Background */
body {
    background-color: #F4F6F9;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0B3C5D;
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Card style */
.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

/* Result box */
.result-box {
    background: linear-gradient(135deg, #0B3C5D, #1E81B0);
    color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

/* Compact spacing */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 0rem;
}

/* Metric size */
[data-testid="stMetricValue"] {
    font-size: 1.4rem;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (LOGO + TITLE)
# =========================
col1, col2 = st.columns([1,6])

with col1:
    if os.path.exists("logo.jpg"):
        st.image("logo.jpg", width=80)

with col2:
    st.markdown("## 🚢 Port Operational Capacity")
    st.caption("Simulasi Kapasitas Terminal Petikemas")

# =========================
# SIDEBAR
# =========================
if os.path.exists("logo.jpg"):
    st.sidebar.image("logo.jpg", width=120)

st.sidebar.title("Navigation")
tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# =========================
# BERTH
# =========================
with tabs[0]:
    main_col, side_col = st.columns([3,1])

    with main_col:
        st.markdown("### 🔵 Input & Calculation")

        # GRID INPUT (PADAT)
        c1, c2, c3, c4 = st.columns(4)
        length_berth = c1.number_input("Length Berth", value=0)
        avg_loa = c2.number_input("Avg LOA", value=0)
        bch = c3.number_input("BCH", value=0)
        crane_ratio = c4.number_input("Crane Ratio", value=0.0)

        c5, c6, c7, c8 = st.columns(4)
        avg_dl = c5.number_input("Avg D/L", value=0)
        teus_ratio = c6.number_input("TEUs Ratio", value=1.13)
        safety_dist = c7.number_input("Safety Dist", value=1.1, disabled=True)
        bor = c8.number_input("BOR", value=0.65, disabled=True)

        st.divider()

        # ================= CALCULATION =================
        num_berth = length_berth / (avg_loa * safety_dist) if avg_loa > 0 else 0
        bsh = bch * crane_ratio
        bt_per_call = avg_dl / bsh if bsh > 0 else 0
        total_hours = 8760
        ship_call_year = (total_hours / bt_per_call) * bor if bt_per_call > 0 else 0
        berth_cap = ship_call_year * avg_dl * teus_ratio

        # METRICS
        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Berth", f"{num_berth:.2f}")
        r2.metric("BSH", f"{bsh:.2f}")
        r3.metric("BT/Call", f"{bt_per_call:.2f}")
        r4.metric("Ship Call", f"{ship_call_year:.0f}")

    with side_col:
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
            Berth Capacity<br>
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
        row = y1.number_input("Row", value=0)
        slot = y2.number_input("Slot", value=0)
        tier = y3.number_input("Tier", value=0)

        y4, y5, y6 = st.columns(3)
        eff_cap = y4.number_input("Effective Cap", value=0)
        dwelling = y5.number_input("Dwelling Time", value=0)
        yor_max = y6.number_input("YOR (%)", value=70)

        yard_cap = (slot * row * tier * 365 / (dwelling if dwelling > 0 else 1)) * (yor_max/100)

    with right:
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-box">
            Yard Capacity<br>
            {yard_cap:,.0f}<br>
            TEU / Tahun
        </div>
        """, unsafe_allow_html=True)

# =========================
# QC
# =========================
with tabs[2]:
    st.subheader("🟣 Quay Crane")
    st.info("Siap kamu isi rumusnya")

# =========================
# YC
# =========================
with tabs[3]:
    st.subheader("🟤 Yard Crane")
    st.info("Siap kamu isi rumusnya")

# =========================
# GATE
# =========================
with tabs[4]:
    st.subheader("🟠 Gate")
    st.success("Logic siap ditambahkan")
