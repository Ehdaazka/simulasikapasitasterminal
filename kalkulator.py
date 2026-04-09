import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="Port Capacity", layout="wide")

# ======================
# CUSTOM CSS (NEW UI)
# ======================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background-color: #D9E1F1;
}

/* CONTAINER */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 0rem;
}

/* CARD */
.card {
    background: linear-gradient(135deg, #1E2E4F, #31487A);
    padding: 1.2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 1rem;
    color: white;
}

/* TITLE */
.card-title {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
    color: #8FB3E2;
}

/* METRIC */
[data-testid="stMetricValue"] {
    font-size: 1.6rem;
    font-weight: bold;
    color: white;
}

[data-testid="stMetricLabel"] {
    color: #D9E1F1;
}

/* INPUT */
label {
    color: #D9E1F1 !important;
}

input {
    background-color: #192338 !important;
    color: white !important;
    border-radius: 6px !important;
    border: 1px solid #31487A !important;
}

/* TAB */
button[data-baseweb="tab"] {
    color: #1E2E4F;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #31487A !important;
    color: white !important;
    border-radius: 8px;
}

/* ALERT */
.stAlert {
    background-color: #8FB3E2 !important;
    color: #192338 !important;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# TITLE
# ======================
st.markdown("<h1 style='color:#192338;'>🚢 Terminal Capacity Simulation</h1>", unsafe_allow_html=True)

tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# ======================
# TAB 1: BERTH
# ======================
with tabs[0]:
    left, right = st.columns([3,1])

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🔵 Berth Capacity Input</div>', unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)
        length_berth = c1.number_input("Length of Berth", value=0)
        avg_loa = c2.number_input("Avg LOA", value=0)
        bch = c3.number_input("BCH", value=0)
        crane_ratio = c4.number_input("Crane Ratio", value=0.0, step=0.1)

        c5, c6, c7, c8 = st.columns(4)
        avg_dl = c5.number_input("Avg D/L", value=0)
        teus_ratio = c6.number_input("Teus Ratio", value=0.0, step=0.01)
        safety_dist = c7.number_input("Safety Dist", value=1.1, disabled=True)
        bor = c8.number_input("BOR", value=0.65, disabled=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # CALCULATION
        num_berth = length_berth / (avg_loa * safety_dist) if avg_loa > 0 else 0
        bsh = bch * crane_ratio
        bt_per_call = avg_dl / bsh if bsh > 0 else 0
        total_hours = 8760
        ship_call_year = (total_hours / bt_per_call) * bor if bt_per_call > 0 else 0
        berth_cap = ship_call_year * avg_dl * teus_ratio

        # RESULT
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">📊 Live Calculation</div>', unsafe_allow_html=True)

        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Num Berth", f"{num_berth:.2f}")
        r2.metric("BSH", f"{bsh:.2f}")
        r3.metric("BT/Call", f"{bt_per_call:.2f}")
        r4.metric("Ship/Yr", f"{ship_call_year:.0f}")

        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card" style="background: linear-gradient(135deg, #192338, #1E2E4F);">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🚀 Final Result</div>', unsafe_allow_html=True)

        st.metric("Berth Capacity", f"{berth_cap:,.0f}", "TEU/year")

        st.markdown("**Constants**")
        st.caption(f"Total Hours: {total_hours}")
        st.caption(f"BOR: {bor}")

        st.markdown('</div>', unsafe_allow_html=True)

# ======================
# TAB 2: YARD
# ======================
with tabs[1]:
    left, right = st.columns([3,1])

    with left:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🟢 Yard Capacity Input</div>', unsafe_allow_html=True)

        y1, y2, y3 = st.columns(3)
        row = y1.number_input("Row", value=0)
        slot = y2.number_input("Slot", value=0)
        tier = y3.number_input("Tier", value=0)

        y4, y5, y6 = st.columns(3)
        eff_cap = y4.number_input("Effective Cap", value=0)
        dauling = y5.number_input("Dwell Time", value=1)
        yor_max = y6.number_input("YOR Max (%)", value=70)

        yard_cap = (slot * row * tier * 365 / dauling) * (yor_max/100)

        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card" style="background: linear-gradient(135deg, #192338, #1E2E4F);">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">🚀 Final Result</div>', unsafe_allow_html=True)

        st.metric("Yard Capacity", f"{yard_cap:,.0f}", "TEU/year")

        st.markdown('</div>', unsafe_allow_html=True)

# ======================
# TAB 5: GATE
# ======================
with tabs[4]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🟠 Gate In & Out</div>', unsafe_allow_html=True)
    st.warning("Gate logic belum dibuat")
    st.markdown('</div>', unsafe_allow_html=True)
