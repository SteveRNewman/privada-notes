# streamlit_app.py

import streamlit as st
import s3fs
import os

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Retrieve file contents.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

content = read_file("privada-df/myfile.csv")

# Print results.
for line in content.strip().split("\n"):
    name, pet = line.split(",")
    st.write(f"{name} has a :{pet}:")
# import streamlit as st
# import pandas as pd
# import numpy as np
# import os
# from PIL import Image

# action = st.radio('Action', ['Submit Notes', "Search Notes","View Archive"])
# if action == "Submit Notes":
#     with st.form('Form1'):
#         st.selectbox('Subscription Type', ['Privada Box', 'Farm Rolled', "Brian's Box",'Test Blends'], key=1)
#         st.selectbox('Year', ['2017', '2018', "2019",'2020', '2021', '2022'], key=2)
#         st.selectbox('Month', ['January', 'February', "March",'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December'], key=3)
#         st.text_input(label='Cigar One')
#         st.text_input(label='Cigar Two')
#         st.text_input(label='Cigar Three')
#         st.text_input(label='Cigar Four')
#         uploaded_file_f = st.file_uploader("Choose Notes Front")
#         if uploaded_file_f is not None:
#         # To read file as bytes:
#             bytes_data = uploaded_file_f.getvalue()
#             st.write(bytes_data)
#         uploaded_file_b = st.file_uploader("Choose Notes Back")
#         if uploaded_file_b is not None:
#         # To read file as bytes:
#             bytes_data = uploaded_file_b.getvalue()
#             st.write(bytes_data) 
#         # uploaded_files = st.file_uploader("Choose Notes Front", accept_multiple_files=False)
#         # for uploaded_file in uploaded_files:
#         #     bytes_data = uploaded_file.read()
#         #     st.write("filename:", uploaded_file.name)
#         #     st.write(bytes_data)
#         submit_button = st.form_submit_button(label='Submit')

# if action == "Search Notes":
#     search = st.selectbox ("Cigar", ['Cigar 1','Cigar 2','Cigar 3', 'Cigar 4'],key=4)
#     if search == 'Cigar 1':
#         with open("flower.png", "rb") as file:
#             btn = st.download_button(
#                     label="Download image",
#                     data=file,
#                     file_name="flower.png",
#                     mime="image/png"
#                 )
#             st.image('flower.png')
#     if search == 'Cigar 2':
#         with open("flower2.png", "rb") as file:
#             btn = st.download_button(
#                     label="Download image",
#                     data=file,
#                     file_name="flower2.png",
#                     mime="image/png"
#                 )
#             st.image('flower2.png')
#     if search == 'Cigar 3':
#         with open("flower3.png", "rb") as file:
#             btn = st.download_button(
#                     label="Download image",
#                     data=file,
#                     file_name="flower3.png",
#                     mime="image/png"
#                 )
#             st.image('flower3.png')
#     if search == 'Cigar 4':
#         with open("flower4.png", "rb") as file:
#             btn = st.download_button(
#                     label="Download image",
#                     data=file,
#                     file_name="flower4.png",
#                     mime="image/png"
#                 )
#             st.image('flower4.png')
# paths = Image.open('flower.png')

# if action == "View Archive":
#     df = pd.DataFrame([['Privada Box','2021','December','Cigar A','Cigar B','Cigar C', 'Cigar D','/flowers.png','flowers2.png'],
#     ['Privada Box','2021','December','Cigar A','Cigar B','Cigar C', 'Cigar D',paths,'flowers2.png'],
#     ['Privada Box','2021','December','Cigar A','Cigar B','Cigar C', 'Cigar D','/flowers.png','flowers2.png'],
#     ['Privada Box','2021','December','Cigar A','Cigar B','Cigar C', 'Cigar D','/flowers.png','flowers2.png'],
#     ['Privada Box','2021','December','Cigar A','Cigar B','Cigar C', 'Cigar D','/flowers.png','flowers2.png']],
#     columns=('Subscription', "Year", 'Month', 'Cigar 1', "Cigar 2", 'Cigar 3', 'Cigar 4', 'Notes Front', 'Notes Back'))

#     st.dataframe(df)
# # def save_uploadedfile(uploadedfile):
# #     with open(os.path.join('Data', uploadedfile.name), 'wb') as f:
# #      f.write(uploadedfile.getbuffer())
# #     return st.success('Saved File:{} to Data'.format(uploadedfile.name))

# # st.title(' PDF File upload')
# # st.text(' A simple way to upload files directly into a directory')
# # uploadedfiles = st.file_uploader('Upload PDF', type=["pdf"], accept_multiple_files=True)
# # for file in uploadedfiles:
# #     if uploadedfiles is not None:
# #         save_uploadedfile(file) 