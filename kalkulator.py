import streamlit as st

# =========================

# CONFIG

# =========================

st.set_page_config(page_title="Port Capacity Dashboard", layout="wide")

# =========================

# CUSTOM CSS (UI UPGRADE)

# =========================

st.markdown("""

<style>
.main { background-color: #121212; }

/* Card container */
.card {
    background: #1E1E1E;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    margin-bottom: 15px;
}

/* Highlight result */
.result-box {
    background: linear-gradient(135deg, #4A90E2, #6FC3FF);
    color: white;
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    font-size: 22px;
    font-weight: 600;
    margin-top: 10px;
}

/* Label */
.label-muted {
    color: #A0A0A0;
    font-size: 13px;
}
</style>

""", unsafe_allow_html=True)

# =========================

# HEADER

# =========================

st.markdown("## 🚢 Port Capacity Dashboard")
st.caption("Operational analysis for terminal capacity")

# Sidebar

st.sidebar.title("⚙️ Settings")
st.sidebar.write("Port Capacity Calculator")

# =========================

# TABS

# =========================

tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# =========================

# TAB 1: BERTH

# =========================

with tabs[0]:
st.subheader("🔵 Berth Capacity")

```
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    length_berth = st.number_input("Length of Berth (m)", 0)
    num_berth = st.number_input("Number of Berth", 0)
    crane_ratio = st.number_input("Crane Ratio", 0.0, step=0.1)

with col2:
    avg_loa = st.number_input("Avg LOA (m)", 0)
    avg_dl = st.number_input("Avg D/L per call", 0)
    bor = st.number_input("BOR", 0.0, step=0.01)

with col3:
    safety_dist = st.number_input("Safety distance", 0.0, step=0.1)
    bch = st.number_input("BCH", 0)
    teus_ratio = st.number_input("Teu's Ratio", 0.0, step=0.01)

st.markdown('</div>', unsafe_allow_html=True)

# ===== CALCULATION =====
bsh = bch * crane_ratio
bt_per_call = (avg_dl / bsh) if bsh > 0 else 0
total_hours = 8760
ship_call_year = 740

# ===== METRICS =====
res1, res2, res3, res4 = st.columns(4)

res1.markdown(f'<div class="card">BSH<br><b>{bsh:.2f}</b></div>', unsafe_allow_html=True)
res2.markdown(f'<div class="card">BT/Call<br><b>{bt_per_call:.2f}</b></div>', unsafe_allow_html=True)
res3.markdown(f'<div class="card">Total Hours<br><b>{total_hours}</b></div>', unsafe_allow_html=True)
res4.markdown(f'<div class="card">Ship Call<br><b>{ship_call_year}</b></div>', unsafe_allow_html=True)

# ===== RESULT =====
berth_cap = 501720  # TODO: masukin rumus asli
st.markdown(f"""
<div class="result-box">
    Berth Capacity<br>
    {berth_cap:,.0f} TEU / Tahun
</div>
""", unsafe_allow_html=True)
```

# =========================

# TAB 2: YARD

# =========================

with tabs[1]:
st.subheader("🟢 Yard Capacity")

```
st.markdown('<div class="card">', unsafe_allow_html=True)

y1, y2, y3 = st.columns(3)

with y1:
    row = st.number_input("Row", 0)
    eff_cap = st.number_input("Effective Capacity", 0)
    total_days_y = st.number_input("Total Days", 365, disabled=True)

with y2:
    slot = st.number_input("Slot", 0)
    dwelling_time = st.number_input("Dwelling Time (hari)", 0)

with y3:
    tier = st.number_input("Tier", 0)
    yor_max = st.number_input("YOR Max (%)", 0, max_value=100)

st.markdown('</div>', unsafe_allow_html=True)

yard_cap = 15943  # TODO
st.markdown(f"""
<div class="result-box">
    Yard Capacity<br>
    {yard_cap:,.0f} TEU / Tahun
</div>
""", unsafe_allow_html=True)
```

# =========================

# TAB 3: QUAY CRANE

# =========================

with tabs[2]:
st.subheader("🟣 Quay Crane Capacity")

```
st.markdown('<div class="card">', unsafe_allow_html=True)

q1, q2, q3 = st.columns(3)

with q1:
    total_qcc = st.number_input("Total QCC", 0)
    bch_hmc = st.number_input("BCH HMC", 0)
    total_hours_qc = st.number_input("Total Hours", 24, disabled=True)

with q2:
    bch_qcc = st.number_input("BCH QCC", 0)
    total_fc = st.number_input("Total FC/JC/MC", 0)
    total_days_qc = st.number_input("Total Days", 365, disabled=True)

with q3:
    total_hmc = st.number_input("Total HMC", 0)
    bch_fc = st.number_input("BCH FC/JC/MC", 0)
    util_max = st.number_input("Utilization Max (%)", 0, max_value=100)

st.markdown('</div>', unsafe_allow_html=True)

qc_cap = 9549372  # TODO
st.markdown(f"""
<div class="result-box">
    QC Capacity<br>
    {qc_cap:,.0f} TEU / Tahun
</div>
""", unsafe_allow_html=True)
```

# =========================

# TAB 4: GATE

# =========================

with tabs[4]:
st.subheader("🟠 Gate Capacity")

```
st.markdown('<div class="card">', unsafe_allow_html=True)

g1, g2, g3 = st.columns(3)

with g1:
    lane_gi = st.number_input("Total Lane GI", 0)
    service_go = st.number_input("Service GO", 0)
    teus_gate = st.number_input("Teu's Ratio", 0.0, step=0.01)

with g2:
    service_gi = st.number_input("Service Time GI", 0)
    time_24h = st.number_input("Time 24H (sec)", 86400, disabled=True)

with g3:
    lane_go = st.number_input("Total Lane GO", 0)
    total_days_g = st.number_input("Total Days", 365, disabled=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="result-box">
    Gate In Capacity<br>
    465,133 TEU / Hari
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="result-box">
    Gate Out Capacity<br>
    465,133 TEU / Hari
</div>
""", unsafe_allow_html=True)
```
