import os
import sys
from google import genai
from google.genai import types

api_key = os.getenv("LLM_API_KEY")
if not api_key:
    print("Error: LLM_API_KEY not found in environment variables.")
    sys.exit(1)

client = genai.Client(api_key=api_key)
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
        "Return ONLY the clean Python code. Do not include any explanations, markdown formatting, or backticks."
    )

    print("Sending code to Google Gemini for auto-improvement...")
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Here is the current code:\n\n{current_code}",
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.6,
            ),
        )
        
        improved_code = response.text.strip()
        
        backticks = '`' * 3
        if improved_code.startswith(backticks + "python"):
            improved_code = improved_code[9:]
            if improved_code.endswith(backticks):
                improved_code = improved_code[:-3]
        elif improved_code.startswith(backticks):
            improved_code = improved_code[3:]
            if improved_code.endswith(backticks):
                improved_code = improved_code[:-3]
                
        improved_code = improved_code.strip()

        if improved_code and improved_code != current_code:
            with open(TARGET_FILE, "w", encoding="utf-8") as f:
                f.write(improved_code)
            print("Success: Code updated by Gemini Agent.")
        else:
            print("No improvements made (code is identical).")

    except Exception as e:
        print(f"API Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()