# app/llm/steps.py
from typing import List, Dict, Any

def describe_steps(steps: List[Dict[str, Any]], language: str = "English") -> List[str]:
    """
    Offline, no-LLM fallback: generate very simple step descriptions
    based on OCR text in each segment.
    """
    descriptions = []

    for idx, step in enumerate(steps, start=1):
        texts = [f["text"] for f in step["frames"] if f.get("text")]
        combined_text = " ".join(texts).strip()

        if not combined_text:
            desc = f"Step {idx}: Perform an action on the screen."
        else:
            # Take first ~15 words as a hint
            words = combined_text.split()
            snippet = " ".join(words[:15])
            desc = f"Step {idx}: Interact with the part of the screen showing: \"{snippet}\"."

        descriptions.append(desc)

    return descriptions
