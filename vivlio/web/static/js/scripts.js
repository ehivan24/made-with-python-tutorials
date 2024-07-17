document.getElementById('upload-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('file-input');
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/convert', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `<a href="/${result.audio_file_path}" download>Download Audiobook</a>`;
});
