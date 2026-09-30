import streamlit as st

st.set_page_config(page_title="FitBuddy AI", page_icon="💪")

st.title("💪 FitBuddy AI")
st.subheader("AI Fitness Plan Generator")

name = st.text_input("Your Name")
age = st.number_input("Age", 13, 100, 22)
weight = st.number_input("Weight (kg)", 20.0, 300.0, 60.0)

goal = st.selectbox(
    "Fitness Goal",
    ["Weight Loss", "Muscle Gain", "Strength", "General Fitness"]
)

intensity = st.selectbox(
    "Intensity",
    ["Beginner", "Moderate", "Advanced"]
)

if st.button("🚀 Generate Workout Plan"):

    if name:
        st.success("Workout plan generated successfully!")

        st.header(f"🏋️ {name}'s 7-Day Plan")

        st.write("### Day 1 - Full Body")
        st.write("Squats 3×10 • Push-ups 3×8 • Plank 3×20 sec")

        st.write("### Day 2 - Cardio")
        st.write("Brisk walking - 20 minutes")

        st.write("### Day 3 - Upper Body")
        st.write("Push-ups 3×10 • Shoulder raises 3×12")

        st.write("### Day 4 - Recovery")
        st.write("Walking • Mobility • Stretching")

        st.write("### Day 5 - Lower Body")
        st.write("Squats 3×12 • Lunges 3×10 • Calf raises 3×15")

        st.write("### Day 6 - Cardio + Core")
        st.write("Walking 20 minutes • Crunches 3×10 • Plank")

        st.write("### Day 7 - Rest")
        st.write("Rest • Stretching • Hydration")

        st.header("🥗 Nutrition Tip")
        st.info(
            f"For {goal}, eat balanced meals, include protein and vegetables, "
            "and stay well hydrated."
        )

    else:
        st.warning("Please enter your name.")