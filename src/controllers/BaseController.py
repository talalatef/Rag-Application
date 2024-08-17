from helpers.config import get_settings, Settings
import os 
import random
import string

class BaseController:

    def __init__(self):
        self.app_settings = get_settings()
        
        self.base_dir = os.path.dirname( os.path.dirname( __file__ ) )
        self.file_path = os.path.join(
            self.base_dir,
            "assets/files"
        )
    def generate_random_string(self, length = 12):
        # Define the characters that can be used in the string
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate a random string from the defined characters
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
