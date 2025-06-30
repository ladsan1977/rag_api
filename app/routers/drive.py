from fastapi import APIRouter, HTTPException
from app.services.drive_service import list_drive_files

router = APIRouter()

@router.get("/list-drive-files")
def list_drive_files_route():
    files = list_drive_files()
    if not files:
        raise HTTPException(status_code=404, detail="No se encontraron archivos en el Drive.")
    return {"files": files}