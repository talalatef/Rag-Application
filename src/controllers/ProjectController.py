from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignals
import os 

class ProjectController(BaseController):

    def __init__(self):
        super().__init__()

    def get_file_path(self, project_id:str):
        project_dir = os.path.join(
            self.file_path,
            project_id
        )

        if not os.path.exists(project_dir):
            os.mkdir(project_dir)
        
        return project_dir