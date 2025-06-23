import os

def get_files_info(working_directory, directory=None):
    working_directory = os.path.abspath(working_directory)
    directory = os.path.abspath(os.path.join(working_directory, directory))

    if not f"{directory}".startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        dir_contents = os.listdir(directory)
        for c in dir_contents:
            c_path = os.path.join(directory, c)
            is_dir = os.path.isdir(c_path)
            # is_file = os.path.isfile(c_path)
            file_size = os.path.getsize(c_path)
            files_info.append(f"- {c}: file_size={file_size} bytes, is_dir={is_dir}\n")
            
        return "".join(files_info)
    except:
        return f"Error: Unexpected error"