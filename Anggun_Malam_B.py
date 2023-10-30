import pickle
import streamlit as st

model = pickle.load(open('Anggun_Malam_B.sav','rb'))

st.title('Estimasi Harga Rumah di Chicago')

Bedroom = st.number_input('Input Kamar')
Space = st.number_input('Input Ukuran')
Room = st.number_input('Input Jumlah Kamar')
Lot = st.number_input('Lebar')
Tax = st.number_input('Input Pajak')
Bathroom = st.number_input('Input Kamar Mandi')
Garage = st.number_input('Input Garasi')
Condition = st.number_input('Input Kondisi Rumah (1 = Bagus dan 0 = Tidak)')

predict = ''

if st.button('proses'):
    features = [[Bedroom,Space,Room,Lot,Tax,Bathroom,Garage,Condition]]
    predict = model.predict(features)

    st.write('Harga Rumah di Chicago:', predict[0])
