import streamlit as st
from PIL import Image
import os
import google.generativeai as genai


# my api key
my_api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
# this will add the columns in the streamlit website.
page1, page2 = st.columns(2)

with page1:
    st.subheader("Hi There:wave:, It's Sarim.")
    st.title("Welcome to my website.")
    st.subheader("Let's get started.")    
# Adding the headings and titles.
with page2:
    st.image("images/sarim.jpg")

#giving some info about me.
st.title(" ")
st.header("<>WHO AM I?")
st.write("I am an undergraduate passed student who is learnig the programming. I've joined NLC (mandra) branch and currently doing the IOT course which involves many subjects and after this I'll be going to china for scholorship and to study there. I'm good at problem solving and I can do the best work in the programming.") 
# Adding the image
st.image("images/javapython.jpg")
# some info
st.write("Programming is the process of creating instructions that a computer can follow to perform tasks or solve problems. It involves writing code using programming languages like Python, Java, C++, and many others. Programmers use these languages to write algorithms and logic that dictate how software applications behave and interact with users and data.")

st.write("Programming requires logical thinking, problem-solving skills, and attention to detail. Programmers break down complex tasks into smaller, manageable steps and translate these steps into a language the computer can understand. They often collaborate with designers, analysts, and other stakeholders to create software that meets specific requirements and solves real-world problems efficiently. Programming is not just about writing code; it also involves testing, debugging, and refining code to ensure it functions correctly and efficiently. As technology evolves, programming continues to play a crucial role in shaping the digital world, from mobile apps to artificial intelligence systems and beyond.")


# another heading
st.markdown(" # Our webite features")
st.title(" ")
st.title(" ")
# here for the second 2column section part we again use the page1, page2 or some other name according to you.
page1, page2 = st.columns(2)
# heading 1
with page1:    
    st.subheader("<>User-Friendly Interface:")
    st.write("- Clean and intuitive design.")
    st.write("- Easy navigation and search functionality.")
    st.write("- Mobile-friendly layout.")
    # heading 2
    st.subheader("<>Teaching skills showcase:")
    st.write("- Highlight profiles and achievements of skilled educators.")
    st.write("- Provide detailed descriptions of their expertise and teaching methodologies.")
    # heading 3
    st.subheader("<>Online Gift Hampers:")
    st.write("- Offer a selection of customizable gift hampers.")
    st.write("- Include options for various occasions with personalized messages.")
    # heading 4
    st.subheader("<>Variety of Learning Resources:")
    st.write("- Articles, videos, podcasts, and eBooks.")
    st.write("- Quizzes and challenges to reinforce learning.")
    st.write("- Reference materials and cheat sheets.")

with page2:
    st.image("images/features.png")

# trying to "give the working link of the website.
st.markdown("[nvidia link](https://www.nvidia.com/en-us/)")
st.title(" ")

# here's my youtube channel link.
st.subheader("<>You can also visit my youtube channel")
st.write(" ")
st.write("Sorry but it's content is quite different but i hope you'll enjoy it. As i've made this before programming:broken_heart:")
st.markdown("[My Youtube Channel:](https://youtube.com/@mobitech6622?si=02iZCHv1AtKW2fwu)")

st.header("# HERE THE SAMPLE")
# another columns
page1, page2 = st.columns(2)
with page1:
    st.write("If you want to visit just click on the link on the right")
with page2:
    st.video("https://www.youtube.com/watch?v=wZpzJYKd48E")


st.write(" ")
st.image("images/talking.png")

# making my skills slidbar.
st.write(" ")
st.header("# My skills")
st.slider("programming",0,100,60)
st.slider("teaching",0,100,50)
st.slider("practical performing",0,100,60)

# now for uploading file.
st.file_uploader("upload the file")
# Taking the inputs form the user.
st.title("ANY QUESTIONS?")
user_question = st.text_input("You can ask any questoins here:thumbsup:") 
if st.button("search"):
    prompt = user_question
    response = model.generate_content(prompt)
    st.write(response.text)

# giving my contact number.
st.write(" ")
st.header("# MY CONTACT")
st.write("You can contact me by clicking here on the email:heart:")
st.write("muhammadsarim0864@gmail.com")
st.subheader("<> MY GITHUB LINK ")
st.markdown("[<My githublink>](https://github.com/sarim135/IOT-112-Sarim)")
# underconstruction heading
st.title("UNDER DEVELOPMENT:smile:")