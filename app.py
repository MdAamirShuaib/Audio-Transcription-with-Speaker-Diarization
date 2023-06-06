import streamlit as st
from transcriptionServices import englishTranscription
from wordCloud import generateWordCloud
import os


def main():
    os.environ[
        "API_TOKENS"
    ] = "ba95568cfd68462f99da2476a3fd57ca,6e88b49266ce4b5db5449071ea3c7508,d627deb9f64e44d4a4c554ea6842e184,eca9dec4d8614a7891fa7e69efcb517e,d72b75869a73428da298dea5436843ab,ef4957879d814ae4af47e8ac80c294e2"
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
