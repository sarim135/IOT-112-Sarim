import streamlit as st

# adding title.
st.title("Streamlit Basics")
st.header(" ")
# it just add the checkbox that you can mark as tick.
st.subheader("Adding the check box")
st.checkbox("check0")
st.checkbox("check1")
st.checkbox("check2")
# it adds options like in MCQs paper.
st.write(" ")
st.subheader("Options method")
st.radio('Options',['option 1','option 2','option 3'])
# adding the button.
st.button('button')
st.header("Color picker")
st.color_picker(' ')
# adding the date input method 
st.subheader("Input date")
st.date_input("Input date")
# adding the input time method.
st.subheader("Input Time")
st.time_input("input time")
# adding the text input method.
st.text_input('Text input', placeholder='Enter your Name')
# adding the input chat method.
st.chat_input("chat")
# adding the input number method.
st.number_input("123")



