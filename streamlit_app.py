import streamlit as st
action = st.radio('Action', ['Submit Notes', "Search Notes"])
if action == "Submit Notes":
    with st.form('Form1'):
        st.selectbox('Subscription Type', ['Privada Box', 'Farm Rolled', "Brian's Box",'Test Blends'], key=1)
        st.selectbox('Year', ['2017', '2018', "2019",'2020', '2021', '2022'], key=2)
        st.selectbox('Month', ['January', 'February', "March",'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December'], key=3)
        st.text_input(label='Cigar One')
        st.text_input(label='Cigar Two')
        st.text_input(label='Cigar Three')
        st.text_input(label='Cigar Four')
        uploaded_files = st.file_uploader("Choose Notes Images", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
        submit_button = st.form_submit_button(label='Submit')

if action == "Search Notes":
    st.selectbox ("Cigar", ['Cigar 1','Cigar 2','Cigar 3', 'Cigar 4'],key=4)
    with open("flower.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="flower.png",
             mime="image/png"
           )
    st.image('flower.png')
# def save_uploadedfile(uploadedfile):
#     with open(os.path.join('Data', uploadedfile.name), 'wb') as f:
#      f.write(uploadedfile.getbuffer())
#     return st.success('Saved File:{} to Data'.format(uploadedfile.name))

# st.title(' PDF File upload')
# st.text(' A simple way to upload files directly into a directory')
# uploadedfiles = st.file_uploader('Upload PDF', type=["pdf"], accept_multiple_files=True)
# for file in uploadedfiles:
#     if uploadedfiles is not None:
#         save_uploadedfile(file) 