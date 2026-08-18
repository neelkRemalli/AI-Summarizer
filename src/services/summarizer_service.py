from src.api import generate_text
from src.exceptions import ValidationError
from src.utils import clean_text


ALLOWED_SUMMARY_LENGTHS = {
    "short",
    "medium",
    "detailed"
}

def summarize_text(text:str,summary_length:str) -> str:
    "Generate a summary of the provided text"

    text = clean_text(text)
    summary_length = clean_text(summary_length)

    if not text:
        raise ValidationError("Text can not be empty")

    if summary_length not in ALLOWED_SUMMARY_LENGTHS:
        raise ValidationError("summary_length must be short, medium or detailed")

    prompt = f"""
    You ar a professional text summarizer.
    
    Summarize the following text.

    summary length: {summary_length}

    Rules:
    - Preserve the important information.
    - Do not invent informantion.
    - Use clear and concise language.
    - return only the summary.

    Text:
    {text}
    """
    return generate_text(prompt)



