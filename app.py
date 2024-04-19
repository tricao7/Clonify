import streamlit as st

def load_file(file):
    try:
        content = file.read()
        return content
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def main():
    st.title('Voice Cloning App')

    uploaded_file = st.file_uploader("Upload a .wv file", type=".wv")

    if uploaded_file is not None:
        content = load_file(uploaded_file)
        
        if content is not None:
            st.write("File Content:")
            st.write(content)

if __name__ == "__main__":
    main()
