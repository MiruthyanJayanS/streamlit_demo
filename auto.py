from tracemalloc import start
import streamlit as st

st.image("https://www.zebra.com/ap/en/services/signature-services/voice-enablement/jcr:content/mainpar/columncontrol_3f49/col1par/imagecomponent_917b/image.adapt.1280.jpg/1539184964829.jpg")
if st.button('click here'):
     st.write('It works')
else:
     st.write('You aint click')


starting_point = st.selectbox(
     'where are u now',
     ('specify address','location'))

st.write('You selected:', starting_point)

Destination = st.selectbox(
     'where would u like to go',
    ('Specify address','location'))

st.write('You selected:', Destination)

