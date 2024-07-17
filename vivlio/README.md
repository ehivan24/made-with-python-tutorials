# made-with-python-tutorials
This repository is intended for python developers. Feel free to contribute new content, raise issues. 


# Projects

# Vivlío

Vivlío is a web application that converts PDF files into audiobooks.

## Features

- Upload a PDF file and get an audiobook in return
- Built with FastAPI
- Uses PyMuPDF for PDF processing and gTTS for text-to-speech conversion

## Installation

```bash
git clone https://github.com/ehivan24/made-with-python-tutorials
cd vivlio
poetry install
```

## Running the Application

```bash
just build && just up
```

## Docker

## API

- `POST /convert` - Upload a PDF file and get an audiobook