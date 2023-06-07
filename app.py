import streamlit as st
from transcriptionServices import englishTranscription
from wordCloud import generateWordCloud
from dotenv import load_dotenv
from htmlTemplates import footer, completed
import os


def main():
    load_dotenv()
    TranscriptionComplete = False
    tokens = os.environ["API_TOKENS"].split(",")
    st.set_page_config(
        page_title="Audio Transcription", page_icon=":speaker:", layout="wide"
    )
    st.title("Audio Transcription with Speaker Diarization")

    with st.sidebar:
        uploaded_file = st.file_uploader("Choose a file", type=["mp3", "wav", "mp4"])
        transcribe = st.button("Transcribe")
        getwordcloud = st.checkbox("Generate Word Cloud")

        if transcribe:
            if uploaded_file is not None:
                with st.spinner("Transcribing..."):
                    data = englishTranscription.start_transcription(
                        uploaded_file, tokens
                    )
                    print(data)
                    if getwordcloud:
                        textList = data["utter"].values.tolist()
                        text = " ".join(textList)
                        wordclouds = generateWordCloud.word_cloud(text)
                    TranscriptionComplete = True
                st.write(
                    completed.replace("{{text}}", "Transcription Complete"),
                    unsafe_allow_html=True,
                )
            else:
                st.write("Please upload a file")
    if TranscriptionComplete:
        st.table(data)
        col1, col2 = st.columns(2)
        with col1:
            st.pyplot(wordclouds)
    st.markdown(footer, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
