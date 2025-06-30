import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(["python", file_path], timeout=30, capture_output=True, cwd=abs_working_directory, text=True)
        
        if not result.stdout and not result.stderr:
            return "No output produced"
        
        output = ""
        if result.stdout:
            output += f"STDOUT: {result.stdout}\n"

        if result.stderr:
            output += f"STDERR: {result.stderr}\n"
        
        if not result.returncode == 0:
            output += "Process exited with code X"

        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

