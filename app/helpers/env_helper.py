import os

def get_env_variable(variable_name):
    # Try environment variable directly
    value = os.getenv(variable_name)
    if value is not None:
        return value
    
    # If not found, try to load from a .env file
    try:
        from dotenv import load_dotenv
        dotenv_path = '/Users/abhayhasrani/myVsCode/Book/Book_Library_FastApi/.env'  # Specify the path to your .env file
        load_dotenv(dotenv_path)
        value = os.environ.get(variable_name)
        if value is not None:
            return value
    except ImportError:
        pass 