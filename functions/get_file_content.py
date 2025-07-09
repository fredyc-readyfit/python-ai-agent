import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_string
    except Exception as e:
        return f"Error: exception reading file {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="List the content of a file up to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to list the content file from, relative to the working directory. Must be provided.",
            ),
        },
    ),
)