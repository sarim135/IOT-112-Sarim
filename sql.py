import sqlite3
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, MARKS, 
    CLASS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The Response is")
    st.write(response)

    # Connect to SQLite database
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()

# Insert sample data into the STUDENT table
    cur.execute("""
    INSERT INTO STUDENT (NAME, MARKS, CLASS) VALUES ('John', 85, 'Math');
    INSERT INTO STUDENT (NAME, MARKS, CLASS) VALUES ('Alice', 92, 'Science');
    INSERT INTO STUDENT (NAME, MARKS, CLASS) VALUES ('Bob', 78, 'History');
""")
    conn.commit()


    # Execute SQL query and display results
    try:
        rows = read_sql_query(response, "student.db")
        if rows:
            st.subheader("Query Result")
            for row in rows:
                st.write(row)
        else:
            st.write("No results found.")
    except Exception as e:
        st.write(f"Error executing SQL query: {e}")

    # Close database connection
    conn.close()
