import requests
import scipy.io.wavfile as wav
import streamlit as st


def main():
    st.set_page_config(page_title="Landing Page",
                       initial_sidebar_state="collapsed")

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Sen:wght@400..800&display=swap');
        
        .stButton>button {
            border: 2px solid #8A2BE2;
            border-radius: 5px;
            background-color: #951CCE;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            transition: background-color 0.3s, color 0.3s;
        }
        .stButton>button:hover {
            background-color: white;
            color: #951CCE;
        }
        
        [data-testid="collapsedControl"] {
            display: none;
        }
        .title {
            text-align: center;
        }
        
        .body {
            font-size: 16px;
            font-family: 'Montserrat', sans-serif;
            font-optical-sizing: auto;
            font-weight: 100;
            font-style: thin;
        }
        
        .header {
           font-family: 'Sen', sans-serif;
           font-size: 35px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.image("images/Clonify.png", use_column_width=True)
    st.markdown('<h1 class="title">Elevate Your Audio Experience with AI-Generated Voices</h1>',
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="body">Let your content go beyond text with our realistic TTS generation models. Generate your own custom high-quality audio.</div>',
                    unsafe_allow_html=True)
        st.markdown("""<br>""", unsafe_allow_html=True)
        if st.button("Try It Now"):
            st.switch_page("pages/app.py")

    with col2:
        st.markdown('<div class="body">Join us to personalize your experience and access premium features like access to past voices and audio outputs!</div>',
                    unsafe_allow_html=True)
        st.markdown("""<br>""", unsafe_allow_html=True)

        if st.button("Sign Up / Log In"):
            st.switch_page("pages/user_auth.py")

    st.markdown("---")
    st.markdown('<div class="header">How It Works</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="body">Clonify is a text-to-speech (TTS) application that allows you to generate voice from text. You can upload a .wav file and enter text to be spoken. The generated audio will be a voice clone of the uploaded file.</div>', unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown('<div class="body">Follow these simple steps to try it yourself:</h1>',
                unsafe_allow_html=True)
    st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown('<div class="body">1. Record a 30 second .wav file using the voice you want to clone.</h1>',
                unsafe_allow_html=True)
    with st.expander("Click here for a sample prompt (for best results): "):
        st.markdown('<div class="body">The North Wind and the Sun were disputing which was the stronger, when a traveler came along wrapped in a warm cloak.\
            They agreed that the one who first succeeded in making the traveler take his cloak off should be considered stronger than the other.\
            Then the North Wind blew as hard as he could, but the more he blew the more closely did the traveler fold his cloak around him;\
            and at last the North Wind gave up the attempt. Then the Sun shined out warmly, and immediately the traveler took off his cloak.\
            And so the North Wind was obliged to confess that the Sun was the stronger of the two.</h1>', unsafe_allow_html=True)
    st.markdown('<div class="body">2. Click the Try it Now button above to redirect to our free demo.</h1>',
                unsafe_allow_html=True)
    st.markdown('<div class="body">3. Enter the custom text you want to be spoken.</h1>',
                unsafe_allow_html=True)
    st.markdown('<div class="body">4. Adjust the guidance, top P, and top K parameters.</h1>',
                unsafe_allow_html=True)
    st.markdown('<div class ="body">5. Click the "Generate Voice" button to generate your new customized audio.</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # # Footer Section
    # st.markdown('<h1 class="header">Get Started with Clonify AI Voice Generator</h1>',
    #             unsafe_allow_html=True)

    # st.write(
    #     "Ready to bring your content to life? [Sign up today](/user_auth) or contact us for more information.")


if __name__ == "__main__":
    main()
