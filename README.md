# AI Summarizer

A Python AI-powered text summarization application built with the OpenAI API.

## Features

- Summarize text using AI

- Support short, medium, and detailed summaries

- Input validation

- Custom application exceptions

- OpenAI integration

- Request timeout

- Retry handling

- Logging

- Unit testing

- Mocking external API calls

- Environment-based configuration

## Architecture

The application follows a simple layered architecture:

```text
User
 │
 ▼
main.py
 │
 ▼
summarizer_service.py
 │
 ▼
api.py
 │
 ▼
OpenAI


ai-summarizer/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api.py
│   ├── exceptions.py
│   ├── utils.py
│   │
│   └── services/
│       ├── __init__.py
│       └── summarizer_service.py
│
├── tests/
│   ├── test_api.py
│   └── test_summarizer_service.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

## Installation

pip install -r requirements.txt

## Run the application

python -m src.main

## Testing
python -m pytest

python -m pytest -v

python -m pytest -v tests/test_summarizer_service.py

python -m pytest -v tests/test_api.py

python -m pytest -v tests/test_summarizer_service.py::test_empty_text