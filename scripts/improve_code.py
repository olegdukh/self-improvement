import os
import sys
from openai import OpenAI

api_key = os.getenv("LLM_API_KEY")
if not api_key:
    print("Error: LLM_API_KEY not found in environment variables.")
    sys.exit(1)

client = OpenAI(api_key=api_key)
TARGET_FILE = "target_code.py"

def main():
    if not os.path.exists(TARGET_FILE):
        print(f"Error: Target file {TARGET_FILE} not found.")
        sys.exit(1)

    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        current_code = f.read()

    system_prompt = (
        "You are a Senior Python Developer. Your job is to refactor the code in target_code.py.\n"
        "You can: optimize algorithms, add type hinting, add docstrings, and handle exceptions.\n"
        "⚠️ CRITICAL RULE: You are strictly forbidden to change the function name 'calculate' or its argument count. "
        "The function must accept two arguments and return their sum. If you break this logic, the automated tests will fail!\n"
        "Return ONLY the clean Python code. Do not include any explanations, markdown formatting, or backticks (```)."
    )

    print("Sending code to LLM for auto-improvement...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is the current code:\n\n{current_code}"}
            ],
            temperature=0.6
        )
        
        improved_code = response.choices[0].message.content.strip()
        
        # Clean up occasional markdown block wrapping from LLM
        if improved_code.startswith("```python"):
            improved_code = improved_code.split("```python")[1].split("```")[0].strip()
        elif improved_code.startswith("```"):
            improved_code = improved_code.split("```")[1].split("```")[0].strip()

        if improved_code and improved_code != current_code:
            with open(TARGET_FILE, "w", encoding="utf-8") as f:
                f.write(improved_code)
            print("Success: Code updated by LLM Agent.")
        else:
            print("No improvements made (code is identical).")

    except Exception as e:
        print(f"API Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()