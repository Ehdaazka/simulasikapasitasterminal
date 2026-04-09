import streamlit as st

# Setup page agar lebar dan judul tab browser rapi
st.set_page_config(page_title="Port Capacity", layout="wide")

# CSS untuk memadatkan spasi antar elemen
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 0rem; }
    h3 { margin-bottom: 0.5rem; font-size: 1.2rem !important; }
    [data-testid="stMetricValue"] { font-size: 1.5rem !important; }
    div[data-testid="column"] { padding: 0.5rem; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚢 Port Operational Capacity")

tabs = st.tabs(["Berth", "Yard", "Quay Crane", "Yard Crane", "Gate"])

# --- TAB 1: BERTH ---
with tabs[0]:
    # Menggunakan 2 kolom besar: Kiri untuk Input & Auto-Calc, Kanan untuk Ringkasan Utama
    main_col, side_col = st.columns([3, 1])

    with main_col:
        st.subheader("🔵 Parameter Input & Auto-Calculation")
        
        # Row 1: Input Utama
        c1, c2, c3, c4 = st.columns(4)
        length_berth = c1.number_input("Length of Berth (m)", value=0)
        avg_loa = c2.number_input("Avg LOA (m)", value=0)
        bch = c3.number_input("BCH", value=0)
        crane_ratio = c4.number_input("Crane Ratio", value=0.0, step=0.1)

        # Row 2: Input & Locked Params
        c5, c6, c7, c8 = st.columns(4)
        avg_dl = c5.number_input("Avg D/L per call", value=0)
        teus_ratio = c6.number_input("Teu's Ratio", value=0.0, step=0.01)
        safety_dist = c7.number_input("Safety Dist (Locked)", value=1.1, disabled=True)
        bor = c8.number_input("BOR (Locked)", value=0.65, disabled=True)

        st.divider()

        # LOGIKA PERHITUNGAN
        # 1. Number Of Berth
        num_berth = length_berth / (avg_loa * safety_dist) if avg_loa > 0 else 0
        # 2. BSH
        bsh = bch * crane_ratio
        # 3. BT per Call
        bt_per_call = avg_dl / bsh if bsh > 0 else 0
        # 4. Total Hours (Locked)
        total_hours = 8760
        # 5. Total Ship Call / Year
        ship_call_year = (total_hours / bt_per_call) * bor if bt_per_call > 0 else 0
        # 6. Final Capacity
        berth_cap = ship_call_year * avg_dl * teus_ratio

        # Baris Hasil Otomatis (Ringkas)
        st.write("🔍 **Live Calculation Results:**")
        r1, r2, r3, r4 = st.columns(4)
        r1.metric("Num of Berth", f"{num_berth:.2f}")
        r2.metric("BSH", f"{bsh:.2f}")
        r3.metric("BT/Call", f"{bt_per_call:.2f}")
        r4.metric("Ship Call/Yr", f"{ship_call_year:.0f}")

    with side_col:
        # Box Hasil Akhir di Samping agar terlihat jelas tanpa scroll
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.info("### Final Result")
        st.metric("Berth Capacity", f"{berth_cap:,.0f}", delta="TEU/tahun")
        
        with st.expander("Lihat Konstanta"):
            st.write(f"Total Hours: {total_hours}")
            st.write(f"BOR Target: {bor}")

# --- TAB 2: YARD (Dibuat Ringkas Juga) ---
with tabs[1]:
    col_y_left, col_y_right = st.columns([3, 1])
    with col_y_left:
        st.subheader("🟢 Yard Input")
        y1, y2, y3 = st.columns(3)
        row = y1.number_input("Row", value=0)
        slot = y2.number_input("Slot", value=0)
        tier = y3.number_input("Tier", value=0)
        
        y4, y5, y6 = st.columns(3)
        eff_cap = y4.number_input("Effective Cap", value=0)
        dauling = y5.number_input("Dauling Time", value=0)
        yor_max = y6.number_input("YOR Max (%)", value=70)
        
        # Rumus sederhana
        yard_cap = (slot * row * tier * 365 / (dauling if dauling > 0 else 1)) * (yor_max/100)

    with col_y_right:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.success("### Final Result")
        st.metric("Yard Capacity", f"{yard_cap:,.0f}", "TEU/tahun")

# --- TAB LAINNYA ---
with tabs[4]:
    st.subheader("🟠 Gate Summary")
    st.columns(3)[0].warning("Gate In & Out logic ready.")
