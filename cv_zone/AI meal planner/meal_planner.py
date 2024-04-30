# streamlit_meal_planner.py

import streamlit as st
import random

# Function to generate a creative meal name
def generate_meal_name():
    adjectives = ["Spicy", "Savory", "Zesty", "Delicious", "Hearty", "Exotic"]
    proteins = ["Chicken", "Salmon", "Tofu", "Beef", "Lentils"]
    sides = ["Quinoa", "Sweet Potato", "Broccoli", "Cauliflower Rice", "Mixed Greens"]
    return f"{random.choice(adjectives)} {random.choice(proteins)} with {random.choice(sides)}"

# Main Streamlit app
def main():
    st.title("AI Meal Planner")

    # User input: Age, weight, height, gender
    age = st.slider("Your Age", 18, 100, 30)
    weight = st.slider("Your Weight (kg)", 40, 200, 70)
    height = st.slider("Your Height (cm)", 140, 220, 170)
    gender = st.radio("Your Gender", ["Male", "Female"])

    # Calculate BMR (Basal Metabolic Rate)
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    # Calorie targets for each meal
    target_calories = bmr // 3

    # Generate meal plans
    breakfast = generate_meal_name()
    lunch = generate_meal_name()
    dinner = generate_meal_name()

    # Display meal plans
    st.subheader("Your Personalized Meal Plan:")
    st.write(f"Breakfast: {breakfast} ({target_calories} kcal)")
    st.write(f"Lunch: {lunch} ({target_calories} kcal)")
    st.write(f"Dinner: {dinner} ({target_calories} kcal)")

if __name__ == "__main__":
    main()
