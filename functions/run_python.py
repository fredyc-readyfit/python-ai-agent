import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands, 
            timeout=30, 
            capture_output=True, 
            cwd=abs_working_directory, 
            text=True,
        )
        
        output = ""
        if result.stdout:
            output += f"STDOUT:\n{result.stdout}\n"

        if result.stderr:
            output += f"STDERR:\n{result.stderr}\n"
        
        if result.returncode != 0:
            output += "Process exited with code X"

        return output if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

