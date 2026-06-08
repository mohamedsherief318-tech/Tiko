import streamlit as st

st.set_page_config(page_title="Tiko - Real Estate AI", layout="wide")
st.title("Tiko - Real Estate AI")
st.subheader("Invest Smarter, Faster.")

lang = st.sidebar.selectbox("Language / اللغة", ["English", "العربية"])

if st.sidebar.button("Upgrade to Premium"):
    st.sidebar.success("Subscription: $29/mo or $290/yr")

col1, col2 = st.columns(2)
col1.metric("Market Index", "84.2", "+2.1%")
col2.metric("Investment Score", "92/100", "High")

st.area_chart([10, 20, 15, 45, 30, 60, 50])
