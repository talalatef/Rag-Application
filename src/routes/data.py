from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignals
import aiofiles
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_date(project_id: str, file: UploadFile,
                    app_settings: Settings= Depends(get_settings)):
    data_controller = DataController()
    is_valid, signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":signal
            }
        )
    
    project_dir = ProjectController().get_file_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(
        orig_file_name=file.filename,
        project_id=project_id
    )

    async with aiofiles.open(file=file_path, mode='wb') as f:
        while chunk := await file.read(app_settings.FILE_DEFUELT_CHUNK_SIZE):
            await f.write(chunk)

    return JSONResponse(
            content={
                "signal": ResponseSignals.FILE_UPLOADED_SUCCESS.value
            }
    )