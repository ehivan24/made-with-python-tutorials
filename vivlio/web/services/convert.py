import os

import aiofiles
import fitz  # PyMuPDF
from fastapi import UploadFile
from gtts import gTTS


async def convert_pdf_to_audio(file: UploadFile) -> str:
    # Save the uploaded file
    file_location = f"web/tmp/{file.filename}"
    async with aiofiles.open(file_location, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    # Read the PDF
    doc = fitz.open(file_location)
    text = ""
    for page in doc:
        text += page.get_text()

    # Convert text to speech
    tts = gTTS(text)
    audio_file_path = f"web/tmp/{os.path.splitext(file.filename)[0]}.mp3"
    tts.save(audio_file_path)

    return audio_file_path
