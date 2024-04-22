import streamlit as st
import requests 
import json
import os

def save_uploaded_file(uploaded_file, save_path):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Read the uploaded file content
    file_content = uploaded_file.read()
    
    # Write the content to the specified file path
    with open(save_path, "wb") as f:
        f.write(file_content)

    return save_path
    
def tts_request(text, content, speaker_ref_path=None, guidance=3.0, top_p=0.95, top_k=None):
    payload = {
        "text": text,
        "speaker_ref_path": speaker_ref_path,
        "guidance": guidance,
        "top_p": top_p,
        "top_k": top_k
    }

    headers = {"X-Payload": json.dumps(payload)}
    files = {'file': ('uploaded_file.wav', content, 'audio/wav')}
    
    response = requests.post("http://localhost:58003/tts", files=files, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.content
    # except requests.RequestException as e:
    #     st.error(f"Error generating voice: {e}")
    #     return None

# do you want preset or do you want your own
# if preset, then choose from a list of presets

# if you want your own, upload yours own
def main():
    st.title('Voice Cloning App')

    uploaded_file = st.file_uploader("Upload a .wav file", type=".wav")

    if uploaded_file is not None:
        save_path = 'metavoice/fam/llm/' + uploaded_file.name  

        # Save the uploaded file to the specified path
        saved_file_path = save_uploaded_file(uploaded_file, save_path)

        st.write(f"File saved at: {saved_file_path}")

        st.audio(uploaded_file, format="wav")

        text_input = st.text_area("Enter text to be spoken (Max 220 characters):", max_chars=220)

    # Add slider with increased font size
    guidance = st.slider("Guidance", min_value=0.0, max_value=10.0, value=3.0, step=0.1, help='Guidance is a parameter that controls the amount of control the user has over the generated audio. A higher value will result in more control over the generated audio.')
    top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.95, step=0.01, help='Top P is a parameter that controls the probability of the model choosing the next token. A higher value will result in more randomness in the generated audio.')
    top_k = st.number_input("Top K", min_value=1, max_value=100, value=50, step=1, help='Top K is a parameter that controls the number of tokens to consider for the next token. A higher value will result in more randomness in the generated audio.')

    if st.button("Generate Voice"):
        content = uploaded_file.read()
        if content:
            st.write("Generated Audio:")
            fname = '/home/rishimohan/tts/VoiceCloning/metavoice/fam/llm/' + uploaded_file.name
            output = tts_request(text_input, fname, speaker_ref_path=fname, guidance=guidance, top_p=top_p, top_k=top_k)
            if output:
                st.audio(output, format='audio/wav')
                # st.markdown(get_binary_file_downloader_html(output, file_label='Download Audio', file_name='output.wav'), unsafe_allow_html=True)
            else:
                st.error("Error generating voice")

def get_binary_file_downloader_html(bin_file, file_label='File', file_name='file.wav'):
    with open(file_name, 'wb') as f:
        f.write(bin_file)
    href = f'<a href="data:file/wav;base64,{bin_file.decode()}" download="{file_name}">{file_label}</a>'
    return href


if __name__ == "__main__":
    main()
