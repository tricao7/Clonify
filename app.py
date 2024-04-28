import json
import os
from datetime import datetime, timezone

import requests
import scipy.io.wavfile as wav
import streamlit as st


def get_current_utc_datetime() -> str:
    """
    Get the current datetime with UTC timezone
    """
    current_utc_datetime = datetime.now(timezone.utc)
    # Return the datetime as a string
    return str(current_utc_datetime)


def check_length(data, rate=44100):
    """
    Checks to see if an uploaded audio file is longer than 30 seconds.
    Parameters:
        - data: audio data
        - rate: sample rate of the audio file (default is 44100)
    Returns:
        - True if the audio file is longer than 30 seconds
        - False if the audio file is shorter than 30 seconds
    """
    if len(data) / rate <= 30:
        return False
    return True


def save_uploaded_file(uploaded_file: bytes, save_path: str) -> str:
    """
    Saves the uploaded file to the specified path.
    Parameters:
        - uploaded_file: the uploaded file object
        - save_path: the path to save the uploaded file
    Returns:
        - save_path: the path where the file was saved
    """
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Read the uploaded file content
    file_content = uploaded_file.read()

    # Write the content to the specified file path
    with open(save_path, "wb") as f:
        f.write(file_content)

    return save_path


def tts_request(
    text: str,
    content: str = None,
    speaker_ref_path: str = None,
    guidance: float = 3.0,
    top_p: float = 0.95,
    top_k: int = None,
) -> bytes:
    """
    Create a POST request to the TTS server to generate voice from text.
    Parameters:
        - text: the text to be spoken
        - content: the content of the uploaded file
        - speaker_ref_path: the path to the reference speaker file
        - guidance: the guidance parameter
        - top_p: the top P parameter
        - top_k: the top K parameter
    Returns:
        - response.content: the content of the generated audio file
    """
    payload = {
        "text": text,
        "speaker_ref_path": speaker_ref_path,
        "guidance": guidance,
        "top_p": top_p,
        "top_k": top_k,
    }

    headers = {"X-Payload": json.dumps(payload)}
    files = {"file": ("uploaded_file.wav", content, "audio/wav")}

    # Process the request
    response = requests.post("http://localhost:58003/tts", files=files, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.content


def main():
    # Display image and center
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

    # Display horizontal line
    st.markdown("---")

    # Get uploaded file from user
    uploaded_file = st.file_uploader(
        "Upload a .wav / .mp3 / .flac file (30 seconds min):",
        type=["wav", "mp3", "flac"],
    )

    if uploaded_file is not None:
        # Read the uploaded audio file
        rate, data = wav.read(uploaded_file)
        # Make sure the audio file is longer than 30 seconds
        if not check_length(data, rate):
            st.error("Input audio file must be longer than 30 seconds.", icon="🚨")
            return

        # Initialize the save path and current time
        tnow = get_current_utc_datetime()
        save_path = "/home/files/input/" + tnow + uploaded_file.name
        # Save the uploaded file to the specified path
        save_uploaded_file(uploaded_file, save_path)

        # Display the Uploaded Audio
        st.audio(uploaded_file, format="wav")

    text_input = st.text_area(
        "Enter text to be spoken (Max 220 characters):", max_chars=220
    )

    # Add slider with increased font size
    guidance = st.slider(
        "Guidance",
        min_value=0.0,
        max_value=10.0,
        value=3.0,
        step=0.1,
        help="Guidance controls the amount of control the user has over the \
            generated audio. A higher value will result in more control over the generated audio.",
    )
    top_p = st.slider(
        "Top P",
        min_value=0.0,
        max_value=1.0,
        value=0.95,
        step=0.01,
        help="Top P controls the probability of the model choosing the next token. \
            A higher value will result in less randomness in the generated audio.",
    )
    top_k = st.number_input(
        "Top K",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        help="Top K controls the number of tokens to consider for the next token.",
    )

    # Generate voice
    if st.button("Generate Voice"):
        content = uploaded_file.read()
        if content:
            st.write("Generated Audio:")
            # create a request to the TTS server
            output = tts_request(
                text_input,
                save_path,
                speaker_ref_path=save_path,
                guidance=guidance,
                top_p=top_p,
                top_k=top_k,
            )
            if output:
                st.audio(output, format="audio/wav")
            else:
                st.error("Error generating voice")
        else:
            st.error("No file uploaded")


def get_binary_file_downloader_html(
    bin_file: bytes, file_label: str = "File", file_name: str = "file.wav"
) -> str:
    """
    Generates a link to download the given binary file.
    Parameters:
        - bin_file: the binary file content
        - file_label: the label of the download link
        - file_name: the name of the file to be downloaded
    Returns:
        - href: the HTML code for the download link
    """
    with open(file_name, "wb") as f:
        f.write(bin_file)
    href = f'<a href="data:file/wav;base64,{bin_file.decode()}" download="{file_name}">{file_label}</a>'
    return href


if __name__ == "__main__":
    main()
