import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types
from call_function import available_functions, call_function
from prompts import system_prompt

# system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''

def main():
    # Load Environment Variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("Usage: python3 main.py <prompt> [--verbose]")
        sys.exit(1)
    
    # Create a new instance of genai
    client = genai.Client(api_key=api_key)

    # response = client.models.generate_content(model="gemini-2.0-flash-001", contents=sys.argv[1])

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )

    print("Response:")
    if not response.function_calls:
        return response.text
    
    for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if not function_call_result.parts[0].function_response.response:
                 raise Exception("Something went wrong!")
            
            if verbose:
                 print(f"-> {function_call_result.parts[0].function_response.response}")


    # print(response.text)

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()