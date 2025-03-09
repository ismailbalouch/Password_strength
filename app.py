import streamlit as st
import re
import random
import string

def password_strength_meter(password):
    score = 0  # 
    feedback = []

    # Be at least 8 characters long
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    # Contain uppercase & lowercase letters
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase & lowercase letters")

    # Include at least one digit (0-9)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit")

    # Have one special character (!@#$%&*)
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character")

    # Score System
    if score == 4:
        return "Strong password", feedback, score
    elif score == 3:
        return "Medium password", feedback, score
    else:
        return "Password is too weak", feedback, score


def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return password


# Creation of UI
if __name__ == "__main__":
    st.title("Password Strength Meter")
    st.write("_____________________")
    st.write("Generate a Strong Password")
    password = st.text_input("Enter Your Password", type="password")

    if st.button("Check") and password:
        result, feedback, score = password_strength_meter(password)
        st.write(f"Your password is: {result}")

        if feedback:
            st.write("Feedback:")
            for fb in feedback:
                st.write(f"- {fb}")

        st.write(f"Your score is: {score}")
