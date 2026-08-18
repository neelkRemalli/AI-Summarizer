from unittest.mock import patch

import pytest

from src.exceptions import ValidationError
from src.services.summarizer_service import (
    summarize_text,
)


def test_empty_text():
    with pytest.raises(ValidationError):
        summarize_text(
            "",
            "short",
        )


def test_whitespace_text():
    with pytest.raises(ValidationError):
        summarize_text(
            "   ",
            "short",
        )


def test_invalid_summary_length():
    with pytest.raises(ValidationError):
        summarize_text(
            "Artificial intelligence is useful.",
            "banana",
        )


def test_empty_summary_length():
    with pytest.raises(ValidationError):
        summarize_text(
            "Artificial intelligence is useful.",
            "",
        )


@patch(
    "src.services.summarizer_service.generate_text"
)
def test_summarize_text(mock_generate_text):
    mock_generate_text.return_value = (
        "AI is a field of computer science."
    )

    result = summarize_text(
        text=(
            "Artificial intelligence is a field "
            "of computer science."
        ),
        summary_length="short",
    )

    assert result == (
        "AI is a field of computer science."
    )

    mock_generate_text.assert_called_once()