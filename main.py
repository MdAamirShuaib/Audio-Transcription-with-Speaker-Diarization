from fastapi import FastAPI, File, UploadFile, Form
from transcriptionServices import englishTranscription
from typing import List
from wordCloud import generateWordCloud
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/transcribe_english/")
async def transcribe_english(files: List[UploadFile] = File(...)):
    errors, data = await englishTranscription.start_transcription(files)
    return {"data": data, "errors": errors}


@app.post("/generate_word_cloud/")
async def generate_word_cloud(
    text: str = Form(...), wordCount: int = Form(...), removeWords: str = Form(...)
):
    return generateWordCloud.word_cloud(text, wordCount, removeWords)


@app.get("/")
async def response_default():
    return {"detail": "Analytics API Backend"}
