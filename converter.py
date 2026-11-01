import streamlit as st


st.title("Konverter")

tab1, tab2 = st.tabs(["Feet ↔ Meter", "Fahrenheit ↔ Celsius"])

with tab1:
    richtung = st.radio("Richtung", ["ft → m", "m → ft"], horizontal=True, key="r1")

    if richtung == "ft → m":
        feet = st.number_input("Feet", value=100.0, format="%.1f")
        st.metric("Meter", f"{feet * 0.3048:.1f} m")
    else:
        meter = st.number_input("Meter", value=10, format="%.1f")
        st.metric("Feet", f"{meter / 0.3048:.1f} ft")

with tab2:
    richtung = st.radio("Richtung", ["°F → °C", "°C → °F"], horizontal=True, key="r2")

    if richtung == "°F → °C":
        f = st.number_input("Fahrenheit", value=69.0, format="%.1f")
        st.metric("Celsius", f"{(f - 32) * 5 / 9:.1f} °C")
    else:
        c = st.number_input("Celsius", value=21.0, format="%.1f")
        st.metric("Fahrenheit", f"{c * 9 / 5 + 32:.1f} °F")
