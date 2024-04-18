import re
import streamlit as st

with st.form("os"):
    st.write("Please enter your operating system")
    val = st.radio(
        "Please enter your operating system",
        ('Android', 'Windows', 'IOS', 'MacOS'))
    st.write("لینک مورد نظر خود را وارد کنید:")
    st.text("لینک مد نظر :")
    link = st.text_input(label="link", max_chars=150)
    submitted = st.form_submit_button("سنجش امنیت")
operating_system = val
if submitted:
    if link.startswith("https://") and link.endswith((".com", ".ai", ".ir")):
        st.write(f"این لینک جهت استفاده در ,{operating_system} مجاز است . ")
    elif link.startswith("http://"):
        st.write(":red[این لینک نامعتبر است در صورتیکه فرستنده آن را میشناسید از آن استفاده کنید]")
    else:
        st.write(f" این لینک جهت استفاده{operating_system} مجاز است . ")