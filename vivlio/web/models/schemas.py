from pydantic import BaseModel


class AudioResponse(BaseModel):
    audio_file_path: str
