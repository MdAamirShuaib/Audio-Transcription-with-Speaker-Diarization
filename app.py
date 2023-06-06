import streamlit as st
from transcriptionServices import englishTranscription
from wordCloud import generateWordCloud
import os


def main():
    tokens = os.environ["API_TOKENS"].split(",")
    print(tokens)
    st.set_page_config(
        page_title="Audio Transcription", page_icon=":speaker:", layout="wide"
    )
    st.title("Audio Transcription with Speaker Diarization")

    uploaded_file = st.file_uploader("Choose a file", type=["mp3", "wav", "mp4"])
    transcribe = st.button("Transcribe")

    if transcribe:
        if uploaded_file is not None:
            with st.spinner("Transcribing..."):
                data = englishTranscription.start_transcription(uploaded_file, tokens)
                print(data)
            st.table(data)
        else:
            st.write("Please upload a file")

    # wordclouds = generateWordCloud.word_cloud(text, wordCount, removeWords)


if __name__ == "__main__":
    main()
