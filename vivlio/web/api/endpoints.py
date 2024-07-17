from fastapi import APIRouter, File, UploadFile
from icecream import ic

from web.services.convert import convert_pdf_to_audio

router = APIRouter()


@router.post("/convert")
async def convert(file: UploadFile = File(...)):
    audio_file_path = await convert_pdf_to_audio(file)
    ic(f"{audio_file_path=}")
    return {"audio_file_path": audio_file_path}
