import streamlit as st

st.title("🚢 Terminal Capacity Simulator")

# =========================
# 1. BERTH CAPACITY
# =========================
st.header("1. Berth Capacity")

# INPUT (user isi)
length = st.number_input("Length of Berth", 0.0)
loa = st.number_input("Avg LOA", 0.0)
dl = st.number_input("Avg D/L per Call", 0.0)
bch = st.number_input("BCH", 0.0)
crane_ratio = st.number_input("Crane Ratio", 0.0)

# TETAPAN (sudah ditentukan)
hours = 8760
bor = 0.65
teus = 1.13

# BUTTON HITUNG
btn_berth = st.button("Hitung Berth Capacity")

if btn_berth:
    if bch * crane_ratio != 0:
        bt = dl / (bch * crane_ratio)
    else:
        bt = 0

    if bt != 0:
        ship_call = hours / bt
    else:
        ship_call = 0

    berth_capacity = ship_call * dl * teus

    st.write("BT per Call =", bt)
    st.write("Ship Call =", ship_call)
    st.success(f"Berth Capacity = {berth_capacity:,.0f}")


# =========================
# 2. YARD CAPACITY
# =========================
st.header("2. Yard Capacity")

row = st.number_input("Row", 0)
slot = st.number_input("Slot", 0)
tier = st.number_input("Tier", 0)
dwell = st.number_input("Dwell Time", 0.0)

# TETAPAN
yor = 0.7
days = 365

btn_yard = st.button("Hitung Yard Capacity")

if btn_yard:
    effective = row * slot * tier

    if dwell != 0:
        capacity = (effective * yor * days) / dwell
    else:
        capacity = 0

    st.write("Effective Capacity =", effective)
    st.success(f"Yard Capacity = {capacity:,.0f}")


# =========================
# 3. QUAY CRANE
# =========================
st.header("3. Quay Crane Capacity")

qcc = st.number_input("Total QCC", 0)
bch_qcc = st.number_input("BCH QCC", 0)

# TETAPAN
hours_qc = 24
days_qc = 365
util = 0.55
teus_qc = 1.13

btn_qc = st.button("Hitung QC Capacity")

if btn_qc:
    capacity = qcc * bch_qcc * hours_qc * days_qc * util * teus_qc
    st.success(f"QC Capacity = {capacity:,.0f}")


# =========================
# 4. YARD CRANE
# =========================
st.header("4. Yard Crane Capacity")

rtg = st.number_input("Total RTG", 0)
bch_rtg = st.number_input("BCH RTG", 0)

# TETAPAN
hours_yc = 24
days_yc = 365
util_yc = 0.55
teus_yc = 1.13

btn_yc = st.button("Hitung Yard Crane Capacity")

if btn_yc:
    capacity = rtg * bch_rtg * hours_yc * days_yc * util_yc * teus_yc
    st.success(f"Yard Crane Capacity = {capacity:,.0f}")


# =========================
# 5. GATE CAPACITY
# =========================
st.header("5. Gate Capacity")

lane_in = st.number_input("Lane In", 0)
service_in = st.number_input("Service Time In (detik)", 0.0)

lane_out = st.number_input("Lane Out", 0)
service_out = st.number_input("Service Time Out (detik)", 0.0)

# TETAPAN
time = 86400
days_gate = 365

btn_gate = st.button("Hitung Gate Capacity")

if btn_gate:
    if service_in != 0:
        gate_in = (time / service_in) * lane_in * days_gate
    else:
        gate_in = 0

    if service_out != 0:
        gate_out = (time / service_out) * lane_out * days_gate
    else:
        gate_out = 0

    st.write("Gate In =", gate_in)
    st.write("Gate Out =", gate_out)
    st.success("Perhitungan Gate selesai")
