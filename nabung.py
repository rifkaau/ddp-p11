import streamlit as st

st.title("Halaman Menabung")

# Halaman Menabung
with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)" , min_value=0)
    submit_button = st.form_submit_button(label = "Menabung")
    if submit_button:
        st.session_state["jumlah"].append({
            "Tipe" : "Menabung",
            "Nama" : nama,
            "jumlah" : jumlah
        })
        st.success("Anda Berhasil Menabung")
    else:
        st.error("Anda Gagal Menabung")