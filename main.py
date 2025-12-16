import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("no Gemini API key found")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    
    args = parser.parse_args()
    prompt = args.user_prompt



    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)
    
    if response.usage_metadata:
        metadata = response.usage_metadata
    else:
        raise RuntimeError("Gemini response metadata not found")
    tokens_in_prompt = metadata.prompt_token_count
    tokens_in_response = metadata.candidates_token_count
    result = response.text

    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {tokens_in_prompt}")
        print(f"Response tokens: {tokens_in_response}")

    print(result)

if __name__ == "__main__":
    main()
