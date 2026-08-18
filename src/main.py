import logging

from src.exceptions import AIProviderError, ValidationError
from src.services.summarize_service import summarize_text

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)"
)

logger = logging.getLogger(__name__)

def main():
    """Run the AI Summarizer appliction."""

    logger.info("Application started")

    try:
        text = input("Enter text to summarize: ")
        summary_length = input("Summary length (short/medium/detailed): ")

        summary = summarize_text(text=text,summary_length=summary_length)

        logger.info("Summarization completed")

        print("\nSummary")
        print("-" * 30)
        print(summary)

    except ValidationError as error:
        logger.warning("Invalid user input: %s",error)
        print(f"Input Error: {error}")

    except AIProviderError as error:
        logger.error("AI provider error: %s",error)

        print(f"AI Error: {error}")

    except Exception:
        logger.exception("unexpected application error")

        print("unexpected Error: "
               "Something went wrong"
        )

if __name__ == "__main__":
    main()


