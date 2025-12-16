import os
import argparse
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("no Gemini API key found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    response = client.models.generate_content(model="gemini-2.5-flash", contents=args.user_prompt)
    
    if response.usage_metadata:
        metadata = response.usage_metadata
    else:
        raise RuntimeError("Gemini response metadata not found")
    tokens_in_prompt = metadata.prompt_token_count
    tokens_in_response = metadata.candidates_token_count
    result = response.text

    print(f"Prompt tokens: {tokens_in_prompt}")
    print(f"Response tokens: {tokens_in_response}")

    print(result)

if __name__ == "__main__":
    main()
