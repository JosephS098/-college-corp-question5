import streamlit as st
from PIL import Image
st.set_page_config(page_title="QR Code Quiz 5", page_icon="🧠")


st.title("🧩 College Corps Mid-Year Workshop!")
st.markdown("<h3 style='color:#4CAF50;'>Let's see if you can solve this!</h3>", unsafe_allow_html=True)
question = "What communication style is being used in the image above?"
image = Image.open('Aggressive.webp')
st.image(image)
choices = ["Assertive", "Aggressive", "Passive", "Passive-Aggressive"]
correct_answer = "Aggressive"


if "answered_correctly" not in st.session_state:
    st.session_state.answered_correctly = False

st.subheader(question)
user_choice = st.radio("Choose your answer:", choices, index=None)


if st.button("Submit"):
    if user_choice == correct_answer:
        st.session_state.answered_correctly = True
        st.success("✅ Correct! Great job!")
    else:
        st.warning("❌ Try again!")


if st.session_state.answered_correctly:
    st.balloons()
    st.info("Find Facilitator for next clue!")
