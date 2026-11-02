"""Ask a plain LLM questions while preserving conversation history.

Usage:
    uv run python -m app.ask "What is LoRA?"
    AIE_MODEL=gemini-3.5-flash uv run python -m app.ask "What is LoRA?"

After startup, ask follow-up questions using the same conversation history.
Compare response times and token counts across models and questions.
In Session 3, improve this with an agent that can search the glossary.
"""

import argparse
from time import perf_counter

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# The correct answer to this course-specific question is in the homework-levels glossary entry.
DEFAULT_QUESTION = "What are the three homework levels in the AIE2026 course?"


def ask(chat, question: str) -> None:
    started_at = perf_counter()
    response = chat.send_message(question)
    elapsed = perf_counter() - started_at

    usage = response.usage_metadata
    input_tokens = usage.prompt_token_count if usage else None
    output_tokens = usage.candidates_token_count if usage else None
    print(response.text or "")
    print(
        f"[Metrics] time={elapsed:.2f}s "
        f"input={input_tokens if input_tokens is not None else 'N/A'} tokens "
        f"output={output_tokens if output_tokens is not None else 'N/A'} tokens"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ask a plain LLM questions while preserving conversation history"
    )
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    client = genai.Client(api_key=get_api_key())
    chat = client.chats.create(model=MODEL)
    print(f"[Model] {MODEL}")
    try:
        question = args.question
        while True:
            if question:
                print(f"\n[Question] {question}")
                ask(chat, question)

            try:
                question = input("\nAsk a follow-up question (type 'exit' to quit): ").strip()
            except EOFError:
                break
            if question.lower() in {"exit", "quit", "/exit", "/quit"}:
                break
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
