# streamlit_app.py

# import streamlit as st
# import s3fs
# import os

# # Create connection object.
# # `anon=False` means not anonymous, i.e. it uses access keys to pull data.
# fs = s3fs.S3FileSystem(anon=False)

# # Retrieve file contents.
# # Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def read_file(filename):
#     with fs.open(filename) as f:
#         return f.read().decode("utf-8")

# content = read_file("privada-df/myfile.csv")

# # Print results.
# for line in content.strip().split("\n"):
#     name, pet = line.split(",")
#     st.write(f"{name} has a :{pet}:")
import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image
import s3fs


df = pd.DataFrame(columns=('Subscription', "Year", 'Month', 'Cigar 1', "Cigar 2", 'Cigar 3', 'Cigar 4'))#[['Privada Box','2021','December','Cigar A','Cigar B','Cigar C', 'Cigar D','flowers.png','flowers2.png']],
    #columns=('Subscription', "Year", 'Month', 'Cigar 1', "Cigar 2", 'Cigar 3', 'Cigar 4', 'Notes Front', 'Notes Back'))
# my_dict1 = {"Cigar 1":[],"Cigar 2":[],"Cigar 3":[],"Cigar 4":[]}
# my_dict = {"Subscription":[],"Year":[],"Month":[],"Cigars": my_dict1,"Notes Front":[],"Notes Back":[]}

# my_dict["Cigars"] = my_dict1
action = st.sidebar.radio('Action', ['Submit Notes', "Search Notes"])
if action == "Submit Notes":
    with st.sidebar.form(key ='Form1'):
        sub = st.selectbox('Subscription Type', ['Privada Box', 'Farm Rolled', "Brian's Box",'Test Blends'], key=1)
        year = st.selectbox('Year', ['2017', '2018', "2019",'2020', '2021', '2022'], key=2)
        month = st.selectbox('Month', ['January', 'February', "March",'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December'], key=3)
        c1 = st.text_input(label='Cigar One')
        c2 = st.text_input(label='Cigar Two')
        c3 = st.text_input(label='Cigar Three')
        c4 = st.text_input(label='Cigar Four')
        f_uploaded_file = st.file_uploader("Choose Notes Front")
        if f_uploaded_file is not None:
            image = Image.open(f_uploaded_file)
        b_uploaded_file = st.file_uploader("Choose Notes Back")
        if b_uploaded_file is not None:
            image = Image.open(b_uploaded_file)

        submit = st.form_submit_button(label='Submit')
        if submit:
            df2 = pd.DataFrame([[sub,year,month,c1,c2,c3,c4,c4,c4]], columns=('Subscription', "Year", 'Month', 'Cigar 1', "Cigar 2", 'Cigar 3', 'Cigar 4','Front','Back'))#,uff,ufb])
        s3 = s3fs.S3FileSystem(anon=False)

        # Use 'w' for py3, 'wb' for py2
        with s3.open('privada-df/privada_data.csv','w') as f:
            df2.to_csv(f)

    st.write("Archive of notes already submitted can be sorted by clicking on the column name.")
    # Create connection object.
    # `anon=False` means not anonymous, i.e. it uses access keys to pull data.
    fs = s3fs.S3FileSystem(anon=False)

    # Retrieve file contents.
    # Uses st.cache to only rerun when the query changes or after 10 min.
    @st.cache(ttl=600)
    def read_file(filename):
        with fs.open(filename) as f:
            return f.read()#.decode("utf-8")

    content = read_file("privada-df/privada_data.csv")

    # Print results.

    st.dataframe(content, width=2000)

    

if action == "Search Notes":
    search = st.selectbox ("Cigar", ['Cigar 1','Cigar 2','Cigar 3', 'Cigar 4'],key=4)
    if search == 'Cigar 1':
        with open("flower.png", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="flower.png",
                    mime="image/png"
                )
            st.image('flower.png')
    if search == 'Cigar 2':
        with open("flower2.png", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="flower2.png",
                    mime="image/png"
                )
            st.image('flower2.png')
    if search == 'Cigar 3':
        with open("flower3.png", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="flower3.png",
                    mime="image/png"
                )
            st.image('flower3.png')
    if search == 'Cigar 4':
        with open("flower4.png", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="flower4.png",
                    mime="image/png"
                )
            st.image('flower4.png')


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