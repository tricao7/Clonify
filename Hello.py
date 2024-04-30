import requests
import scipy.io.wavfile as wav
import streamlit as st


def main():
    # Display image and center
    st.set_page_config(initial_sidebar_state="collapsed")

    st.markdown(
        """
        <style>
        [data-testid="collapsedControl"] {
        display: none
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.image("images/Clonify.png", use_column_width=True)

    # Display title
    st.title("Welcome to Clonify!")
    st.markdown("---")

    # Display description
    st.write(
        "Clonify is a text-to-speech (TTS) application that allows you to generate voice from text. \
        You can upload a .wav file and enter text to be spoken. \
        The generated audio will be a voice clone of the uploaded file."
    )
    st.write("Instructions:")
    st.write("1. Upload a 30 second .wav file that you want to clone the voice of.")
    with st.expander("Click here for a sample prompt (for best results): "):
        st.write(
            "   'The North Wind and the Sun were disputing which was the stronger, when a traveler came along wrapped in a warm cloak.\
            They agreed that the one who first succeeded in making the traveler take his cloak off should be considered stronger than the other.\
            Then the North Wind blew as hard as he could, but the more he blew the more closely did the traveler fold his cloak around him;\
            and at last the North Wind gave up the attempt. Then the Sun shined out warmly, and immediately the traveler took off his cloak.\
            And so the North Wind was obliged to confess that the Sun was the stronger of the two.'"
        )
    st.write("2. Enter the text you want to be spoken.")
    st.write("3. Adjust the guidance, top P, and top K parameters.")
    st.write("4. Click the 'Generate Voice' button to generate the audio.")
    if st.button("Demo"):
        st.switch_page("pages/app.py")
    if st.button("Sign up/Log in"):
        st.switch_page("pages/user_auth.py")
    # Display horizontal line
    st.markdown("---")


if __name__ == "__main__":
    main()
