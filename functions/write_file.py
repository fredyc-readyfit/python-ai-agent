import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: exception writing file {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file with the provided content, constrained to the working directory. If the file doesn't exist it creates it. If the file exist it overwrites it.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write, relative to the working directory. Must be provided.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file. Must be provided."
            )
        },
    ),
)