import pytest
from app.services.convert import convert_pdf_to_audio
from fastapi import UploadFile
from io import BytesIO

@pytest.mark.asyncio
async def test_convert_pdf_to_audio():
    pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Count 1 /Kids [3 0 R] >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >>\nendobj\n4 0 obj\n<< /Length 44 >>\nstream\nBT\n/F1 24 Tf\n100 700 Td\n(Hello, world!) Tj\nET\nendstream\nendobj\ntrailer\n<< /Root 1 0 R >>\n%%EOF"
    file = UploadFile(filename="test.pdf", file=BytesIO(pdf_content))
    audio_file_path = await convert_pdf_to_audio(file)
    assert audio_file_path.endswith(".mp3")
