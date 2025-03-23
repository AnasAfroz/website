import streamlit as st
st.title("welcome to Anas website this is my first website ") 
st.header("python")
st.code("hello world")

name= st.text_input("Enter your name:")
favplayer = st.text_input("Enter your fav player:")
adr = st.text_area("Enter your text:")
classdata = st.selectbox("Enter Your class: ",(1,2,3,4,5,6,7,8,9,10))

button = st.button("Done")
if button: 
   st.markdown(f"""
name = {name}
favplayer: {favplayer}
address : {adr}
class:{classdata}""")
