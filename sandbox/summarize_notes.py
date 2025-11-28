import traceback

from services.summarization_service import (
    summarize_notes,
    DummyLLMClient
)



def main():
    note_id = input("Enter Note's ID to summarize:").strip()

    if not note_id:
        print("Note's id is required")
        return
    
    mode = input("Summary mode? (short/detailed) [short]: ").strip() or "short"
    if mode not in ("short", "detailed"):
        print("Invalid mode. Use 'short' or 'detailed'.")
        return
    
    llm = DummyLLMClient()

    try:
        summary = summarize_notes(
            note_id=note_id,
            llm = llm,
            mode=mode,
            max_chunks= 10
        )
        print("\n ===Summary Result:===")
        print(summary)

    except Exception as e:
        print(f"Error while summarizing: {e}:\n{traceback.print_exc()}")


if __name__ == "__main__":
    main()