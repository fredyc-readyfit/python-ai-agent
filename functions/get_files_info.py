import os

def get_files_info(working_directory, directory=None):
    abs_working_directory = os.path.abspath(working_directory)
    target_dir = abs_working_directory
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not f"{target_dir}".startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        files_info = []
        dir_contents = os.listdir(target_dir)
        for c in dir_contents:
            c_path = os.path.join(target_dir, c)
            is_dir = os.path.isdir(c_path)
            # is_file = os.path.isfile(c_path)
            file_size = os.path.getsize(c_path)
            files_info.append(f"- {c}: file_size={file_size} bytes, is_dir={is_dir}")
            
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: exception listing files {e}"
