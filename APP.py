import streamlit as st

# Title
st.title("💰 Simple Interest Calculator")

# User Inputs
principal = st.number_input(
    "Enter Principal Amount (₹)",
    min_value=0.0,
    value=10000.0,
    step=100.0
)

rate = st.number_input(
    "Enter Rate of Interest (%)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

time_year = st.number_input(
    "Enter Time (Years)",
    min_value=0,
    value=1,
    step=1
)

time_month = st.number_input(
    "Enter Additional Months",
    min_value=0,
    max_value=11,
    value=0,
    step=1
)

# Calculate Button
if st.button("Calculate"):
    time = time_year + (time_month / 12)
    interest = (principal * rate * time) / 100
    maturity_amount = principal + interest

    st.success(f"Simple Interest: ₹{interest:.2f}")
    st.success(f"Maturity Amount: ₹{maturity_amount:.2f}")