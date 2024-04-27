import streamlit as st
import requests

# Function to fetch recipes from Spoonacular API
def fetch_recipes(cuisine):
    # API endpoint
    url = "https://api.spoonacular.com/recipes/complexSearch"
    # Parameters for filtering by cuisine
    params = {
        "cuisine": cuisine,
        "number": 20,  # Number of recipes to fetch
        "apiKey": "97da410b5ca24642a23ac35b160d26cf"  # Replace with your Spoonacular API key
    }
    # Make GET request
    response = requests.get(url, params=params)
    # Check if request was successful
    if response.status_code == 200:
        return response.json()['results']
    else:
        st.error("Failed to fetch recipes. Please try again later.")
        return None

# Function to fetch recipe details by ID
def fetch_recipe_details(recipe_id):
    # API endpoint
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/analyzedInstructions"
    # Parameters
    params = {
        "apiKey": "97da410b5ca24642a23ac35b160d26cf"  # Replace with your Spoonacular API key
    }
    # Make GET request
    response = requests.get(url, params=params)
    # Check if request was successful
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch recipe details. Please try again later.")
        return None

# Set page background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0; /* Off-white background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title('Recipe Generator')
st.write('Welcome to the Recipe Generator app! 🍽️')

# Customize selectbox color
st.markdown(
    """
    <style>
    /* Red color for selectbox */
    .st-eb .st-cs {
        background-color: red !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input options
cuisine_options = ['Italian', 'Indian', 'Mexican', 'Asian', 'Middle Eastern']  # Add more cuisines as needed
cuisine = st.selectbox('Select Cuisine', cuisine_options)

# Fetch recipes
recipes = fetch_recipes(cuisine)

# Display recipes
if recipes:
    st.subheader('Recipes')
    selected_recipe = st.selectbox('Select Recipe', [recipe['title'] for recipe in recipes])
    recipe_id = [recipe['id'] for recipe in recipes if recipe['title'] == selected_recipe][0]
    recipe_details = fetch_recipe_details(recipe_id)
    if recipe_details:
        st.subheader('Cooking Instructions')
        for step in recipe_details[0]['steps']:
            st.write(f"- {step['step']}")
