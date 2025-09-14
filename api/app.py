import numpy as np
import cv2 as cv
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response 
from document_scanner import pipelines

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/scan", response_class = Response, responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Returns a PDF file generated from the scanned image",
        }
    })
def image_scan(image: UploadFile = File(...)):
    cv_img = uploadfile_to_cv2_image(image)
    pdf_bytes = pipelines.process_basic(cv_img, debug= False) 

    # Return as raw bytes with correct content type
    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=document.pdf"}
    )
def uploadfile_to_cv2_image(file: UploadFile):
    # ✅ Synchronous read
    contents = file.file.read()
    # Bytes → np array → OpenCV image
    np_array = np.frombuffer(contents, np.uint8)
    img = cv.imdecode(np_array, cv.IMREAD_COLOR)
    return img