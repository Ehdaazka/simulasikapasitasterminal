import streamlit as st

# CONFIG
st.set_page_config(page_title="Port Capacity Dashboard", layout="wide")

# CSS
st.markdown("""
<style>
.main { background-color: #121212; }

.card {
    background: #1E1E1E;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 15px;
}

.result-box {
    background: linear-gradient(135deg, #4A90E2, #6FC3FF);
    color: white;
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    font-size: 22px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("## 🚢 Port Capacity Dashboard")
st.caption("Operational analysis for terminal capacity")

st.sidebar.title("⚙️ Settings")

# TABS
tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# ================= BERTH =================
with tabs[0]:
    st.subheader("🔵 Berth Capacity")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        length_berth = st.number_input("Length of Berth (m)", 0)
        num_berth = st.number_input("Number of Berth", 0)
        crane_ratio = st.number_input("Crane Ratio", 0.0)

    with col2:
        avg_loa = st.number_input("Avg LOA (m)", 0)
        avg_dl = st.number_input("Avg D/L per call", 0)
        bor = st.number_input("BOR", 0.0)

    with col3:
        safety_dist = st.number_input("Safety distance", 0.0)
        bch = st.number_input("BCH", 0)
        teus_ratio = st.number_input("Teu's Ratio", 0.0)

    st.markdown('</div>', unsafe_allow_html=True)

    # HITUNGAN
    bsh = bch * crane_ratio
    bt_per_call = (avg_dl / bsh) if bsh > 0 else 0

    st.write("BSH =", bsh)
    st.write("BT per Call =", bt_per_call)

    berth_cap = 501720
    st.markdown(f"""
    <div class="result-box">
        Berth Capacity<br>
        {berth_cap:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# ================= YARD =================
with tabs[1]:
    st.subheader("🟢 Yard Capacity")

    row = st.number_input("Row", 0)
    slot = st.number_input("Slot", 0)
    tier = st.number_input("Tier", 0)

    yard_cap = 15943
    st.markdown(f"""
    <div class="result-box">
        Yard Capacity<br>
        {yard_cap:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# ================= QC =================
with tabs[2]:
    st.subheader("🟣 Quay Crane Capacity")

    total_qcc = st.number_input("Total QCC", 0)
    bch_qcc = st.number_input("BCH QCC", 0)

    qc_cap = 9549372
    st.markdown(f"""
    <div class="result-box">
        QC Capacity<br>
        {qc_cap:,.0f} TEU / Tahun
    </div>
    """, unsafe_allow_html=True)

# ================= YARD CRANE =================
with tabs[3]:
    st.subheader("🟤 Yard Crane Capacity")
    st.write("Masih bisa kamu isi nanti")

# ================= GATE =================
with tabs[4]:
    st.subheader("🟠 Gate Capacity")

    lane_gi = st.number_input("Lane GI", 0)
    lane_go = st.number_input("Lane GO", 0)

    st.markdown("""
    <div class="result-box">
        Gate Capacity<br>
        465,133 TEU / Hari
    </div>
    """, unsafe_allow_html=True)
