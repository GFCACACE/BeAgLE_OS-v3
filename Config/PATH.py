import os
import sys

def get_user_directory():
    # Get the absolute path of the current script (the file that calls this function)
    script_path = os.path.abspath(__file__)
    
    # Navigate up one level to get the project directory
    project_directory = os.path.dirname(os.path.dirname(script_path))
    
    project_directory=os.path.join(project_directory, "User")
    
    return project_directory

USER_SPACE_PATH = get_user_directory()

    