from enum import Enum

class ResponseSignals(Enum):

    FILE_TYPE_NOT_SUPPORTED="file type not supported"
    FILE_SIZE_EXCEDDED="file size excedded 10 mb"
    VALIDATION_SUCCESS="validation for file is Successed"
    VALIDATION_FAILED="validation for file is Failed"
    FILE_UPLOADED_SUCCESS = "file uploaded success and saved in assets"