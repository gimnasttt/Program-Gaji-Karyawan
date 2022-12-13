import streamlit as st
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pandas as pd


st.set_page_config(layout="centered", page_icon="💰", page_title="PROGRAM PERHITUNGAN GAJI KARYAWAN")

jabatan = 300000
jgol1 = 0.05
jgol2 = 0.10
jgol3 = 0.15


tunjangan = 300000
sma = 0.025
d1 = 0.05
d3 = 0.20
s1 = 0.30

jabatang1 = jabatan * jgol1
jabatang2 = jabatan * jgol2
jabatang3 = jabatan * jgol3

tunjangansma = tunjangan * sma
tunjangand1 = tunjangan * d1
tunjangand3 = tunjangan * d3
tunjangans1 = tunjangan * s1


selected = option_menu(
    menu_title = None,
    options = ["Home", "Kontak"],
    icons = ["house", "envelope"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    )
if selected == "Home":
    st.markdown("<h1 style='text-align: center;'>PROGRAM PERHITUNGAN GAJI KARYAWAN</h1>", unsafe_allow_html=True)


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_djwnoxew.json")

    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=200,
        width=None,
        key=None,
    )


    nama = st.text_input("Masukkan nama")
    golongan = st.selectbox(
        "Golongan jabatan",
        ('1', '2', '3'))
    if golongan == '1':
        pendidikan = st.selectbox(
            "Pendidikan",
            ('SMA', 'D1', 'D3', 'S1'))
        if pendidikan == 'SMA':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang1 + total + tunjangansma

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)
            else:
                jumlah = 300000 + jabatang1 + tunjangansma

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Jumlahnya adalah______________", jumlah)

        elif pendidikan == 'D1':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang1 + total + tunjangand1

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangand1)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)
            else:
                jumlah = 300000 + jabatang1 + tunjangand1


                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangand1)
                st.write("Jumlahnya adalah______________", jumlah)


        elif pendidikan == 'D3':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang1 + total + tunjangand3
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangand3)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang1 + tunjangand3
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangand3)
                st.write("Jumlahnya adalah______________", jumlah)
        else:
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang1 + total + tunjangans1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangans1)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)
            else:
                jumlah = 300000 + jabatang1 + tunjangans1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang1)
                st.write("Tunjangan pendidikan__________", tunjangans1)
                st.write("Jumlahnya adalah______________", jumlah)

    elif golongan == '2':
        pendidikan = st.selectbox(
            "Pendidikan",
            ('SMA', 'D1', 'D3', 'S1'))
        if pendidikan == 'SMA':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang2 + total + tunjangansma

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang2 + tunjangansma
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Jumlahnya adalah______________", jumlah)


        elif pendidikan == 'D1':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang2 + total + tunjangand1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangand1)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang2 + tunjangand1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangand1)
                st.write("Jumlahnya adalah______________", jumlah)

        elif pendidikan == 'D3':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang2 + total + tunjangand3

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangand3)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang2 + tunjangand3

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangand3)
                st.write("Jumlahnya adalah______________", jumlah)

        else:
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang2 + total + tunjangans1

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangans1)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang2 + tunjangans1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang2)
                st.write("Tunjangan pendidikan__________", tunjangans1)
                st.write("Jumlahnya adalah______________", jumlah)

    else:
        pendidikan = st.selectbox(
            "Pendidikan",
            ('SMA', 'D1', 'D3', 'S1'))
        if pendidikan == 'SMA':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang3 + total + tunjangansma
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang3 + tunjangansma
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Jumlahnya adalah______________", jumlah)

        elif pendidikan == 'D1':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang3 + total + tunjangand1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangand1)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang3 + tunjangand1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangand1)
                st.write("Jumlahnya adalah______________", jumlah)

        elif pendidikan == 'D3':
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang3 + total + tunjangand3

                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangand3)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang3 + tunjangand3
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangand3)
                st.write("Jumlahnya adalah______________", jumlah)

        else:
            jamkerja = st.number_input("Jumlah Jam Kerja", 0, 15)
            if jamkerja >= 8:
                total = (jamkerja - 8) * 3500

                jumlah = 300000 + jabatang3 + total + tunjangans1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangans1)
                st.write("Honor lembur__________________", total)
                st.write("Jumlahnya adalah______________", jumlah)

            else:
                jumlah = 300000 + jabatang3 + tunjangans1
                st.write('-' * 100)
                st.markdown("#")
                st.write("Karyawan yang bernama", nama)
                st.write("Honor yang diterima")
                st.write("Gaji pokok____________________", jabatan)
                st.write("Tunjangan jabatan_____________", jabatang3)
                st.write("Tunjangan pendidikan__________", tunjangansma)
                st.write("Jumlahnya adalah______________", jumlah)




if selected == "Kontak":
    st.markdown("<h2 style='text-align: center; color: white;'>Kami Selalu Mendengarkan Anda</h1>", unsafe_allow_html=True)
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    kontak = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_bt7iqzns.json")

    st_lottie(
        kontak,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",  # medium ; high
        height=250,
        width=None,
        key=None,
    )


    st.text("Whatsapp   : 0877-2555-3704            (Gimnastiar)")
